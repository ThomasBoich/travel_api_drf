<template>
  <!-- <div></div> -->
  <form action="" method="post" @submit.prevent="filterTravels">
    <div ref="whatSearhLayout" class="what-search-layout">
    <div class="what-search-content">
      <span style="font-weight: 700;">Я ищу:</span> <span class="ff2" @click="OpenWhat()" style="color: #999999;
        margin: 0px 0px 0px 9px;font-size: 700!IMPORTANT;">{{ what }}</span> <span></span>
    </div>
    <div :class="addClass" class="what-navigation">
    <div class="ff" ref="ff">
    <select v-model="what" class="what-search">
    <!-- <option value="Я ищу" selected disabled>Я ищу</option> -->
    <option value="Мужчину">Мужчину</option>
    <option value="Женщину">Женщину</option>
    <option value="Семью">Семью</option>
    <option value="Не важно" selected>Не важно</option>
    </select>
    <p>Возраст</p>
    <div class="whatAge">
      <input type="text" placeholder="от"> <input type="text" placeholder="до">
    </div>
    <button ref="buttonSave" class="save" @click.prevent="saveWhat">Сохранить</button>
    </div>
    </div>
    </div>
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
      <div class="from_city_input" @click="activeListCityFrom">
        <template v-if="fromCity">
          {{fromCity}}
        </template>
        <template v-else>
          Откуда?
        </template>
        
      </div>
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
    
    <div class="goCountry">
      <div class="go_country_input" @click="activeListGoCounty">
        <template v-if="goCountry">
          {{goCountry}}
        </template>
        <template v-else>
          Куда?
        </template>
        </div>
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
function filterTravels() {
  if (!fromCity.value && (goCountry.value != false && goCountry.value != true)) {
    navigateTo({
      path: `/travels/in/${goCountry.value}`,
      query: { what: what.value } // Передаём значение what
    });
  } else if (!goCountry.value && (fromCity.value != false && fromCity.value != true)) {
    navigateTo({
      path: `/travels/from/${fromCity.value}`,
      query: { what: what.value } // Передаём значение what
    });
  } else if (!goCountry.value && !fromCity.value) {
    navigateTo({
      path: `/travels/`,
      query: { what: what.value } // Передаём значение what
    });
  } else {
    navigateTo({
      path: `/travels/${fromCity.value}/${goCountry.value}`,
      query: { what: what.value } // Передаём значение what
    });
  }
}

const countryLoad = ref(true)
const cityLoad = ref(true)
const fromCity = ref(false)
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
  searchQuery.value = '';
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

const goCountry = ref(false)
const searchCountry = ref('');
const countries = ref([]);
const activeCountry = ref(false)

function activeListGoCounty(){
  activeCountry.value = !activeCountry.value
  fetchCountries();
}

const filteredCountries = computed(() => {
     if (!countries.value) return []; // Возвращаем пустой массив, если countries не определен
     return countries.value.filter(country =>
       country.name.toLowerCase().includes(searchCountry.value.toLowerCase())
     );
   });


const selectCountry = (country) => {
  searchCountry.value = '';
  activeCountry.value = !activeCountry.value
  goCountry.value = country
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
     const { data, pending } = await useFetch(apiConfig.countries);
     console.log('Данные из API:', data.value); // Логирование данных
     countryLoad.value = pending.value; // Логирование статуса загрузки
     if (Array.isArray(data.value)) {
       countries.value = data.value; // Убедитесь, что это массив
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



const whatSearhLayout = ref()
const addClass = ref('')
const what = ref('Не важно')

function OpenWhat(){
  addClass.value = 'active'
}

const WhatNavigation = ref()


// function outsideClick(event){
//   const ff = document.querySelector('.ff')
//   const ff2 = document.querySelector('.ff2')
//   if (!ff.contains(event.target) && !ff2.contains(event.target)){
//     addClass.value = '';
//     console.log(ff)
//   }
// }

function saveWhat(event) {
  const buttonSave = document.querySelector('.save');
  if (buttonSave && buttonSave.contains(event.target)) {
    addClass.value = '';
    // console.log(buttonSave);
  }
}

onMounted(() => {
  // document.addEventListener('click', outsideClick);
})

const people = ['Мужчину', 'Женщину', 'Пару', 'Семью', 'Не важно']

// const selected = ref()
const query = ref('')

</script>

<style scoped>
form{
  width: 100%;
}
.goCountry{
  width: 100%;
  position: relative;
  display: flex;
  align-items: center;
}
.from_city{
  width: 100%;
  position: relative;
  display: flex;
}

.goCountry::before{
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

.ff{
  display: flex;
  flex-direction: column;
  width: 95%;
  height: max-content;
  margin: 0 auto;
}
.whatAge{
  display: flex;
  justify-content: space-between;
  width: 100%;
  height: max-content;
}.whatAge input{
  width: 47%;
  border: 1px solid #00000025;
  border-radius: 9px;
  padding: 9px 15px 9px 15px;
  font-weight: 500;
}
p{
  height: 25px!IMPORTANT;
  margin: 15px 0px 15px 0px!IMPORTANT;
  font-size: 17px!IMPORTANT;
  font-weight: 700;
}
.what-search-content{display: flex;justify-content: flex-start;align-items: center;}

.what-search-layout{display: flex;flex-direction: column;width: 100%;border-right: 1px solid #FFFFFF;position: relative;padding: 0px 0px 0px 25px;cursor: pointer;font-weight: 700;flex-direction: row;}

.what-navigation{position: absolute;
width: 350px;
height: max-content;
background-color: #FFFFFF;
border-radius: 15px;
padding: 25px 25px 25px 25px;
visibility: hidden;
z-index: 145;
top: 35px;
box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
border: 1px solid #00000025;
z-index: 147;
}
.what-navigation button{
  width: 100%;
  background-color: #000000;
  padding: 9px 15px 9px 15px;
  border-radius: 9px;
  color: #FFFFFF;
  margin: 15px 0px 0px 0px;
}
.active{
  visibility: visible;
}
.what-search {
  border-bottom: 1px solid #00000025;
  width: 100% !important;
  display: flex;
  box-shadow: none !important;
  padding: 9px 15px 9px 0px;
  font-size: 17px !important;
  outline: none;
  margin: 0px 0px 0px 0px;
  border-radius: 0px;
  -webkit-appearance: none;
  cursor: pointer;
}.what-search:hover select{
  opacity: 0.9;
}
.what-search label{
  color: white;
}
.what-search option{
  font-size: 15px!IMPORTANT;
  padding: 5px;
  margin: 15px 0px 0px 0px;
}
.what-search-layout::before{
    content: "asd";
    content: "💙";
    display: flex;
    align-items: center;
    position: relative;
    margin: 0px 9px 0px 0px;
  }

@media(max-width: 770px){
  .what-search-layout{
    width: calc(100% - 30px);
    padding: 15px 0px 15px 0px;
    border-bottom: 1px solid #00000025;
    border-right: none;
    display: flex;
    flex-direction: row;
  }
  .what-navigation{
    width: calc(100% + 39px);
    left: -19px;
    padding: 9px 9px 9px 9px;
    top: 47px;
  }
  .what-navigation p{
    text-align: left;
  }
}
.what-search{
  padding: 10px 10px  10px 10px;
  border-radius: 9px;
  border: 1px solid #00000025;
}
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
  .goCountry{
    padding: 0px 15px 0px 15px;
  }
}

</style>
