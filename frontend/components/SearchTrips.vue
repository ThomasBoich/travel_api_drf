<template>
  <!-- <div></div> -->
  <form action="" method="post" @submit.prevent="filterTrips">
    <!-- <ButtonsWhatSearch></ButtonsWhatSearch> -->
    <!-- <UInput
      size="sm"
      placeholder="Откуда едем?"
      class="is"
      style="
        border: none;
        box-shadow: none;
        font-size: 17px;
        padding: 0px 0px 0px 25px;
        color: #676767;
      "
    /> -->

    <!-- <ButtonsTheWhereSearch></ButtonsTheWhereSearch> -->
    <!-- <USelectMenu
      class="where"
      v-model="selected"
      :loading="loading"
      :searchable="search"
      placeholder="Куда?"
      option-attribute="name"
      multiple
      trailing
      by="id"
      style="
        border: none;
        box-shadow: none;
        font-size: 17px;
        padding: 0px 0px 0px 0px;
        width: 100%!IMPORTANT;
      "
    /> -->
    
    <div class="from_city">
      <div class="from_city_input" @click="activeListCityFrom">{{fromCity}}</div>
      <!-- <input
       class="from_city_input"
       type="text"
       placeholder="Откуда?"
       @click="activeListCityFrom"
      />  -->
      <div class="from_city_list" :class="{'active': activeCity}">
        <input type="text" placeholder="Название города" @input="updateFilteredCities" v-model="searchQuery">
        <span v-if="cityLoad">Загрузка....</span>
        <span v-else
         v-for="city in filteredCities" :key="city"
         @click="selectCity(city.name)">🌐 {{ city.name }}</span>
         <span v-if="!filteredCities.length">Ничего не найдено</span>
      </div>
    </div>

    
    <div class="goCity">
      <div class="go_country_input" @click="activeListGoCounty">{{goCity}}</div>
      <div class="from_country_list" :class="{'active': activeCountry}">
        <input type="text" placeholder="Название города" @input="updateFilteredCountries" v-model="searchCountry">
        <span v-if="countryLoad">Загрузка....</span>
        <span v-if="!countryLoad"
         v-for="country in filteredCountries" :key="country"
         @click="selectCountry(country.name)">🌐 {{ country.name }}</span>
         <span v-if="!filteredCountries.length">Ничего не найдено</span>
      </div>
    </div>    
    <Button class="search" label="Найти" severity="contrast" rounded>Найти</Button>

    <!-- {{selected}} -->
  </form>
</template>

<script lang="ts" setup>
import { API, apiConfig } from "@/api/api";


function filterTrips(){
  navigateTo(`/trips/${fromCity.value}/${goCity.value}`)
}


const countryLoad = ref(true)
const cityLoad = ref(true)

const fromCity = ref('Откуда?')
const searchQuery = ref('');
const cities = ref([]);
const activeCity = ref(false)

function activeListCityFrom(){
  activeCity.value = !activeCity.value;
  fetchCities();
}

const filteredCities = computed(() => {
     if (!cities.value) return []; // Возвращаем пустой массив, если countries не определен
     return cities.value.filter(city =>
       city.name.toLowerCase().includes(searchQuery.value.toLowerCase())
     );
   });

const selectCity = (city) => {
  searchQuery.value = city;
  activeCity.value = !activeCity.value
  fromCity.value = city
};

// Метод для обновления списка городов, если это необходимо
const updateFilteredCities = () => {
  // В данном случае метод просто обновляет filteredCities
  // Это можно использовать для других действий, если необходимо
};


onMounted(()=>{
  document.addEventListener('click', (e)=>{
    if(!e.target.closest('.from_city')){
      activeCity.value = false
    }
  })
})


const goCity = ref('Куда?')
const searchCountry = ref('');
const go_countries = ref([]);
const activeCountry = ref(false)

function activeListGoCounty(){
  activeCountry.value = !activeCountry.value
  fetchCountries();
}

const filteredCountries = computed(() => {
     if (!go_countries.value) return []; // Возвращаем пустой массив, если countries не определен
     return go_countries.value.filter(city =>
       city.name.toLowerCase().includes(searchCountry.value.toLowerCase())
     );
   });


const selectCountry = (city) => {
  searchCountry.value = city;
  activeCountry.value = !activeCountry.value
  goCity.value = city
};


const fetchCities = async () => {
     const { data, pending } = await useFetch(apiConfig.cities);
     console.log('Данные из API:', data.value); // Логирование данных
     cityLoad.value = pending.value; // Логирование статуса загрузки
     if (Array.isArray(data.value)) {
       cities.value = data.value; // Убедитесь, что это массив
     } else {
       console.error('Полученные данные не являются массивом:', data.value);
       cities.value = []; // Или обработайте ошибку по-другому
     }
     cityLoad.value = false
   };

const fetchCountries = async () => {
     const { data, pending } = await useFetch(apiConfig.cities);
     console.log('Данные из API:', data.value); // Логирование данных
     countryLoad.value = pending.value; // Логирование статуса загрузки
     if (Array.isArray(data.value)) {
       go_countries.value = data.value; // Убедитесь, что это массив
     } else {
       console.error('Полученные данные не являются массивом:', data.value);
       countries.value = []; // Или обработайте ошибку по-другому
     }
     countryLoad.value = false
   };
   
onMounted(() => {
 
})



const updateFilteredCountries = () => {
  
}



// function selectCity(city: string){
//   fromCity.value = city


const loading = ref(false);
const selected = ref([]);

async function search(q: string) {
  loading.value = true;

  const countries: any[] = await $fetch<any[]>(`${API}countries`, {
    params: { q },
  });

  loading.value = false;

  return countries;
}

</script>

<style scoped>
form{
  width: 100%;
}
.goCity{
  width: 100%;
  position: relative;
  display: flex;
  align-items: center;
}
.from_city{
  width: 100%;
  position: relative;
  display: flex;
  padding: 0px 0px 0px 15px;
}

.goCity::before{
  content: "✈️";
  display: flex;
  align-items: center;
  position: relative;
  margin: 0px 9px 0px 0px;
}

.from_city::before{
  content: "✈️";
  display: flex;
  align-items: center;
  position: relative;
  margin: 0px 9px 0px 0px;
}

.go_country_input{
  height: 50px;
  padding: 0px 0px 0px 0px;
  border: none;
  font-size: 17px;
  font-weight: 700;
  outline: none;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 100%;
  white-space: nowrap;
  display: flex;
  align-items: center;
  cursor: pointer;
}

.from_city_list{
  position: absolute;
  background-color: #FFFFFF;
  padding: 15px 15px 7px 15px;
  border: 1px solid #d9d9d9;
  display: flex;
  flex-direction: column;
  width: 100%;
  border-radius: 15px;
  overflow: hidden;
  overflow-y: auto;
  max-height: 400px;
  display: none;
  top: 49px;
  z-index: 9999;
  left: 0;
  right: 0;
}

.from_city_list.active{
  display: flex;
}

.from_country_list{
  position: absolute;
  background-color: #FFFFFF;
  padding: 15px 15px 7px 15px;
  border: 1px solid #d9d9d9;
  display: flex;
  flex-direction: column;
  width: 100%;
  border-radius: 15px;
  overflow: hidden;
  overflow-y: auto;
  max-height: 400px;
  display: none;
  top: 49px;
  z-index: 9999;
  left: 0;
  right: 0;
}
.from_country_list.active{
  display: flex;
}

.from_city_list span{
  cursor: pointer;
  margin: 0px 0px 0px 0px;
  padding: 10px 13px 10px 13px;
  color: #595959;
  font-size: 17px;
  border-radius: 15px;
  align-items: center;
  display: flex;
}
.from_country_list span{
  cursor: pointer;
  margin: 0px 0px 0px 0px;
  padding: 10px 13px 10px 13px;
  color: #595959;
  font-size: 17px;
  border-radius: 15px;
  align-items: center;
  display: flex;
}
.from_country_list span:hover{
  color: #151515;
  background-color: #f2f2f2;
}
.from_city_list span:hover{
  color: #151515;
  background-color: #f2f2f2;
}
.from_city_list input{
  padding: 7px 15px 7px 15px;
  font-size: 17px;
  border-radius: 15px;
  border-color: #cecece;
  border: solid 2px #f0f0f0d9;
  background-color: #f0f0f0d9;
  outline: 2px solid #efefefd9;
  margin: 0px 0px 7px 0px;
}
.from_country_list input{
  padding: 7px 15px 7px 15px;
  font-size: 17px;
  border-radius: 15px;
  border-color: #cecece;
  border: solid 2px #f0f0f0d9;
  background-color: #f0f0f0d9;
  outline: 2px solid #efefefd9;
  margin: 0px 0px 7px 0px;
}
.from_city_input{
  height: 50px;
  padding: 0px 0px 0px 0px;
  border: none;
  font-size: 17px;
  font-weight: 700;
  outline: none;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 100%;
  white-space: nowrap;
  display: flex;
  align-items: center;
  cursor: pointer;
}.from_city_input:hover{opacity: 0.9;}

.from_country_input{
  height: 50px;
  padding: 0px 15px 0px 15px;
  border: none;
  font-size: 17px;
  font-weight: 700;
  outline: none;
  overflow: hidden;
  text-overflow: ellipsis;
  width: 100%;
  white-space: nowrap;
  display: flex;
  align-items: center;
  cursor: pointer;
}.from_country_input:hover{opacity: 0.9;}
@media (max-width: 770px){
  form{
    display: flex;
    flex-direction: column;
    border-radius: 9px;
    width: calc(100% - 29px);
    width: 100%;
  }.search{
    width: calc(100% - 30px);
    border-radius: 9px;
    padding: 9px 5px 9px 5px;
    margin: 0px 0px 15px 0px;
    font-size: 17px;
  }
  .where{
    width: 100%;
    padding: 15px 0px 15px 15px!IMPORTANT;
    margin: 0px 0px 0px 0px!IMPORTANT;
    display: inline-flex;
    height: 55px;
  }
  .from_city{
    padding: 0px 0px 0px 15px;
  }
  .goCity{
    padding: 0px 15px 0px 15px;
  }
}

</style>
