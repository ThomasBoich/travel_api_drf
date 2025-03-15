<script setup>
definePageMeta({
  layout: 'pages'
});
// Получаем объект маршрута
const route = useRoute();
import axios from 'axios';
// Извлекаем параметры из маршрута
const fromCity = route.params._fromCity; // Параметр из URL
const goCountry = route.params._goCountry; // Параметр из URL

import {API, apiConfig, base_url} from '@/api/api'
// const {data: travels, pending} = await useFetch(apiConfig.travels)

const users = ref([]);
const error = ref(null);
const pending = ref(true);

// Функция для создания задержки
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

const fetchTravels = async () => {
  try {
    await delay(0); // Задержка в 2 секунды
    const response = await axios.get(apiConfig.users);
    users.value = response.data;
  } catch (err) {
    error.value = err;
  } finally {
    pending.value = false; // Устанавливаем pending в false после завершения запроса
  }
};

const page = ref(false)

onMounted( () => {
    fetchTravels();
    page.value = true
    
});
</script>
<template>
Людей:
<template v-if="users?.length == 0 || users?.length == null || users?.length == undefined">
    0
</template>
<template v-else>
    {{users?.length}}
</template>
<div class="search_title">
    <h1>Поиск друзей</h1>
</div>

<Search></Search>

<div class="travels_list">
    <!-- <span v-if="pending">Загрузка....</span>
     -->

     

<template v-if="pending">
    <div class="pulsar" style="margin: 20px 0px 0px 0px;">
        <div class="block pulsate" style="height: 170px;"></div>
    </div>
    <div class="pulsar" style="margin: 20px 0px 0px 0px;">
        <div class="block pulsate" style="height: 170px;"></div>
    </div>
    <div class="pulsar" style="margin: 20px 0px 0px 0px;">
        <div class="block pulsate" style="height: 170px;"></div>
    </div>
    <div class="pulsar" style="margin: 20px 0px 0px 0px;">
        <div class="block pulsate" style="height: 170px;"></div>
    </div>
</template>

    <NuxtLink :to="`/profile/${user.id}/`" v-for="user in users" :key="user.id" v-else>
        <div class="travel">
            <img :src="user?.photo" alt="" v-if="user?.photo && user?.photo?.length > 0">
            <img src="~/assets/img/photo.png" alt="" v-else>
            <div class="travel_cart_info">
                <h2>
                    <span v-for="country in travel?.country">{{ country?.name }},&nbsp;</span>
                </h2>
                <div class="travel_cart_user_info">
                    <h3 v-if="user?.first_name && user?.last_name">{{user?.first_name}} {{user?.last_name}}</h3>
                    <h3 v-else>ФИО не заполнено</h3>
                    <div class="user_cart_search">
                        <span>Возраст: {{user?.age}}</span>
                    </div>
                </div>
                <!-- <h1>{{travel.id}}</h1> -->
                <p v-if="user?.small_description">{{user?.small_description}}</p>
                <p v-else>Здесь будет статус</p>
                <span v-if="user?.city?.name" style="padding: 15px 15px 7.5px 15px;width: 100%;text-align: center;border-top: 1px solid #e7e7e7;margin: 15px 0px 0px 0px;font-weight: 700;font-size: 14px;">г. {{user?.city?.name}}</span>
                <span v-else style="padding: 15px 15px 7.5px 15px;width: 100%;text-align: center;border-top: 1px solid #e7e7e7;margin: 15px 0px 0px 0px;font-weight: 700;font-size: 14px;">Город не указан</span>
            </div>
        </div>
    </NuxtLink>

</div>
</template>
<style scoped>

.travels_list{
    display: flex;
    flex-wrap: wrap;
    flex: 1;
    gap: 0.79vw;
    margin: 25px 0px 0px 0px;

    && a{
        width: 24%;
        display: flex;
        min-width: 299px;
        min-height: 299px;
        margin: 0;
    }
}
.travel_cart_user_info{
    width: 100%;
    && h3{
        font-size: 15px;
        text-align: center;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        width: 100%;
    }
}

.user_cart_search{
    width: 100%;
    border-bottom: 1px solid #dddddd;
    margin: 10px 0px 10px 0px;
    padding: 0px 0px 10px 0px;
    line-height: 2;

    && span{
        border-radius: 115px;
        padding: 5px 15px 5px 15px;
        background-color: #128ce91e;
        font-weight: 700;
        font-size: 14px;
        color: #2963d6;
    }
}

.travel_cart_info{
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

/* travel */
.travel{
    display: flex;
    width: 100%;
    margin: 0px 0px 0px 0px;
    padding: 0px 0px 25px 0px;
    border-bottom: 1px solid #dddddd;
    align-items: center;
    transition: all 0.3s;
    -moz-transition: all 0.3s;
    -webkit-transition: all 0.3s;
    position: relative;
    top: 0;
    opacity: 9;
    background-color: #FFFFFF;
    padding: 35px 15px 15px 15px;
    border-radius: 15px;
    overflow: hidden;
    font-size: 15px;
    
    && img{
        width: auto;
        object-fit: cover;
        width: 135px;
        height: 135px;
        border-radius: 15px;
        margin: 0px 0px 0px 0px;
        max-width: 100px;
        max-height: 100px;
        min-width: 100px;
        min-height: 100px;
    }

    && h2{
        width: 100%;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
        margin: 0px 0px 10px 0px;
    }
}
/* travel */

.travel{
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}
.search_title{
    font-size: 5vw;
    margin: 0px 0px 25px 0px;

    && h1{
        font-size: clamp(25px, 4vw, 49px);
    }
}

.travels_list a{
    position: relative;
    transition: all 0.2s;
    -moz-transition: all 0.2s;
    -webkit-transition: all 0.2s;
    top: 0px;
}
.travels_list a:hover{
    position: relative;
    top: 2px;
    transition: all 0.2s;
    -moz-transition: all 0.2s;
    -webkit-transition: all 0.2s;
    opacity: 0.9;
}
.user_cart_search {
    display: flex;
    justify-content: center;
}

@media (max-width: 960px){
    .travels_list{

        && a{
            width: 49%;
        }
    }
}

@media (max-width: 700px){
    .travels_list{

        && a{
            width: 100%;
            margin: 15px 0px 0px 0px;
        }
    }
}
@media (max-width: 490px){
    .travel{
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;

        && img{
            max-width: 99px;
            max-height: 99px;
            margin: 0px 0px 15px;
            border-radius: 100%;
        }
    }
    .user_cart_search {
        text-align: center;
    }
    .travel_cart_user_info {
        text-align: center;
    }
    .travels_list{

        && a{
            width: 100%;
            margin: 15px 0px 0px 0px;
        }
    }
}
</style>