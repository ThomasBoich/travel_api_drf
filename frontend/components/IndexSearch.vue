<template>
  <div class="popular-countries">
    <div class="popular-countries-title">
      <h2>Популярные направления <span>{{ countries?.length }} шт.</span></h2>
      <!-- <button>Как найти надежного попутчика ></button> -->
    </div>

    <div
      class="popular-countries-layout"
      data-aos="fade-up"
      data-aos-anchor-placement="top-bottom"
    >


    <template v-if="!loaded">
      <div class="pulsar" style="margin: 0px 0px 0px 0px;min-width: 150px;">
        <div class="block pulsate" style="height: 79px;"></div>
      </div>
      <div class="pulsar" style="margin: 0px 0px 0px 0px;min-width: 150px;">
        <div class="block pulsate" style="height: 79px;"></div>
      </div>
      <div class="pulsar" style="margin: 0px 0px 0px 0px;min-width: 150px;">
        <div class="block pulsate" style="height: 79px;"></div>
      </div>
      <div class="pulsar" style="margin: 0px 0px 0px 0px;min-width: 150px;">
        <div class="block pulsate" style="height: 79px;"></div>
      </div>
      <div class="pulsar" style="margin: 0px 0px 0px 0px;min-width: 150px;">
        <div class="block pulsate" style="height: 79px;"></div>
      </div>
      <div class="pulsar" style="margin: 0px 0px 0px 0px;min-width: 150px;">
        <div class="block pulsate" style="height: 79px;"></div>
      </div>
      <div class="pulsar" style="margin: 0px 0px 0px 0px;min-width: 150px;">
        <div class="block pulsate" style="height: 79px;"></div>
      </div>
      <div class="pulsar" style="margin: 0px 0px 0px 0px;min-width: 150px;">
        <div class="block pulsate" style="height: 79px;"></div>
      </div>
      <div class="pulsar" style="margin: 0px 0px 0px 0px;min-width: 150px;">
        <div class="block pulsate" style="height: 79px;"></div>
      </div>
      <div class="pulsar" style="margin: 0px 0px 0px 0px;min-width: 150px;">
        <div class="block pulsate" style="height: 79px;"></div>
      </div>
      <div class="pulsar" style="margin: 0px 0px 0px 0px;min-width: 150px;">
        <div class="block pulsate" style="height: 79px;"></div>
      </div>
      <div class="pulsar" style="margin: 0px 0px 0px 0px;min-width: 150px;">
        <div class="block pulsate" style="height: 79px;"></div>
      </div>
    </template>


      <!-- <div
        v-for="country in countries"
        :key="country.id"
        class="popular-country"
        v-if="!loaded"
      >


      </div> -->

      <div
        v-for="country in limitedCountries"
        :key="country.id"
        class="popular-country"
        v-if="loaded"
      >
      <NuxtLink :to="`travels/in/${country?.name}`" style="width: 100%;display: flex;
    align-items: center;justify-content: flex-start;text-align: left;">
        <img :src="country?.image" alt="" />
        <div class="popular-country-info">
          <div class="popular-country-info-layer">
            <span>{{ country?.name }}</span>
            <p>Поездок: {{ country?.travel_count }}</p>
          </div>
        </div>
      </NuxtLink>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
const loaded = ref(false);
const handleImageLoad = () => {
  loaded.value = true;
};


import { apiConfig } from '@/api/api';

const {data: countries, error:countries_e, pending: countries_p} = useFetch(apiConfig.countries);

const limitedCountries = computed(() => {
  return countries.value ? countries.value.slice(0, 12) : [];
});

// const props = defineProps(['popular_countries', 'total_popular_countries', 'countries', 'limitedCountries'])



// const {data: countries, error, pending} = await useFetch('http://127.0.0.1:8000/api/countries/');

// const isLoading = ref(pending);

// const limitedCountries = computed(() => {
//   return countries.value ? countries.value.slice(0, 12) : [];
// });





onMounted(() => {

  const timeToMount = performance.now();
  // console.log("Время монтирования компонента:", timeToMount);

  setTimeout(() => {
    loaded.value = true;
  }, 0);

});
  // Измерение времени монтирования компонента
  // Установка loaded после завершения монтирования
// const countries = ref([
//   {
//     id: 1,
//     name: "Калининград",
//     countRoad: "1500 поездок",
//     url: "./country.png",
//   },
//   {
//     id: 2,
//     name: "Ростов-на-Дону",
//     countRoad: "1500 поездок",
//     url: "./country2.webp",
//   },
//   {
//     id: 3,
//     name: "Екатерингбург",
//     countRoad: "1500 поездок",
//     url: "./country3.webp",
//   },
//   {
//     id: 4,
//     name: "Ярославль",
//     countRoad: "1500 поездок",
//     url: "./country4.webp",
//   },
//   {
//     id: 5,
//     name: "Геленджик",
//     countRoad: "1500 поездок",
//     url: "./country5.webp",
//   },
//   {
//     id: 6,
//     name: "Краснодар",
//     countRoad: "1500 поездок",
//     url: "./country6.webp",
//   },
//   {
//     id: 7,
//     name: "Красная Поляна",
//     countRoad: "1500 поездок",
//     url: "./country7.webp",
//   },
//   {
//     id: 8,
//     name: "Новосибирск",
//     countRoad: "1500 поездок",
//     url: "./country7.webp",
//   },
//   { id: 9, name: "Воронеж", countRoad: "1500 поездок", url: "./country9.webp" },
//   { id: 10, name: "Самара", countRoad: "1500 поездок", url: "./country10.webp" },
//   { id: 11, name: "Тула", countRoad: "1500 поездок", url: "./country11.webp" },
//   {
//     id: 12,
//     name: "Кисловодск",
//     countRoad: "1500 поездок",
//     url: "./country12.webp",
//   },
// ]);
</script>

<style scoped>
.popular-countries {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
  margin-bottom: 20px;
  padding-bottom: 25px;
  flex-direction: column;
  margin: 75px 0px 50px 0px;
}
.popular-countries-title {
  width: calc(100% - 29px);
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 0px 0px 35px 0px;
}
.popular-countries-title h2 {
  font-size: 25px;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  margin: 0px 15px 0px px;
}
.popular-countries-title h2 span {
  font-size: 15px;
  background-color: #f3f3f3;
  padding: 5px 9px 5px 9px;
  border-radius: 25px;
  font-weight: 500;
  color: #989898;
  margin: 0px 0px 0px 15px;
  min-width: max-content;
}
.popular-countries-layout {
  width: 100%;
  min-width: 200px;
  display: grid;
  grid-template-columns: repeat(4, 1fr); /* 4 столбца */
  grid-template-rows: repeat(3, auto); /* 3 ряда */
  justify-content: space-between;
  align-items: center;
  gap: 35px;
  flex-shrink: 0;
  overflow: hidden;
  overflow-x: auto;
  padding: 0px 15px 25px 15px;
}
.popular-country {
  width: 22%;
  display: flex;
  height: 78px;
  align-items: center;
  min-width: 250px;
}
.popular-country img {
  min-width: 78px;
  min-height: 78px;
  border-radius: 9px;
  object-fit: cover;
  margin: 0px 15px 0px 0px;
  align-items: center;
  max-width: 78px;
  max-height: 78px;
}
.popular-country-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  display: block;
  width: 100%;
  min-width: 129px;
  max-width: 129px;
}
.popular-country-info p {
  margin: 0;
  padding: 0;
  font-size: 15px;
  color: #707070;
  text-align: left;
  width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.popular-country-info span {
  font-weight: 700;
  font-size: 19px;
  width: 100%;
  overflow: hidden;
  text-overflow:ellipsis;
  white-space: nowrap;
}

/* мобильная версия */
@media (max-width: 770px) {
  .popular-countries-title h2 {
    font-size: 4vw;
  }
  .popular-countries-title {
    flex-direction: column;
    justify-content: flex-start;
    text-align: left;
    align-items: flex-start;
    margin: 0px 0px 25px 0px;
  }.popular-countries-title button{
    font-size: 15px;
    color: #707070;
    display: none;
  }
  .popular-country-info span {
    font-size: 15px;
  }
  .popular-country {
    min-width: max-content;
  }
  .popular-countries-layout {
    gap: 15px;
  }
  .popular-countries {
    margin: 45px 0px 0px 0px;
  }
  .popular-countries-layout{
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: repeat(2, auto);
  }
}
</style>
