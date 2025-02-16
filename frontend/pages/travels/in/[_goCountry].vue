<script setup>
definePageMeta({
  layout: 'pages'
});
// Получаем объект маршрута
const route = useRoute();

// Извлекаем параметры из маршрута
const fromCity = route.params._fromCity; // Параметр из URL
const goCountry = route.params._goCountry; // Параметр из URL

import {API, apiConfig, base_url} from '@/api/api'
const {data: travels, pending} = await useFetch(apiConfig.travels_filter, {
    method: 'POST',
    body: {
        from_city: false,
        to_country: goCountry
    }
})
</script>
<template>
Путешествия:

<template v-if="travels?.length == 0 || travels?.length == null || travels?.length == undefined">
    0
</template>
<template v-else>
    {{travels?.length}}
</template>

<div class="search_title">
    <h1>В {{ goCountry }}</h1>
</div>

<Search></Search>

<div class="travels_list">
    <span v-if="pending">Загрузка....</span>
    <NuxtLink :to="`/travels/${travel.id}/`" v-for="travel in travels" :key="travel.id" v-else>
        <div class="travel">
            <img :src="`${base_url}${travel?.user?.photo}`" alt="">
            <div class="travel_cart_info">
                <h2>
                    <span v-for="country in travel?.country">{{ country?.name }},&nbsp;</span>
                </h2>
                <div class="travel_cart_user_info">
                    <h3>{{travel?.user?.first_name}} {{travel?.user?.last_name}} , Возраст: {{travel?.user?.age}}</h3>
                    <div class="user_cart_search">
                        <span>{{travel?.gender}} ищет {{travel?.gender_search}}</span> на {{travel?.days}} дней
                    </div>
                </div>
                <!-- <h1>{{travel.id}}</h1> -->
                <p>{{travel?.description}}</p>
            </div>
        </div>
    </NuxtLink>

</div>
</template>
<style scoped>
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
.travel_cart_user_info{
    && h3{
        font-size: 15px;
    }
}

.user_cart_search{
    width: 100%;
    border-bottom: 1px solid #dddddd;
    margin: 10px 0px 10px 0px;
    padding: 0px 0px 10px 0px;
    line-height: 2;

    && span{
        border-radius: 15px;
        padding: 5px 10px 5px 10px;
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
}

/* travel */
.travel{
    display: flex;
    width: 100%;
    margin: 25px 0px 0px 0px;
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
    padding: 15px 15px 15px 15px;
    border-radius: 15px;
    overflow: hidden;
    font-size: 15px;
    

    && img{
        width: auto;
        object-fit: cover;
        width: 135px;
        height: 135px;
        border-radius: 15px;
        margin: 0px 15px 0px 0px;
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


.search_title{
    font-size: 5vw;
    margin: 0px 0px 25px 0px;

    && h1{
        font-size: clamp(25px, 4vw, 49px);
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
}
</style>