<script lang="ts" setup>
const props = defineProps(['popular_users', 'popular_interests'])
const limitedUsers = ref([]);
// const interests = ref()

// onMounted(async () => {
//   interests.value = await $fetch('http://localhost:8000/interests/')
// });


// const views = ref([
//   { id: 1, title: "Лес", image: "./view.png" },
//   { id: 2, title: "Театр", image: "./view2.png" },
//   { id: 3, title: "Знакомства", image: "./view3.png" },
//   { id: 4, title: "Комедии", image: "./view4.png" },
//   { id: 5, title: "Спортзал", image: "./view5.png" },
//   { id: 6, title: "Конный спорт", image: "./view6.png" },
//   { id: 7, title: "Парусный спорт", image: "./view7.png" },
//   { id: 8, title: "Еда", image: "./view8.png" },
//   { id: 9, title: "Фотографии", image: "./view9.png" },
//   { id: 10, title: "Фотографии", image: "./view3.png" },
//   { id: 11, title: "Дайвинг", image: "./view7.png" },
//   { id: 12, title: "Параплыны", image: "./view2.png" },
//   { id: 13, title: "Прогулки", image: "./view.png" },
// ]);

// const users = ref([
//   {
//     id: 1,
//     first_name: "Виктория",
//     photo: "./photo.png",
//     description: "Описание профиля пользователя",
//   },
//   {
//     id: 2,
//     first_name: "Инчон",
//     photo: "./photo2.png",
//     description: "Описание профиля пользователя",
//   },
//   {
//     id: 3,
//     first_name: "Настя",
//     photo: "./photo3.png",
//     description: "Описание профиля пользователя",
//   },
//   {
//     id: 4,
//     first_name: "Сергей",
//     photo: "./photo4.png",
//     description: "Описание профиля пользователя",
//   },
//   {
//     id: 5,
//     first_name: "Алёна",
//     photo: "./photo5.png",
//     description: "Описание профиля пользователя",
//   },
// ]);
</script>
<template>
  <div
    class="index-friends-layout"
    data-aos="fade-up"
    data-aos-anchor-placement="center-bottom"
  >
    <div class="index-friends-title">
      <h2>Найди друга по интересам</h2>
      <!-- <button>Как найти надежного попутчика ></button> -->
    </div>
    <div class="friends-layout">
      <roadViews :popular_interests></roadViews>
      <div class="index-friends-users">
        <div class="index-friends-user" v-for="(user, index) in popular_users" :key="user.id">
          <NuxtLink :to="`profile/${user.id}`">
          <img :src="user.photo" alt="" />
            <span>{{ user.first_name }}</span>
          </NuxtLink>
          <p v-if="user.city">{{ user?.city?.name }}</p>
          <p v-else>Не заполнено</p>
        </div>
      </div>
    </div>
    <NuxtLink to="/users" style="display: flex;"><button class="other">Показать всех</button></NuxtLink>
  </div>
</template>
<style scoped>
.index-friends-layout {
  width: 100%;
  margin: 75px auto auto;
}
.index-friends-layout h2 {
  font-size: 25px;
  font-weight: 700;
}
.friends-layout {
  width: 100%;
  margin: 0 auto 35px;
}
.index-friends-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0px 0px 25px 0px;
}

.index-friends-users {
  margin: 50px 0px 0px 0px;
  display: flex;
  justify-content: space-between;
  overflow: hidden;
  overflow-x: auto;
}
.index-friends-user {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  width: 100%;
  max-width: 150px;
  min-width: 115px;
  min-height: 115px;
}
.index-friends-user a{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  width: 100%;
}
.index-friends-user img {
  border-radius: 1000px;
  max-width: 150px;
  max-height: 150px;
  margin: 0px 0px 15px 0px;
  width: 100%;
  height: 100%;
  object-fit: cover;
  min-width: 150px;
  min-height: 150px;
}
.index-friends-user span {
  font-size: 19px;
  font-weight: 700;
  width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.index-friends-user p {
  font-size: 15px;
  color: #9b9b9b;
  width: 79%;
  max-width: 150px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: grid;
  max-height: 48px;
  text-align: center;
  margin: 9px 0px 0px 0px;
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
@media (max-width: 770px) {
  .index-friends-layout {
    margin: 0px auto 35px;
  }
  .index-friends-title {
    width: calc(100% -30px);
    flex-direction: column;
    align-items: flex-start;
    padding: 0px 0px 0px 15px;
  }
  .index-friends-title h2 {
    font-size: 4vw;
  }.index-friends-title button{
    display: none;
  }
  .road-view {
    overflow: hidden;
    overflow-x: auto;
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    grid-template-rows: repeat(2, auto);
    padding: 0px 15px 0px 15px;
  }
  .index-friends-user {
    margin: 0px 15px 0px 0px;
  }
  .index-friends-user img {
    max-width: 135px;
  }
  .index-friends-user p {
    font-size: 12px;
    padding: 0px;
    width: 100%;
    margin: 0px 0px 0px 0px;
  }
  .index-friends-users {
    padding: 0px 15px 0px 15px;
    margin: 0px 0px 35px 0px;
  }
  .index-friends-user{
    max-width: 115px;
    margin: 0px 25px 0px 0px;
  }
  .index-friends-user img{
    max-height: 115px;
    max-width: 115px;
    height: 100%;
    width: 100%;
    min-width: 115px;
    min-height: 115px;
  }
}

@media (max-width: 490px){
  .other {
        width: calc(100% - 30px);
    }
}
</style>
