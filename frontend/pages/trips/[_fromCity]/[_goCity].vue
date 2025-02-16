<script setup>
definePageMeta({
  layout: 'pages'
});
// Получаем объект маршрута
const route = useRoute();

// Извлекаем параметры из маршрута
const fromCity = route.params._fromCity; // Параметр из URL
const goCity = route.params._goCity; // Параметр из URL

import {API, apiConfig, base_url} from '@/api/api'
const {data: trips, pending} = await useFetch(apiConfig.trips_filter, {
    method: 'POST',
    body: {
        from_city: fromCity,
        to_city: goCity
    }
})
</script>
<template>
Поездки: 

<template v-if="trips?.length == 0 || trips?.length == null || trips?.length == undefined">
    0
</template>
<template v-else>
    {{trips?.length}}
</template>

<div class="search_title">
    <h1>{{fromCity}} — {{goCity}}</h1>
</div>

<SearchTrips></SearchTrips>

<div class="trips_list">
    <span v-if="pending">Загрузка....</span>
    <NuxtLink :to="`/trips/${trip.id}/`" v-for="trip in trips" :key="trip.id" v-else>
        <div class="trip">
            <img :src="`${base_url}${trip?.user?.photo}`" alt="">
            <div class="trip_cart_info">
                <div class="trip_cart_user_info">

                </div>
                <!-- <h1>{{travel.id}}</h1> -->
                <!-- <p>{{travel?.description}}</p> -->
            </div>
        </div>
    </NuxtLink>

</div>
</template>
<style scoped>

.trip_cart_user_info{
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

.trip_cart_info{
    width: 100%;
    display: flex;
    flex-direction: column;
}

/* trip */
.trip{
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
/* trip */


.search_title{
    font-size: 5vw;
    margin: 0px 0px 25px 0px;

    && h1{
        font-size: clamp(25px, 4vw, 49px);
    }
}

@media (max-width: 490px){
    .trip{
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
    .trip_cart_user_info {
        text-align: center;
    }
}
</style>