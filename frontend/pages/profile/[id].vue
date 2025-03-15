<script setup>
definePageMeta({
    layout: 'pages',
})
import {API, apiConfig, base_url} from '@/api/api'
import axios from 'axios';
const user = ref([]);
const error = ref(null);
const pending = ref(true);


const user_trips = ref([])
const user_travels = ref([])
const route = useRoute()
console.log(route.params.id)

// Функция для создания задержки
const delay = (ms) => new Promise(resolve => setTimeout(resolve, ms));

const fetchUser = async () => {
  try {
    await delay(0); // Задержка в 2 секунды
    const response = await axios.get(`${apiConfig.users}${route.params.id}/`);
    user.value = response.data;
    console.log(`фывфыв фыв ${user.value}`)
    await fetchUserTrips();
    await fetchUserTravels();
  } catch (err) {
    error.value = err;
  } finally {
    pending.value = false;
  }
};

const fetchUserTrips = async () => {
  try {
    await delay(0); // Задержка в 2 секунды
    const response = await axios.get(`${apiConfig.user_trips}${route.params.id}/`);
    user_trips.value = response.data;
    // console.log(`фывфыв фыв ${user.value}`)
  } catch (err) {
    error.value = err;
  } finally {
    // pending.value = false;
  }
};

const fetchUserTravels = async () => {
  try {
    await delay(0); // Задержка в 2 секунды
    const response = await axios.get(`${apiConfig.user_travels}${route.params.id}/`);
    user_travels.value = response.data;
    // console.log(`фывфыв фыв ${user.value}`)
  } catch (err) {
    error.value = err;
  } finally {
    // pending.value = false;
  }
};
onMounted(async ()=>{
    await fetchUser();
})
</script>
<template>
<div class="content wow animate__fadeInDown" style="width: 100%; max-width: 100%; visibility: visible; animation-name: fadeInDown;background-color: #FFFFFF;padding: 25px 25px 25px 25px;border-radius: 15px;" v-if="!pending" data-aos="fade-down">
    <div class="user-layer">
      <div class="user-info-layer">

      <img :src="user?.photo" class="user-avatar" alt="">
           
      <div class="user-info">
        <div class="user-rating">

          <h2>{{user?.first_name}} {{user?.last_name}}, {{user?.age}} лет</h2>
            <div class="user_city">
                <img src="~/assets/img/pic_location_grey.png" alt="">
                <span v-if="user?.city">{{user?.city?.name}}</span>
                <span v-else>Город не указан</span>
            </div>

<!-- 
          <div class="rating_layout_star" data-total-value="5">
            <div class="rating_star" data-item-value="5">★</div>
            <div class="rating_star" data-item-value="4">★</div>
            <div class="rating_star" data-item-value="3">★</div>
            <div class="rating_star" data-item-value="2">★</div>
            <div class="rating_star" data-item-value="1">★</div>
          </div> -->

        </div>
        <span>Online</span>
        <p>{{user.small_description}}</p>

        </div>
      </div>
              <!-- <a href="/chats/message/62/"><button style="max-width: max-content;font-size:15px;"><img src=""> Написать сообщение</button></a> -->
        

    </div>

    <!-- <div class="user-nav_profile">
      <a to="/me" class="active">О себе</a>
      <a to="/comments">Отзывы</a>
      <a to="/posts">Объявления</a>
    </div> -->


    <div class="tab">
      <input checked="" id="tab-btn-1" name="tab-btn" type="radio" value="">
      <label for="tab-btn-1">О себе</label>
      <input id="tab-btn-2" name="tab-btn" type="radio" value="">
      <label for="tab-btn-2">Друзья (
        <template v-if="!user?.users_friends">
          0
        </template>
        <template v-else>
          {{user?.users_friends[0]?.friends?.length}}
        </template>       
        )</label>
      <!-- <input id="tab-btn-2" name="tab-btn" type="radio" value=""> -->
      <!-- <label for="tab-btn-2">Отзывы</label>-->
      <input id="tab-btn-3" name="tab-btn" type="radio" value="">
      <label for="tab-btn-3">Путешествия (        
        <template v-if="!user_travels?.length">
          0
        </template>
        <template v-else>
          {{user_travels?.length}}
        </template>        
        )</label>
      <input id="tab-btn-4" name="tab-btn" type="radio" value=""> 
      <label for="tab-btn-4">Поездки (
        <template v-if="!user_trips?.length">
          0
        </template>
        <template v-else>
          {{user_trips?.length}}
        </template>
        

        )</label>
      <div class="tab-content" id="content-1" style="border-top: 1px solid #00000025;margin: -17px 0px 0px 0px;padding: 25px 0px 0px 0px;">
    <!-- <div class="photos-layout">
      <UCarousel v-slot="{ item }" :items="items">
        <img :src="item" width="250" height="350" draggable="false">
      </UCarousel>
    </div> -->

    <div class="about-user">
      <h2>О себе</h2>
      {{user?.description}}
      
       <!--<AboutUser :abouts="abouts" :margin="margin"></AboutUser> -->
      
<div class="aboutUser aboutUser" style="/*border-bottom: 1px solid #ebebeb;*/margin: 15px 0px 15px 0px!IMPORTANT;padding: 0px 0px 0px 0px;">
    
</div>

    </div>

    <div class="intresting">
      <h2>Интересы</h2>
      <RoadViews :popular_interests="user?.interests"></RoadViews>
      <div class="road-view">
    
        </div>

    </div>  

      </div>
      <!-- <div class="tab-content" id="content-2">
    
    
      </div> -->
      <div class="tab-content" id="content-3" style="border-top: 1px solid #00000025;margin: -17px 0px 0px 0px;padding: 0px 0px 0px 0px;">

        <NuxtLink :to="`/travels/${travel.id}/`" v-for="travel in user_travels" :key="travel.id">
        <div class="travel">
            <img :src="travel?.user?.photo" alt="">
            <div class="travel_cart_info">
                <h2>
                    <span v-for="country in travel?.country">{{ country?.name }},&nbsp;</span>
                </h2>
                <div class="travel_cart_user_info">
                    <h3>{{travel?.user?.first_name}} {{travel?.user?.last_name}} , Возраст: {{travel?.user?.age}}</h3>
                    <div class="user_cart_search">
                        <span>{{travel?.gender}} ищет {{travel?.gender_search}}</span> на {{travel?.days}} дней
                    </div>
                </div>
                <!-- <h1>{{travel.id}}</h1> -->
                <p>{{travel?.description}}</p>
            </div>
        </div>
    </NuxtLink>
        
      </div>
      <div class="tab-content" id="content-4" style="border-top: 1px solid #00000025;margin: -17px 0px 0px 0px;padding: 17px 0px 0px 0px;">
        
        <TripCard :search_trip="trip" v-for="trip in user_trips"></TripCard>

      </div>

      <div class="tab-content" id="content-2" style="border-top: 1px solid #00000025;margin: -17px 0px 0px 0px;padding: 17px 0px 0px 0px;">
        <div class="friend" v-for="friend in user?.users_friends[0]?.friends" :key="friend?.id">
          <div class="friend_info">
            <img :src="friend?.photo" alt="">
          </div>
          <div class="friend_name">
            <NuxtLink :to="`/profile/${friend?.id}`">{{friend?.first_name}} {{friend?.last_name}}</NuxtLink>
          </div>
        </div>

      </div>
    </div>

     
  </div>
</template>
<style scoped>
.friend{
  display: flex;
  width: 100%;
  margin: 0px 0px 0px 0px;
  padding: 15px 0px 15px 0px;
  align-items: center;
  border-bottom: 1px solid #d7d7d7;;
}
.friend_info{
  display: flex;

  img{
    max-width: 50px;
    max-height: 50px;
    border-radius: 115px;
    width: 50px;
    height: 50px;
    object-fit: cover;
    margin: 0px 15px 0px 0px;
  }
}
.about-user{
  margin: 0px 0px 25px 0px;
}
.user-layer {
    /* padding: 25px 25px 25px 25px; */
    border-radius: 25px;
    /* border: 1px solid #d2d2d2; */
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.user-info-layer {
    display: flex;
    align-items: center;
}

.user-info {
    display: flex;
    align-items: flex-start;
    flex-direction: column;
    line-height: 1.5;
}

.user-avatar {
    border-radius: 500px;
    width: 95px;
    height: 95px;
    margin: 0px 25px 0px 0px;
    object-fit: cover;
}

.user-info span {
    font-size: 15px;
    color: #d2d2d2;
}

.user-info h2 {
    font-weight: 700;
    font-size: 19px;
}
.user-rating h2 {
    margin: 0px 5px 0px 0px;
    display: flex;
    align-items: center;
}

.user-rating {
    display: flex;
    align-items: center;
}

.user_city {
    display: inline-flex;
    align-items: center;
    padding: 0px 0px 0px 0px;
}

.about-user h2 {
    font-size: 19px;
    font-weight: bold;
    margin: 0px 0px 15px 0px;
}

.intresting h2 {
    font-size: 19px;
    font-weight: 700;
    margin: 0px 0px 15px 0px;
}
.rating_layout_star[data-total-value="1"] .rating_star:nth-child(n + 5), .rating_layout_star[data-total-value="2"] .rating_star:nth-child(n + 4), .rating_layout_star[data-total-value="3"] .rating_star:nth-child(n + 3), .rating_layout_star[data-total-value="4"] .rating_star:nth-child(n + 2), .rating_layout_star[data-total-value="5"] .rating_star:nth-child(n + 1) {
    color: #f0be19;
}
.rating_layout_star {
    display: inline-flex;
    flex-direction: row-reverse;
}

ul, li, a {
    list-style: none;
    text-decoration: none;
}

.user-layer button {
    margin: 0px 0px 0px 0px;
    border-radius: 50px;
    border: 1px solid #ebebeb;
    padding: 9px 15px 9px 15px;
    font-size: 17px;
    display: inline-flex
;
    align-items: center;
    border: 1px solid #DDD;
    /* border-radius: 7px; */
    box-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
}

.tab {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
    margin: 35px 0px 0px 0px;
}

.tab > input[type="radio"] {
    display: none;
}

.tab > input[type="radio"]:checked + label {
    cursor: default;
    font-weight: bold;
    color: #212529;
    border-bottom-color: #212529;
    color: #0d6efd;
    border-bottom-color: #0d6efd;
}

.tab > label {
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
    cursor: pointer;
    transition: color .15s ease-in-out, border-color .15s ease-in-out;
    color: #0d6efd;
    color: #292929;
    background: 0 0;
    border-bottom: 0.125rem solid transparent;
    font-weight: 700;
}

.tab > input[type="radio"] {
    display: none;
}

#tab-btn-1:checked~#content-1, #tab-btn-2:checked~#content-2, #tab-btn-3:checked~#content-3, #tab-btn-4:checked~#content-4 {
    display: block;
}

.tab-content {
    display: none;
    width: 100%;
    margin-top: 1rem;
}







.travel_cart_user_info{
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

.travel_cart_info{
    width: 100%;
    display: flex;
    flex-direction: column;
}

/* travel */
.travel{
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

@media (max-width: 490px){
    .travel{
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
    .travel_cart_user_info {
        text-align: center;
    }
}
</style>