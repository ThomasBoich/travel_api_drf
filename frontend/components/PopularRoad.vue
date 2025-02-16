<script setup>
const popularCity = ref([
  {
    id: 1,
    image: "./city.png",
    name: "Казань",
    info: "ФОоджыоваывоа ыв ава оыва оыждва оыджа оыа ывад ываы ыа ыаыаыв аыа",
  },
  {
    id: 2,
    image: "./city2.png",
    name: "Самара",
    info: "ФОоджыоваывоа ыв ава оыва оыждваоыа ывад ываы ыа ыаыаыв аыа",
  },
  {
    id: 3,
    image: "./city3.png",
    name: "Санкт-Петербург",
    info: "ФОоджыоваывоа ыв ава оыва оыждваоыа ывад ываы ыа ыаыаыв аыа",
  },
]);
const props = defineProps({
  popularCityCount: {
    type: Array,
    required: true,
  },
  countries_from_moscow: {
    type: Array,
    required: true,
  },
  travels_from_moscow:{
    type: Array,
    required: true,
  }
});

console.log(props.travels_from_moscow)
</script>
<template>
  <div
    class="index-pupular-roads-layer"
    data-aos="fade-up"
    data-aos-anchor-placement="center-bottom"
  >
    <div class="index-popular-roads-title">
      <h2>Популярные направления из Москвы</h2>
      <span>{{props.travels_from_moscow?.length}} шт.</span>
    </div>
    <div class="popular-roads">
      <div class="popular-road" v-for="travel in props.travels_from_moscow">
        <NuxtLink :to="`travels/Москва/${travel.country[0].name}`">
          <div class="popular-road-filter"></div>
          <div class="index-popular-city-info">          
            <span v-for="country in travel.country">{{ country.name }}</span>
            <p v-if="travel.description">{{ travel.description }}</p>
            <p v-else>Нет описания</p>
          </div>
          <img v-for="country in travel.country" :src="country.image" alt="" />
        </NuxtLink>
       
      </div>
    </div>
    <NuxtLink :to="`/travels/from/Москва`"><button class="other">Показать всех</button></NuxtLink>
  </div>
</template>
<style scoped>
.index-pupular-roads-layer {
  width: 100%;
  display: flex;
  flex-direction: column;
  margin: 75px 0px 0px 0px;
}
.index-popular-roads-title {
  display: flex;
  align-items: center;
  width: 100%;
  justify-content: flex-start;
  margin: 0px 0px 35px 0px;
}
.index-popular-roads-title h2 {
  font-size: 25px;
  font-weight: 700;
  margin: 0px 15px 0px 0px;
}
.index-popular-roads-title span {
  background-color: #f3f3f3;
  border-radius: 50px;
  padding: 5px 15px 5px 15px;
  color: #989898;
  min-width: max-content;
}
.popular-roads {
  display: flex;
  justify-content: space-between;
  margin: 0px 0px 50px 0px;
}
.popular-road {
  position: relative;
  border-radius: 9px;
  overflow: hidden;
  width: 32%;
  cursor: pointer;
  height: 325px;
}
.popular-road:hover {
  opacity: 0.9;
}
.popular-road img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.popular-road-filter {
  background-color: #00000025;
  width: 100%;
  height: 100%;
  position: absolute;
}
.index-popular-city-info {
  position: absolute;
  bottom: 25px;
  height: max-content;
  padding: 0px 0px 0px 25px;
  width: 100%;
}
.index-popular-city-info p {
  margin: 0;
  padding: 0;
  color: #ffffff;
  font-size: 15px;
  white-space: nowrap;
  text-overflow: ellipsis;
  width: 95%;
  overflow: hidden;
}
.index-popular-city-info span {
  font-size: 25px;
  color: #ffffff;
  font-weight: 700;
}
.other {
  border: 1px solid #e6e6e6;
  border-radius: 9px;
  font-size: 17px;
  text-align: center;
  width: 100%;
  padding: 15px 15px 15px 15px;
  transition: all 0.3s;
  -webkit-transition: all 0.3s;
  -moz-transition: all 0.3s;
}
.other:hover {
  background-color: #000000;
  color: #ffffff;
  border: 1px solid #000000;
  transition: all 0.3s;
  -webkit-transition: all 0.3s;
  -moz-transition: all 0.3s;
}

.index-friends-user a{
  display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    width: -moz-max-content;
    width: 100%;
}.index-friends-user img{
  width: 100%;
  height: 100%;
  object-fit: cover;
}
@media (max-width: 770px) {
  .index-popular-roads-title h2 {
    font-size: 4vw;
  }
  .index-pupular-roads-layer {
    width: calc(100% - 30px);
    margin: 45px auto 45px;
  }
  .index-popular-roads-title span {
    font-size: 15px;
  }
  .popular-roads {
    overflow: hidden;
    overflow-x: auto;
    margin: 0px 0px 35px 0px;
  }
  .popular-road {
    width: 250px;
    height: 250px;
    min-width: 250px;
    min-height: 250px;
    margin: 0px 15px 0px 0px;
  }
}
</style>
