<script setup>
definePageMeta({
    layout: 'pages'
})

import { apiConfig, base_url } from '@/api/api';

const route = useRoute()
const travel_id = route.params.id
const {data: travel, pending} = await useFetch(apiConfig.travel, {
    method: 'POST',
    body: {
        travel_id: travel_id
    }
})
</script>
<template>
    <div class="travel_title">
        <h1>
            <div>Ищу попутчика:</div>
            <span style="padding: 10px 15px;border: 1px solid;border-radius: 49px;font-size: 17px;margin: 0px 15px 0px 0px;font-weight: 700;" v-if="travel?.country" v-for="country in travel?.country">{{country?.name}}</span>
            <!-- ,,  -->
        </h1> 
    </div>
    <div class="travel_information">
        <div class="travel_left">
        <div class="travel_user">
        <img v-if="travel?.user?.photo?.length > 0" :src="`${base_url}${travel?.user?.photo}`" alt="">
        <img v-else src="~/assets/img/photo.png" alt="">

        <div class="travel_user_info">
            <NuxtLink :to="`/profile/${travel?.user?.id}`"><h2>{{travel?.user?.first_name}} {{travel?.user?.last_name}}</h2></NuxtLink>
            <p>
                <span style="
                border-radius: 15px;
                padding: 5px 10px 5px 10px;
                background-color: #128ce91e;
                font-weight: 700;
                font-size: 14px;
                color: #2963d6;
                margin: 0px 15px 0px 0px;
                ">
                {{travel?.gender}} ищет {{travel?.gender_search}}</span>
                <span><img src="~/assets/img/pic_location_grey.png" alt="">{{travel?.user?.city.name}}</span>, 0 отзывов</p>
        </div>
    </div>

    <div class="travel_description">
        <h3>Цель поездки</h3>
        <p>{{travel?.description}}</p>
        
        <div class="travel_interests">
            <h3>Интересы</h3>
            <div class="travel_interests_list">
                <span v-for="interes in travel?.user?.interests">
                <img :src="`${base_url}${interes?.image}`" alt="">
                {{interes.name}}
                </span>
            </div>
        </div>
    </div>
    </div>
    <div class="travel_right">
        <div class="travel_ticket">
            <h4>Детали путешествия</h4>
            <ul>
                <li><span><div>Поиски:</div></span> {{ travel?.gender }} ищет {{travel?.gender_search}}</li>
                <li><span><div>Начало: путешествия</div></span> {{travel?.date}}</li>
                <li><span><div>Срок путешествия:</div></span> {{travel?.days}} дней</li>
                <li><span><div>Уже путешествует:</div></span> <template v-if="travel?.travel_now">Да</template><template v-else>Нет</template></li>
            </ul>
            <button>Путешевствовать вместе</button>
        </div>
    </div>
    </div>


</template>
<style scoped>


.travel_ticket{
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
.travel_information{
    display: flex;
    justify-content: space-between;
}

.travel_right{
    width: 100%;
    max-width: 379px;
    margin: 0px 0px 0px 15px;
}
.travel_left{
    width: 100%;
}
.travel_interests_list{
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
.travel_interests{
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
.travel_description{
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

.travel_title{
    margin: 0px 0px 25px 0px;

    && h1{
        font-size: clamp(24px, 4vw, 40px);
    }
}

.travel_user{
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

.travel_user_info{
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

@media (max-width: 960px){
    .travel_right{
        margin: 15px 0px 0px 0px;
        max-width: 100%;
    }
    .travel_information{
        flex-direction: column;
    }
}
</style>