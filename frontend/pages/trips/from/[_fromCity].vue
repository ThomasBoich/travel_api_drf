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
const {data: trips, pending} = await useFetch(apiConfig.trips_filter, {
    method: 'POST',
    body: {
        from_city: fromCity,
        to_city: false
    }
})
</script>
<template>
Путешествия:
<template v-if="trips?.length == 0 || trips?.length == null || trips?.length == undefined">
    0
</template>
<template v-else>
    {{trips?.length}}
</template>

<div class="search_title">
    <h1>Из {{fromCity}}</h1>
</div>
<SearchTrips></SearchTrips>


<div class="travels_list">
    <span v-if="pending">Загрузка....</span>
    <template v-if="pending">
        <div class="pulsar" style="margin: 20px 0px 0px 0px;">
            <div class="block pulsate" style="height: 90px;"></div>
        </div>
        <div class="pulsar" style="margin: 20px 0px 0px 0px;">
            <div class="block pulsate" style="height: 90px;"></div>
        </div>
        <div class="pulsar" style="margin: 20px 0px 0px 0px;">
            <div class="block pulsate" style="height: 90px;"></div>
        </div>
        <div class="pulsar" style="margin: 20px 0px 0px 0px;">
            <div class="block pulsate" style="height: 90px;"></div>
        </div>
    </template>
    <TripCard :search_trip="trip" v-for="trip in trips"></TripCard>


</div>
</template>
<style scoped>

.trips_list{
    margin: 15px 0px 0px 0px;
}
.search-result {
    display: flex;
    width: 100%;
    margin: 0px 0px 25px 0px;
    padding: 0px 0px 25px 0px;
    border-bottom: 1px solid #dddddd;
    align-items: center;
    transition: all 0.3s;
    -moz-transition: all 0.3s;
    -webkit-transition: all 0.3s;
    position: relative;
    top: 0;
    opacity: 9;
}

.search_trip_one_layer {
    display: flex;
    flex-direction: row;
    width: 100%;
}
.trip_time_layer {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    column-gap: 32px;
    display: grid;
    grid-template-columns: repeat(2, calc(50% - 16px));
    justify-content: space-between;
    overflow: hidden;
    width: 69%;
    min-width: 300px;
    position: relative;
}


.trip_in_time, .trip_out_time {
    font-size: 25px;
    font-weight: 500;
    width: max-content;
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: flex-start;
    position: relative;
    background-color: #FFFFFF;
    z-index: 9;
    padding: 0px 9px 0px 9px;
}
.time__layer {
    display: flex;
    align-items: center;
    width: 100%;
    background-color: #FFFFFF;
    z-index: 9;
}

.trip_time_layer span {
    font-size: 12px;
    background-color: #00000015;
    border-radius: 15px;
    padding: 2px 5px 2px 5px;
    color: #000;
    font-weight: 700;
    margin: 0px 0px 0px 5px;
}

.trip_city {
    width: 100%;
    font-size: 15px;
    color: #00000079;
}
.trip_out_time {
    min-width: 100%;
}

.time__layer {
    display: flex;
    align-items: center;
    width: 100%;
    background-color: #FFFFFF;
    z-index: 9;
}
.trip_time_layer span {
    font-size: 12px;
    background-color: #00000015;
    border-radius: 15px;
    padding: 2px 5px 2px 5px;
    color: #000;
    font-weight: 700;
    margin: 0px 0px 0px 5px;
}

.search-result img {
    width: auto;
    object-fit: cover;
    width: 135px;
    height: 135px;
    border-radius: 15px;
    margin: 0px 15px 0px 0px;
}
.trip_driver_photo img {
    height: 49px ! IMPORTANT;
    width: 49px ! IMPORTANT;
    object-fit: cover ! IMPORTANT;
    border-radius: 101px ! IMPORTANT;
}

.trip_city {
    width: 100%;
    font-size: 15px;
    color: #00000079;
}
.search-result {
    background-color: #FFFFFF;
    padding: 15px 15px 15px 15px ! IMPORTANT;
    border-radius: 15px;
    margin: 0px 0px 15px 0px ! IMPORTANT;
}
.trip_info {
    width: 33%;
}
.trip_price {
    display: flex;
    flex-direction: column;
}

.trip_price span {
    font-size: 25px;
    font-weight: 700;
}

.trip_driver {
    display: flex;
    align-items: center;
    width: 33.333333%;
}
.trip_driver_info {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    font-weight: 500;
    font-size: 15px;
    width: 100%;
}
.trip_cart_user_info{
    && h3{
        font-size: 15px;
    }
}

.trip_driver_info span {
    color: #00000079;
}


.select_service img, svg {
    margin: 0px 5px 0px 0px;
    width: 25px;
    height: 25px;
    object-fit: cover;
}

.trip_time_layer line {
    stroke: rgba(11, 21, 36, .3);
    fill: none;
    stroke-width: 3px;
    stroke-opacity: .5;
    stroke-dasharray: 0, 7;
    stroke-dashoffset: 0;
    stroke-linecap: round;
}
.trip_time_layer svg {
    fill: none;
    height: 6px;
    padding: 0 12px;
    position: absolute;
    width: 100%;
    top: 12px;
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
/* travel */


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