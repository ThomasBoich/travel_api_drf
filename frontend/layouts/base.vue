<template>
  <div class="base-content">
  <div class="vertical-nav">
  <NuxtLink to="/me"><img src="~/assets/img/BMTH.png" />Талайн</NuxtLink>
  <NuxtLink to="/"><img src="~/assets/img/Search.png" />Поиск поездок</NuxtLink>
  <NuxtLink to="/chat"><img src="~/assets/img/Communication.png" />Сообщения <span>2</span> </NuxtLink>
  <!-- <NuxtLink><img src="~/assets/img/Commercial.png" />Мои объявления <span>15</span></NuxtLink> -->
  </div>
    <slot />
  </div>
  <Footer></Footer>
</template>

<script lang="ts" setup>

</script>

<style scoped>
.base-content{
  display: flex;
  justify-content: space-between;
  margin: 0 auto;  
  max-width: 1279px;
  width: calc(100% - 35px);
  padding: 15px 0px 15px 0px;
}
.vertical-nav{
  top: 0;
  position: sticky;
  position: -webkit-sticky;
  display: flex;
  flex-direction: column;
  min-width: 235px;
  margin: 9px 35px 0px 0px;
}
.vertical-nav a{
  display: inline-flex;
  align-items: center;
  margin: 0px 0px 15px 0px;
  font-size: 17px;
  font-weight: 700;
  cursor: pointer;
  color: #707070;
}.vertical-nav a:hover{opacity: 0.9;}
.vertical-nav a img{
  width: 25px;
  height: 25px;
  margin: 0px 9px 0px 0px;
}.vertical-nav a span{
  margin: 0px 0px 0px 5px;
  opacity: 0.5;
}
</style>