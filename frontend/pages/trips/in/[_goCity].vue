<template>
Путешествия:
<template v-if="trips?.length == 0 || trips?.length == null || trips?.length == undefined">
    0
</template>
<template v-else>
    {{trips?.length}}
</template>

<div class="search_title">
    <h1>В {{goCity}}</h1>
</div>
<SearchTrips></SearchTrips>
<div class="trips_list">
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
        from_city: false,
        to_city: goCity
    }
})
</script>
<style scoped>
.search_title{
    font-size: 5vw;
    margin: 0px 0px 25px 0px;

    && h1{
        font-size: clamp(25px, 4vw, 49px);
    }
}
</style>