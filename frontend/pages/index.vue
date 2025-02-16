<script setup>
const hello = ref("Путешевствуй в компании");
const description = ref('Тысячи любителей впечатлений в одном месте')
import { apiConfig } from '@/api/api';


// const travels = ref([])

// const fetchTravels = async (fromCity, country) => {
//   const { data } = await useFetch('http://127.0.0.1:8000/api/travels/list/', {
//     method: 'GET',
//     query: {
//       from_city: fromCity,
//       country: country,
//     },
//   })
//   travels.value = data.value
//   console.log(travels.value)
//   // Пример вызова функции с параметрами
//   fetchTravels('Новосибирск', 'СССР')


const loaded = ref(true);

const {data: countries, error:countries_e, pending: countries_p} = useFetch(apiConfig.countries);

const limitedCountries = computed(() => {
  return countries.value ? countries.value.slice(0, 12) : [];
});

const {data: travels_from_moscow, error: travels_from_moscow_e, pending: travels_from_moscow_p} = useFetch(apiConfig.travel_from_moscow_now)

const {data: users, error: users_e, pending: users_p} = useFetch(apiConfig.users)
const FilterUsers = computed(() => {
  return users.value ? users.value.slice(0, 5) : [];
});
const {data: interests, error: interests_e, pending: interests_p} = useFetch(apiConfig.interests)
// Общее состояние загрузки
const isLoading = computed(() => countries_p || travels_from_moscow_p || users_p || interests_p);
// Отслеживание состояния загрузки
watchEffect(() => {
  if (isLoading.value) {
    console.log('Загрузка данных...');
  } else {
    console.log('Все данные загружены');
  }
});
const page = ref(false)

onMounted(async () => {
  // Измерение времени монтирования компонента
  setTimeout(() => {
    loaded.value = true;
    handleImageLoad;
  }, 70);
  // Установка loaded после завершения монтирования


  page.value = true;
  
});

</script>
<template>
    <slot>
    <div class="content">
    <div class="hello-layout">
      <!-- <UProgress
        animation="carousel"
        v-if="!page"
        style="margin: 100px 0px 70px 0px; max-width: 669px; width: 75%"
        color="#00C7BB"
      /> -->


      <div class="pulsar" style="margin: 75px 0px 0px 0px;font-size: clamp(25px, 4.99vw, 79px);max-width: max-content;" v-if="!page">
        <div class="block pulsate" style="height: max-content;color: #FFFFFF00;width: max-content;">Путешевствуй в компании</div>
      </div>

      <div class="pulsar" style="margin: 20px 0px 75px 0px;font-size: clamp(25px, 4.99vw, 25px);max-width: max-content;" v-if="!page">
        <div class="block pulsate" style="height: max-content;color: #FFFFFF00;width: max-content;">Путешевствуй в компании</div>
      </div>

      <h1 v-if="page" data-aos="fade-down">
        {{ hello }}
      </h1>
      <!-- <p>Travelo — это тысячи любителей впечатлений в одном месте</p> -->
      <p v-if="page">{{description}}</p>
      <div class="select_service wow animate__fadeInDown" style="visibility: visible; animation-name: fadeInDown;">
        <a href="/" class="active">
            <svg width="24" height="24" fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" focusable="false"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.34388 3.71925C6.21098 2.43331 8.40417 1.70258 10.6694 1.61169C12.9347 1.5208 15.1794 2.07347 17.1435 3.20569C19.1077 4.33792 20.7109 6.00337 21.7675 8.00918C22.8241 10.015 23.2909 12.2791 23.1139 14.5393C23.108 14.6546 23.0785 14.7839 23.0722 14.8048C22.5513 15.7519 18.3542 14.2632 13.477 11.5374L10.9179 16.0009H8.5974L11.7554 10.5392C7.00747 7.68232 3.68538 4.78324 4.19388 3.87925C4.23475 3.81804 4.28543 3.76398 4.34388 3.71925ZM13.5039 9.52925C14.9432 10.3723 16.4289 11.1335 17.9539 11.8093C18.8239 8.50925 18.4839 5.29925 16.5739 4.19925C14.6639 3.09925 11.7139 4.40925 9.29388 6.80925C10.6485 7.78913 12.0538 8.69706 13.5039 9.52925ZM22.84 6.88894C22.8382 6.91557 22.8382 6.9423 22.84 6.96894C22.8418 6.9423 22.8418 6.91557 22.84 6.88894ZM5 12.9989L8 16.9989H17C17.5304 16.9989 18.0391 17.2097 18.4142 17.5847C18.7893 17.9598 19 18.4685 19 18.9989V21.9989H17L15 19.9989H6L4 21.9989H2L4 18.6289L0 12.9989H5Z" fill="currentColor"></path></svg>
            <!-- <img src="" alt=""> -->
            <span>Путешествия</span>
        </a>
        <NuxtLink to="/trips/" class="">
            <svg width="24" height="24" fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" focusable="false"><path fill-rule="evenodd" clip-rule="evenodd" d="M15.5627 4.31989C16.2489 4.44411 16.929 4.60428 17.6 4.8C18.0063 4.92779 18.3613 5.18197 18.6131 5.52552C18.8649 5.86907 19.0005 6.28404 19 6.71V11C19 11 19 13 16 13H8C5.01625 13 5.00009 11.0216 5 11.0002V6.71C4.99955 6.28404 5.1351 5.86907 5.38692 5.52552C5.63874 5.18197 5.99367 4.92779 6.4 4.8C7.07103 4.60428 7.75107 4.44411 8.43726 4.31989L8.54 4.63C8.67246 5.02911 8.92735 5.37631 9.26845 5.62226C9.60954 5.86821 10.0195 6.00038 10.44 6H13.56C13.9805 6.00038 14.3905 5.86821 14.7316 5.62226C15.0726 5.37631 15.3275 5.02911 15.46 4.63L15.5627 4.31989ZM12 2C9.91535 2 7.84127 2.2963 5.84 2.88C5.01823 3.12901 4.29841 3.63586 3.78696 4.32559C3.27551 5.01533 2.99959 5.85133 3 6.71V22H6.94L7.94 20H16.08L17.08 22H21V6.71C21.0004 5.85133 20.7245 5.01533 20.213 4.32559C19.7016 3.63586 18.9818 3.12901 18.16 2.88C16.1587 2.2963 14.0847 2 12 2ZM5 15V17H9C9 16.4696 8.78929 15.9609 8.41422 15.5858C8.03914 15.2107 7.53043 15 7 15H5ZM19 17V15H17C16.4696 15 15.9609 15.2107 15.5858 15.5858C15.2107 15.9609 15 16.4696 15 17H19Z" fill="currentColor"></path></svg>
            <!-- <img src="" alt=""> -->
            <span>Попутчики</span>
        </NuxtLink>
        <a href="" class="opacity02">
            <!-- <img src="" alt=""> -->
            <svg width="24" height="24" fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" focusable="false"><path fill-rule="evenodd" clip-rule="evenodd" d="M4.00008 9.23198C3.47053 9.5043 3.01191 9.90225 2.66654 10.3947C2.20436 11.0536 1.97032 11.8457 2.00008 12.65V22H5.00008L6.00008 20H18.0001L19.0001 22H22.0001V12.65C22.0299 11.8457 21.7958 11.0536 21.3336 10.3947C20.9883 9.90225 20.5296 9.5043 20.0001 9.23198V6.5C20.0001 5.10218 20.0001 4.40326 19.7717 3.85195C19.4672 3.11687 18.8832 2.53284 18.1481 2.22836C17.5968 2 16.8979 2 15.5001 2H8.50008C7.10226 2 6.40335 2 5.85203 2.22836C5.11695 2.53284 4.53293 3.11687 4.22845 3.85195C4.00008 4.40326 4.00008 5.10217 4.00008 6.5V9.23198ZM16.5001 8.3357C13.5211 7.83464 10.479 7.83464 7.50008 8.3357V5.76C7.49813 5.66512 7.51578 5.57086 7.55191 5.48311C7.58804 5.39535 7.64189 5.316 7.71008 5.25C7.84572 5.1229 8.02421 5.0515 8.21008 5.05H8.36008C9.55768 5.30762 10.7758 5.45821 12.0001 5.5C13.2241 5.4615 14.4422 5.31425 15.6401 5.06H15.7901C15.976 5.0615 16.1545 5.1329 16.2901 5.26C16.3583 5.326 16.4121 5.40535 16.4483 5.4931C16.4844 5.58086 16.502 5.67512 16.5001 5.77V8.3357ZM4.00008 12.65V14H20.0001V12.65C20.0095 12.2924 19.9064 11.9408 19.7055 11.6448C19.5046 11.3488 19.2159 11.1233 18.8801 11C14.3827 9.71982 9.61742 9.71982 5.12008 11C4.78426 11.1233 4.49557 11.3488 4.29466 11.6448C4.09374 11.9408 3.99071 12.2924 4.00008 12.65Z" fill="currentColor"></path></svg>
        <span>Отели</span>
        </a>
        <a href="" class="opacity02">
            <svg width="24" height="24" fill="none" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" focusable="false"><path fill-rule="evenodd" clip-rule="evenodd" d="M20.9999 1.62029C21.7399 1.39029 22.3099 1.36029 22.4999 1.55029C22.6899 1.74029 22.6599 2.31028 22.4299 3.05028C21.9369 4.55211 21.1055 5.92062 19.9999 7.05026L17.9999 9.05025L18.9999 22.0502L17.9999 23.0502L13.6231 13.4211C12.8067 14.205 11.9296 14.9237 10.9999 15.5702C10.4417 16.0016 9.85336 16.3898 9.24026 16.7323L9.99995 22.0502L8.99995 23.0502L5.99997 18.0502L0.999995 15.0502L1.99999 14.0502L7.32418 14.8108C7.66569 14.1982 8.05177 13.6096 8.47996 13.0502C9.22994 11.978 10.0732 10.9741 10.9999 10.0502L16.9999 4.05027C18.1296 2.94464 19.4981 2.11326 20.9999 1.62029ZM1.99999 5.05027L0.999995 6.05027L9.38995 9.86025C10.5479 8.44318 11.8187 7.1222 13.1899 5.91027L1.99999 5.05027Z" fill="currentColor"></path></svg>
            <!-- <img src="" alt=""> -->
            <span>Авиабилеты</span>
        </a>

      </div>

      <div class="pulsar" style="margin: 0px 0px 0px 0px;" v-if="!page">
        <div class="block pulsate" style="height: 70px;color: #FFFFFF00;"></div>
      </div>

      <Search v-if="page"></Search>
      
      <IndexSearch :popular_countries="countries" :total_popular_countries="countries?.length" :limitedCountries="limitedCountries"></IndexSearch>
      
      <NuxtLink to="/travels" style="width:100%;display: flex;"><button class="other">Еще варианты: {{countries?.length}} шт.</button></NuxtLink>
    </div>
    <PopularRoad :travels_from_moscow></PopularRoad>
    <IndexFriends :popular_users="FilterUsers" :popular_interests="interests"></IndexFriends>
    <div class="info-slide" data-aos="fade-up" data-aos-anchor-placement="center-bottom">
      <div class="info-slide-layout">
      <!-- <span>KUDUGODNO</span> -->
      <img src="~/assets/img/kudaugodno_logo.png" alt="">
      <p>Это пространство для тех, кто жаждет приключений, хочет открыть новые горизонты и познакомиться с интересными людьми по всему миру</p>
      <p>KUDUGODNO — это виртуальная платформа, где встречаются души, стремящиеся к путешествиям. Мы понимаем, что иногда путешествовать в одиночку может быть скучно или даже небезопасно. Поэтому мы предлагаем вам возможность находить проверенных попутчиков — людей с подобными интересами, которые готовы разделить с вами впечатления и переживания. Основные функции: Поиск попутчиков: У нас есть удобный инструмент для поиска людей, желающих путешествовать в ту же сторону. Вы можете указать свои маршруты, даты и предпочтения, а также просматривать профили других путешественников. Чаты путешественников: Здесь вы можете общаться с другими участниками, делиться советами, рекомендовать места и задавать вопросы. Это отличное место для обмена опытом и получения новых идей для следующего путешествия. Знакомства: Мы понимаем, что иногда путешествия могут привести к романтическим встречам. Наш сайт предлагает возможность не только найти друзей-попутчиков, но и познакомиться с интересными людьми для возможных отношений.</p>
      <NuxtLink to="/about" class="about-link">
        <button>
          Узнать больше
      </button>
    </NuxtLink>
    </div>
    </div>
    <!-- <img src="~/assets/img/slider.png" alt=""> -->
  </div>
  <!-- <Footer></Footer> -->
    </slot>
</template>
<style>
.about-link{
  color: #FFFFFF;
  width: max-content;
  max-width: max-content;
  
  && a{
    color: #FFFFFF;
    width: max-content;
    max-width: max-content;
  }

  && a:hover{
    opacity: 0.9;
  }
}
umodal{
  display: none!IMPORTANT;
}
.info-slide-layout img{
  object-fit: contain;
  max-width: 249px;
  margin: 0 0 25px 0;
}
.select_service {
    display: flex;
    align-items: center;
    justify-content: space-around;
    max-width: max-content;
    margin: 0px 0px 25px 0px;
}

.select_service a.active {
    padding: 0px 0px 15px 0px;
    color: #00c7bb ! IMPORTANT;
    color: #7e52c7 ! IMPORTANT;
    font-weight: 700;
    background-color: #7e52c7;
    background-color: #2963d6;
    padding: 0px 0px 15px 0px;
    color: #00c7bb ! IMPORTANT;
    color: #ffffff ! IMPORTANT;
    font-weight: 700;
}

.select_service a {
    display: inline-flex;
    align-items: center;
    margin: 0px 15px 0px 15px;
    padding: 0px 0px 15px 0px;
    font-weight: 700;
    transition: all 0.5s;
    -webkit-transition: all 0.5s;
    -moz-transition: all 0.5s;
    display: inline-flex;
    align-items: center;
    margin: 0px 9px 0px 9px;
    padding: 0px 0px 15px 0px;
    font-weight: 700;
    transition: all 0.5s;
    -webkit-transition: all 0.5s;
    -moz-transition: all 0.5s;
    border-radius: 179px;
    padding: 9px 15px 9px 15px ! IMPORTANT;
    background-color: #f3f3f3;
}

.select_service svg {
    width: 19px;
    height: 19px;
}

.select_service img, svg {
    margin: 0px 5px 0px 0px;
    width: 25px;
    height: 25px;
    object-fit: cover;
}

.opacity02 {
    opacity: 0.2;
}



@media(max-width: 960px){
  .select_service a span{
    display: none;
  }
  .select_service svg{
    margin: 0 0 0 0;
  }
}

@media (max-width: 490px){
  .hello-layout h1{
    width: 90%;
    text-align: center;
    font-size: 35px;
    margin: 35px 0px 9px 0px;
    line-height: 1.2;
    text-align: left;
  }
  .hello-layout p{
    width: 90%;
    font-size: 17px;
    margin: 0px 0px 35px 0px;
    text-align: left;
  }
}
</style>