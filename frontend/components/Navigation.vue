<template>
  <div class="navigation">
    <div class="navigantion-layer">
      <div class="logo">
        <!-- <NuxtLink to="/">Trave<span>lo</span></NuxtLink> -->
        <NuxtLink to="/"><img src="~/assets/img/kudaugodno_logo.png" alt=""></NuxtLink>
      </div>
      <div class="index_navigation" v-if="props.isNavigate">
        <NuxtLink to="/travels/" active-class="active-link">
          

          <!-- style="color: #FFFFFF;background-color: #004ee7;" -->
          <svg width="24" height="24" fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" focusable="false"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.34388 3.71925C6.21098 2.43331 8.40417 1.70258 10.6694 1.61169C12.9347 1.5208 15.1794 2.07347 17.1435 3.20569C19.1077 4.33792 20.7109 6.00337 21.7675 8.00918C22.8241 10.015 23.2909 12.2791 23.1139 14.5393C23.108 14.6546 23.0785 14.7839 23.0722 14.8048C22.5513 15.7519 18.3542 14.2632 13.477 11.5374L10.9179 16.0009H8.5974L11.7554 10.5392C7.00747 7.68232 3.68538 4.78324 4.19388 3.87925C4.23475 3.81804 4.28543 3.76398 4.34388 3.71925ZM13.5039 9.52925C14.9432 10.3723 16.4289 11.1335 17.9539 11.8093C18.8239 8.50925 18.4839 5.29925 16.5739 4.19925C14.6639 3.09925 11.7139 4.40925 9.29388 6.80925C10.6485 7.78913 12.0538 8.69706 13.5039 9.52925ZM22.84 6.88894C22.8382 6.91557 22.8382 6.9423 22.84 6.96894C22.8418 6.9423 22.8418 6.91557 22.84 6.88894ZM5 12.9989L8 16.9989H17C17.5304 16.9989 18.0391 17.2097 18.4142 17.5847C18.7893 17.9598 19 18.4685 19 18.9989V21.9989H17L15 19.9989H6L4 21.9989H2L4 18.6289L0 12.9989H5Z" fill="currentColor"></path></svg>
          Путешествия</NuxtLink>
        <NuxtLink to="/trips/" active-class="active-link">
          <svg width="24" height="24" fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" focusable="false"><path fill-rule="evenodd" clip-rule="evenodd" d="M15.5627 4.31989C16.2489 4.44411 16.929 4.60428 17.6 4.8C18.0063 4.92779 18.3613 5.18197 18.6131 5.52552C18.8649 5.86907 19.0005 6.28404 19 6.71V11C19 11 19 13 16 13H8C5.01625 13 5.00009 11.0216 5 11.0002V6.71C4.99955 6.28404 5.1351 5.86907 5.38692 5.52552C5.63874 5.18197 5.99367 4.92779 6.4 4.8C7.07103 4.60428 7.75107 4.44411 8.43726 4.31989L8.54 4.63C8.67246 5.02911 8.92735 5.37631 9.26845 5.62226C9.60954 5.86821 10.0195 6.00038 10.44 6H13.56C13.9805 6.00038 14.3905 5.86821 14.7316 5.62226C15.0726 5.37631 15.3275 5.02911 15.46 4.63L15.5627 4.31989ZM12 2C9.91535 2 7.84127 2.2963 5.84 2.88C5.01823 3.12901 4.29841 3.63586 3.78696 4.32559C3.27551 5.01533 2.99959 5.85133 3 6.71V22H6.94L7.94 20H16.08L17.08 22H21V6.71C21.0004 5.85133 20.7245 5.01533 20.213 4.32559C19.7016 3.63586 18.9818 3.12901 18.16 2.88C16.1587 2.2963 14.0847 2 12 2ZM5 15V17H9C9 16.4696 8.78929 15.9609 8.41422 15.5858C8.03914 15.2107 7.53043 15 7 15H5ZM19 17V15H17C16.4696 15 15.9609 15.2107 15.5858 15.5858C15.2107 15.9609 15 16.4696 15 17H19Z" fill="currentColor"></path></svg>
          Поездки</NuxtLink>        
        <NuxtLink to="" active-class="active-link">
          <svg width="24" height="24" fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" focusable="false"><path fill-rule="evenodd" clip-rule="evenodd" d="M20.9999 1.62029C21.7399 1.39029 22.3099 1.36029 22.4999 1.55029C22.6899 1.74029 22.6599 2.31028 22.4299 3.05028C21.9369 4.55211 21.1055 5.92062 19.9999 7.05026L17.9999 9.05025L18.9999 22.0502L17.9999 23.0502L13.6231 13.4211C12.8067 14.205 11.9296 14.9237 10.9999 15.5702C10.4417 16.0016 9.85336 16.3898 9.24026 16.7323L9.99995 22.0502L8.99995 23.0502L5.99997 18.0502L0.999995 15.0502L1.99999 14.0502L7.32418 14.8108C7.66569 14.1982 8.05177 13.6096 8.47996 13.0502C9.22994 11.978 10.0732 10.9741 10.9999 10.0502L16.9999 4.05027C18.1296 2.94464 19.4981 2.11326 20.9999 1.62029ZM1.99999 5.05027L0.999995 6.05027L9.38995 9.86025C10.5479 8.44318 11.8187 7.1222 13.1899 5.91027L1.99999 5.05027Z" fill="currentColor"></path></svg>
          Авиабилеты</NuxtLink>
        <NuxtLink to="" active-class="active-link">
          <svg width="24" height="24" fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" focusable="false"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.00008 9.23198C3.47053 9.5043 3.01191 9.90225 2.66654 10.3947C2.20436 11.0536 1.97032 11.8457 2.00008 12.65V22H5.00008L6.00008 20H18.0001L19.0001 22H22.0001V12.65C22.0299 11.8457 21.7958 11.0536 21.3336 10.3947C20.9883 9.90225 20.5296 9.5043 20.0001 9.23198V6.5C20.0001 5.10218 20.0001 4.40326 19.7717 3.85195C19.4672 3.11687 18.8832 2.53284 18.1481 2.22836C17.5968 2 16.8979 2 15.5001 2H8.50008C7.10226 2 6.40335 2 5.85203 2.22836C5.11695 2.53284 4.53293 3.11687 4.22845 3.85195C4.00008 4.40326 4.00008 5.10217 4.00008 6.5V9.23198ZM16.5001 8.3357C13.5211 7.83464 10.479 7.83464 7.50008 8.3357V5.76C7.49813 5.66512 7.51578 5.57086 7.55191 5.48311C7.58804 5.39535 7.64189 5.316 7.71008 5.25C7.84572 5.1229 8.02421 5.0515 8.21008 5.05H8.36008C9.55768 5.30762 10.7758 5.45821 12.0001 5.5C13.2241 5.4615 14.4422 5.31425 15.6401 5.06H15.7901C15.976 5.0615 16.1545 5.1329 16.2901 5.26C16.3583 5.326 16.4121 5.40535 16.4483 5.4931C16.4844 5.58086 16.502 5.67512 16.5001 5.77V8.3357ZM4.00008 12.65V14H20.0001V12.65C20.0095 12.2924 19.9064 11.9408 19.7055 11.6448C19.5046 11.3488 19.2159 11.1233 18.8801 11C14.3827 9.71982 9.61742 9.71982 5.12008 11C4.78426 11.1233 4.49557 11.3488 4.29466 11.6448C4.09374 11.9408 3.99071 12.2924 4.00008 12.65Z" fill="currentColor"></path></svg>
          Отели</NuxtLink>
        <NuxtLink to="" active-class="active-link">
          <svg width="24px" height="24px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fill-rule="evenodd" clip-rule="evenodd" d="M11.993 5.09691C11.0387 4.25883 9.78328 3.75 8.40796 3.75C5.42122 3.75 3 6.1497 3 9.10988C3 10.473 3.50639 11.7242 4.35199 12.67L12 20.25L19.4216 12.8944L19.641 12.6631C20.4866 11.7172 21 10.473 21 9.10988C21 6.1497 18.5788 3.75 15.592 3.75C14.2167 3.75 12.9613 4.25883 12.007 5.09692L12 5.08998L11.993 5.09691ZM12 7.09938L12.0549 7.14755L12.9079 6.30208L12.9968 6.22399C13.6868 5.61806 14.5932 5.25 15.592 5.25C17.763 5.25 19.5 6.99073 19.5 9.10988C19.5 10.0813 19.1385 10.9674 18.5363 11.6481L18.3492 11.8453L12 18.1381L5.44274 11.6391C4.85393 10.9658 4.5 10.0809 4.5 9.10988C4.5 6.99073 6.23699 5.25 8.40796 5.25C9.40675 5.25 10.3132 5.61806 11.0032 6.22398L11.0921 6.30203L11.9452 7.14752L12 7.09938Z" fill="currentColor"></path> </g></svg>
          Избранное</NuxtLink>
      </div>
      <div class="auth-user" v-if="isAuthenticated">
        <!-- <addContent></addContent> -->
        <div class="no-login">

          <!-- <span class="create-button" v-if="isAuthenticated" >+ Создать</span> -->
          <div class="user-nav">

            <template v-if="loadUser">
              <div class="pulsar" style="height: max-content;width: 35px;overflow: hidden;border-radius: 115px;margin: 0px 0px 0px 25px;">
                  <div class="block pulsate" style="height: 35px;width: 35px;"></div>
              </div>
            </template>
            <template v-else>
              <img id="user_nav" class="user_nav premium" :src="`${base_url}` + user?.photo || `~/assets/img/user.png`" alt="" v-if="isAuthenticated" @click="OpenMenu">
            </template>
                  
            <div class="user-nav-layer " :class="{'active': isOpen}">
              <!-- <NuxtLink to="/profile/1/">Моя страница</NuxtLink> -->
              <!-- <NuxtLink to="">Сообщения</NuxtLink> -->
              <NuxtLink to="/travels/">Поиск путешествий</NuxtLink>
              <NuxtLink to="/trips/">Поиск поездок</NuxtLink>
              <!-- <NuxtLink to="/chats/">Чат</NuxtLink> -->
              <NuxtLink to="/settings">Настройки</NuxtLink>
              <NuxtLink to="/tarifs/">Премиум 💎</NuxtLink>
              <!-- <NuxtLink to="/logout/" @click="logout">Выход</NuxtLink> -->
              <span @click="logout">Выход</span>
            </div>
          </div>

        </div>


      </div>

      <NuxtLink to="/login" v-if="!isAuthenticated">
        <Button
          class="login"
          label="Войти"
          severity="contrast"
          rounded>Войти</Button>
      </NuxtLink>

    </div>
  </div>
  <UModal v-model="isOpenSS" prevent-close style="z-index: 1150">
    <UCard :ui="{ ring: '', divide: 'divide-y divide-gray-100 dark:divide-gray-800' }">
      <template #header>
          <!-- <h3 class="text-base font-semibold leading-6 text-gray-900 dark:text-white">
            Modal
          </h3> -->
          <UButton
            color="gray"
            variant="ghost"
            icon="i-heroicons-x-mark-20-solid"
            class="-my-1"
            @click="isOpen = false"
          />
        <div class="flex items-center justify-between" style="height: 75dvh;">
          <div class="text-layout">
          <img src="~/assets/img/planet.png" alt="" style="max-width:49px;max-height: auto;position: relative;left: -5px;margin: 0px 0px 15px 0px;">
          <span>
          Войдите в систему,
          чтобы открыть все возможности
          Trave<span style="color:#4dd8cf;">lo</span>.
          </span>
          <form method="post" action="" @submit.prevent="" style="box-shadow: none;border:none;">
            <input type="text" placeholder="Электронная почта">
            <input type="password" placeholder="Пароль">
            <button>Войти</button>
          </form>
         <NuxtLink>Нет аккаунта? <span>Зарегистрироваться</span></NuxtLink>
         <div class="copy">
          Продолжай, Вы соглашайтесь с <span>Условиями использования</span> и <span>Политикой конфиденциальности</span>, а так же с <span>Политикой использования файлов cookie</span>.
         </div>
          </div>
        </div>
      </template>

      <Placeholder class="h-32" />
    </UCard>
  </UModal>
</template>

<script lang="ts" setup>
import { useAuthStore } from '@/stores/auth';
import { useAuth } from '@/composables/auth';


import { base_url } from '@/api/api';

const {logout} = useAuth();

const {user, isAuthenticated, loadUser} = storeToRefs(useAuthStore());
const isOpen = ref(false);
const isOpenSS = ref(false);

function OpenMenu(){
  isOpen.value = !isOpen.value;
}

const props = defineProps({
  isNavigate: {
    type: Boolean,
    default: false
  }
})

</script>
<style scoped>
.user-nav-layer{}

.user-nav {
    position: relative;
}
.user-nav img.premium {
    height: 35px;
    width: 35px;
    object-fit: cover;
    margin: 0px 0px 0px 25px;
    border-radius: 49px;
    cursor: pointer;
    opacity: 9;
    -webkit-transition: opacity 0.3s;
    -moz-transition: opacity 0.3s;
    transition: opacity 0.3s;
    outline: 4px solid #7e52c7;
    outline: 4px solid #2963d6;
}.user-nav img:active {
    outline: 2px inset #4dd8cf;
}
.user-nav img:hover {
    opacity: 0.9;
    -webkit-transition: opacity 0.3s;
    -moz-transition: opacity 0.3s;
    transition: opacity 0.3s;
}
.user-nav-layer.active {
    visibility: visible;
    transition: opacity 0.3s;
    opacity: 9;
    -webkit-transition: opacity 0.3s;
    -moz-transition: opacity 0.3s;
}
.user-nav-layer {
    visibility: hidden;
    position: absolute;
    min-width: max-content;
    right: 0;
    background-color: #FFFFFF;
    border-radius: 15px;
    padding: 2px 2px;
    border: 1px solid #00000009;
    display: flex;
    flex-direction: column;
    width: 215px;
    max-width: 250px;
    overflow: hidden;
    box-shadow: 0px 0px 6px 5px #00000009;
    opacity: 0;
    transition: opacity 0.3s;
    -moz-transition: opacity 0.3s;
    -webkit-transition: opacity 0.3s;
}
.navigantion-layer a {
    margin: 0px 0px 0px 0px;
}
.user-nav-layer a {
    width: 100%;
    margin: 0px 0px 0px 0px;
    font-size: 15px;
    font-weight: 500;
    background-color: #FFFFFF;
    padding: 15px 25px;
    transition: background-color 0.3s;
    -moz-transition: background-color 0.3s;
    -webkit-transition: background-color 0.3s;
}
.user-nav-layer a:hover{
  background-color: #f7f7f7;
}
.user-nav img {
    height: 35px;
    width: 35px;
    object-fit: cover;
    margin: 0px 0px 0px 25px;
    border-radius: 49px;
    cursor: pointer;
    opacity: 9;
    -webkit-transition: opacity 0.3s;
    -moz-transition: opacity 0.3s;
    transition: opacity 0.3s;
    outline: 2px solid #00000025;
}
.user_nav{
  object-fit: cover;
  width: 49px;
  height: 49px;
  border-radius: 115px;
  cursor: pointer;
}
.text-layout{
  font-weight: 900;
  font-size: 25px;
  width: 100%;
  padding: 2vw;
  display: inline-flex;
  flex-direction: column;
}.text-layout .copy{
  font-size: 13px;
  text-align: center;
  font-weight: 700;
  margin: 25px 0px 0px 0px;
  color: #b5b5b5;
}
.text-layout a{
  font-size: 17px;
  text-align: center;
  font-weight: 700;
}.text-layout a span{
  color: #4ac9c0;
}.text-layout a span{cursor: pointer;}
.text-layout a span:hover{
  color: #54e9df;
}
.text-layout button{
  font-size: 17px;
  font-weight: 700;
  background-color: #4dd8cf;
  padding: 15px;
  border-radius: 50px;
  margin: 0px 0px 25px 0px;
  width: 100%;
}.text-layout button:hover{
  background-color: #54e9df;
}.text-layout button:focus{
  background-color: #4ac9c0;
}

.text-layout form{
  display: flex;
  flex-direction: column;
  margin: 25px 0px 0px 0px;
}

.text-layout input{
  font-size: 17px;
  font-weight: 700;
  border: 1px solid #000000;
  width: 100%;
  padding: 15px 15px 15px 25px;
  margin: 0px 0px 15px 0px;
  border-radius: 50px;
}
.navigation {
  width: calc(100%);
  position: sticky;
  top: 0;
  display: flex;
  padding: 15px 15px 15px 15px;
  padding: 15px 0px 15px 0px;
  background-color: #ffffff;
  border-bottom: 1px solid #e8e8e8;
  z-index: 999;

  
}
.navigantion-layer {
  max-width: 1279px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: calc(100% - 29px);
}
.login {
  margin: 0px 0px 0px 25px;
  padding: 9px 19px 9px 19px;
  background-color: #000000;
  color: #ffffff;
  border-radius: 50px;
  font-size: 17px;
}

.no-login {
  display: flex;
  align-items: center;
}
.logo {
  font-size: 25px;
  font-weight: 900;
  color: #000000;
}
.logo a {
  color: #000000;
}
.logo span {
  color: #4dd8cf;
}
.no-login .create-button {
  border-right: 1px solid #d6d6d6;
  padding: 0px 25px 0px 0px;
  font-weight: 500;
  font-size: 17px;
  cursor: pointer;
}
.no-login .create-button:hover {
  opacity: 0.9;
}

.index_navigation {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0 auto;
    width: max-content;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0 auto;
    width: -moz-max-content;
    width: max-content;
    background-color: #e3ecf4;
    background-color: #f2f3f4;
    border-radius: 29px;
    padding: 0;
    width: 100%;
    max-width: max-content;
}

.index_navigation a {
    margin: 0px 0px 0px 0px;
    text-align: center;
    padding: 10px 20px 10px 20px;
    border-radius: 29px;
    font-size: 14px;
    font-weight: 700;
    color: #15151579;
    align-items: center;
    display: flex;
    transition: all 0.5s;

    && svg{
      width: 19px;
      height: 19px;
      margin: 0px 10px 0px 0px;
      padding: 0px 0px 0px 0px;
    }
}



.user-nav-layer span {
    width: 100%;
    margin: 0px 0px 0px 0px;
    font-size: 15px;
    font-weight: 500;
    background-color: #FFFFFF;
    padding: 15px 25px;
    transition: background-color 0.3s;
    -moz-transition: background-color 0.3s;
    -webkit-transition: background-color 0.3s;
    cursor: pointer;
}.user-nav-layer span:hover{
  background-color: #f7f7f7;
}

.index_navigation a:hover{
  color: #000000;
  transition: all 0.5s;
}

.active-link {
  color: #FFFFFF!IMPORTANT;
  background-color: #004ee7!IMPORTANT;
}

@media (max-width: 960px){
  .index_navigation{
    display: none;
  }
}

@media(max-width: 350px){
  .no-login button{
    display: none;
  }
}
</style>
