<script setup lang="ts">
definePageMeta({
    layout: 'pages'
})
import { shallowRef } from 'vue';
import type { YMap } from '@yandex/ymaps3-types';
import {
  YandexMap,
  YandexMapDefaultSchemeLayer,
  YandexMapDefaultFeaturesLayer,
  YandexMapDefaultMarker,
} from 'vue-yandex-maps';

//Можно использовать для различных преобразований
const map = shallowRef<null | YMap>(null);

import { apiConfig, base_url } from '@/api/api';
import { useAuthStore } from '@/stores/auth';
const {isAuthenticated} = storeToRefs(useAuthStore());
const route = useRoute()
const trip_id = route.params.id
const {data: trip, pending} = await useFetch(`${apiConfig.trips}${trip_id}`)

// Функция для извлечения времени из даты
const extractTime = (dateString) => {
  const date = new Date(dateString) // Преобразуем строку в объект Date
  const hours = String(date.getHours()).padStart(2, '0') // Получаем часы и добавляем ведущий ноль
  const minutes = String(date.getMinutes()).padStart(2, '0') // Получаем минуты и добавляем ведущий ноль
  return `${hours}:${minutes}` // Форматируем время
}


// Функция для форматирования даты
const formatDate = (dateString) => {
  const date = new Date(dateString) // Преобразуем строку в объект Date
  const day = String(date.getDate()).padStart(2, '0') // Получаем день
  const options = { month: 'short', weekday: 'short' } // Опции для форматирования месяца и дня недели
  const month = new Intl.DateTimeFormat('ru-RU', options).format(date).split(' ')[0] // Получаем сокращенное название месяца
  const weekday = new Intl.DateTimeFormat('ru-RU', { weekday: 'short' }).format(date) // Получаем сокращенное название дня недели
  return `${day} ${month}, ${weekday}` // Форматируем строку
}

// Метод для получения форматированного времени
const getFormattedTripInTime = () => {
  return extractTime(trip?.value?.trip_in_time)
}

// Метод для получения форматированного времени
const getFormattedtrip_out_time = () => {
  return extractTime(trip?.value?.trip_out_time)
}

import axios from 'axios'

const startCity = 'Москва' // Название начального города
const endCity = 'Санкт-Петербург' // Название конечного города
const apiKey = '8817a9d8-7d4e-40b7-b810-c68354620fb6' // Ваш API ключ Яндекс.Карт

</script>
<template>
    <div class="trip_title">
        <h1>
            <div>Поездка #{{trip_id}} | {{trip?.city?.name}} — {{trip?.cityin?.name}}</div>
            <!-- <span style="padding: 10px 15px;border: 1px solid;border-radius: 49px;font-size: 17px;margin: 0px 15px 0px 0px;font-weight: 700;" v-if="trip?.country" v-for="country in travel?.country">{{country?.name}}</span> -->
            <!-- ,,  -->
        </h1> 
    </div>
    <div class="trip_information">
        <div class="trip_left">
        <div class="trip_user">
        <img v-if="trip?.user?.photo?.length > 0" :src="trip?.user?.photo" alt="">
        <img v-else src="~/assets/img/photo.png" alt="">

        <div class="trip_user_info">
            <NuxtLink :to="`/profile/${trip?.user?.id}`"><h2>{{trip?.user?.first_name}} {{trip?.user?.last_name}}</h2></NuxtLink>
            <div class="trip_user_info_list">
                <span style="
                border-radius: 15px;
                padding: 5px 10px 5px 10px;
                background-color: #128ce91e;
                font-weight: 700;
                font-size: 14px;
                color: #2963d6;
                margin: 0px 15px 0px 0px;
                width: max-content;
                ">
                Водитель
       <!-- {{travel?.gender}} ищет {{travel?.gender_search}} -->
                 <!----> 
                 </span> <p><span><img src="~/assets/img/pic_location_grey.png" alt=""></span>, 0 отзывов</p> 
            </div>

        </div>
    </div>

    <div class="trip_description">
        <h3>Дополнительные опции</h3>
        <!-- <p>{{travel?.description}}</p> -->
        
        <div class="trip_interests">
            <!-- <h3>Интересы</h3> -->
            <div class="trip_interests_list">
                <span v-for="other in trip?.trip_others">
                <img :src="`${other?.image}`" alt="">
                {{other.name}}
                </span>
            </div>
        </div>
    </div>


    <div class="trip_description">
        <!-- <h3>Цель поездки</h3> -->
        <!-- <p>{{travel?.description}}</p> -->
        
        <div class="trip_users">
            <h3>Пассажиры</h3>
            <div class="trip_interests_list">
                <NuxtLink to=""><span v-for="user in trip?.trip_users">
                    <img :src="user?.photo" alt="">
                    {{user?.first_name}}
                    </span>
                </NuxtLink>
            </div>
        </div>
    </div>

    <yandex-map
      v-model="map"
      :settings="{
        location: {
          center: [37.617644, 55.755819],
          zoom: 9,
        },
      }"
      width="100%"
      height="500px"
  >
    <yandex-map-default-scheme-layer/>
    <yandex-map-default-features-layer/>
    <yandex-map-default-marker :settings="{ coordinates: [37.617644, 55.755819] }"/>
  </yandex-map>
    </div>
    <div class="trip_right">
        <div class="trip_ticket">
            <h4>Детали поездки</h4>
            <ul>
                <li>
                    <span>
                        <div>
                            Пункт отправления:
                        </div>
                    </span>
                    {{trip?.city?.name}}
                </li>
                <li>
                    <span>
                        <div>
                            Конечный пункт:
                        </div>
                    </span>
                    {{trip?.cityin?.name}}
                </li>
                <li>
                    <span>
                        <div>Свободных мест:</div>
                    </span>
                    {{trip?.free_seats}}
                </li>
                <li>
                    <span>
                        <div>
                            Дата поездки:
                        </div>
                    </span>
                     {{formatDate(trip?.trip_in_time)}}, {{getFormattedTripInTime()}}
                </li>
                <li>
                    <span>
                        <div>
                            Дата прибытия:
                        </div>
                    </span>
                     {{formatDate(trip?.trip_out_time)}}, {{getFormattedtrip_out_time()}}
                </li>
                <li>
                    <span>
                        <div>
                            Кол-во попутчиков:
                        </div>
                    </span>
                    {{trip?.trip_users?.length}}
                </li>
                <li>
                    <span>
                        <div>
                            Цена поездки:
                        </div>
                    </span>
                    {{trip?.price}} руб.
                </li>
                <!-- <li><span><div>Поиски:</div></span> {{ travel?.gender }} ищет {{travel?.gender_search}}</li>
                <li><span><div>Начало: путешествия</div></span> {{travel?.date}}</li>
                <li><span><div>Срок путешествия:</div></span> {{travel?.days}} дней</li>
                <li><span><div>Уже путешествует:</div></span> <template v-if="travel?.travel_now">Да</template><template v-else>Нет</template></li> -->
            </ul>
            <template v-if="isAuthenticated">
                <button v-if="trip?.free_seats == 0" style="background-color: rgb(195 195 195);color: #151515;">Места заняты</button>
                <button v-else>Забронировать поездку</button>
            </template>
            <template v-else>
                <NuxtLink to="/login"><button>Авторизируйтесь на сайте</button></NuxtLink>
            </template>

        </div>
    </div>
    </div>


</template>
<style scoped>
.trip_user_info_list{
    display: flex;
    align-items: center;
    margin: 5px 0px 0px 0px;
}

.trip_ticket{
    width: 100%;
    padding: 15px 15px 15px 15px;
    border-radius: 15px;
    background-color: #FFFFFF;
    
    && button{
        background-color: blue;
        background-color: #2963d6;
        padding: 15px 15px 15px 15px;
        width: 100%;
        font-size: 17px;
        font-weight: 700;
        color: #FFFFFF;
        text-align: center;
        border-radius: 15px;
        text-overflow: ellipsis;
        overflow: hidden;
        white-space: nowrap;
    }

    && button:hover{
        opacity: 0.9;
    }
    
    && ul{
        line-height: 2;
        margin: 15px 0px 25px 0px;
    }

    && li{
        display: flex;
        align-items: center;
        font-weight: 600;
    }
    && h3{
        font-size: 20px;
    }
    && h4{
        font-size: 20px;
        margin: 0px 0px 25px 0px;
    }

    && span{
        /* border-bottom: 1px dashed; */
        display: flex;
        flex-grow: 1;
        align-items: baseline;
        min-width: max-content;
        flex-wrap: nowrap;
        font-weight: 500;
    }
    && span::after{
        content: "";
        width: 100%;
        border-bottom: 2px dotted;
    }

    && div{
        min-width: max-content;
    }
}
.trip_information{
    display: flex;
    justify-content: space-between;
}

.trip_right{
    width: 100%;
    max-width: 379px;
    margin: 0px 0px 0px 15px;
}
.trip_left{
    width: 100%;
}
.trip_interests_list{
    display: flex;
    flex-wrap: wrap;

    && img{
        max-width: 19px;
        max-height: 19px;
        object-fit: cover;
        width: 100%;
        height: 100%;
        margin: 0px 5px 0px 0px;
    }
}
.trip_interests{
    width: 100%;
    display: flex;
    flex-direction: column;
    margin: 15px 0px 0px 0px;

    h3{
        margin: 15px 0px 15px 0px;
    }
    
    && span{
        padding: 10px 15px 10px 15px;
        border-radius: 50px;
        border: 1px solid rgb(195, 195, 195);
        display: flex;
        align-items: center;
        width: max-content;
        margin: 0px 10px 0px 0px;
    }
}
.trip_users{
    width: 100%;
    display: flex;
    flex-direction: column;
    margin: 0px 0px 0px 0px;

    h3{
        margin: 0px 0px 15px 0px;
    }
    
    && span{
        padding: 10px 15px 10px 15px;
        border-radius: 50px;
        border: 1px solid rgb(195, 195, 195);
        display: flex;
        align-items: center;
        width: max-content;
        margin: 0px 10px 0px 0px;
    }
}

.trip_description{
    width: 100%;
    padding: 15px 15px 15px 15px;
    background-color: #FFFFFF;
    border-radius: 15px;
    margin: 15px 0px 0px 0px;

    && h3{
        margin: 0px 0px 10px 0px;
    }

    && p{
        min-height: 100px;
        border-bottom: 1px solid #dedede;
    }
}

.trip_title{
    margin: 0px 0px 25px 0px;

    && h1{
        font-size: clamp(24px, 4vw, 40px);
    }
}

.trip_user{
    width: 100%;
    padding: 15px 15px 15px 15px;
    background-color: #FFFFFF;
    border-radius: 15px;
    display: flex;
    align-items: center;

    && img{
        width: 100%;
        height: 100%;
        min-width: 69px;
        min-height: 69px;
        object-fit: cover;
        max-width: 69px;
        max-height: 69px;
        border-radius: 100%;
        margin: 0px 15px 0px 0px;
    }
}

.trip_user_info{
    width: 100%;
    display: flex;
    flex-direction: column;

    && h2{
        font-size: 20px;
        margin: 0px 0px 5px 0px;
    }

    && span{
        display: flex;
        align-items: center;
    }

    && img{
        width: 19px;
        height: 19px;
        object-fit: cover;
        max-width: 19px;
        max-height: 19px;
        min-width: 19px;
        min-height: 19px;
        margin: 0px 0px 0px 0px;
    }
    && p{
        display: flex;
        align-items: center;
    }
}
.__ymap{
    padding: 15px 15px 15px 15px;
    margin: 15px 0px 0px 0px;
    border-radius: 15px;
    background-color: #FFFFFF;
}
@media (max-width: 960px){
    .trip_right{
        margin: 15px 0px 0px 0px;
        max-width: 100%;
    }
    .trip_information{
        flex-direction: column;
    }
}
</style>