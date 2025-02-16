<script setup>
definePageMeta({
  middleware: ['auth'],
})

import {useAuthStore} from '@/stores/auth';
const {user, isAuthenticated, logout} = storeToRefs(useAuthStore());
import { authAxios } from "@/composables/authAxiosSettings";
import { base_url } from '@/api/api';
const newAxios = authAxios();



const fetch_user = ref(null)

const photo = ref(null)
const last_name = ref( null)
const first_name = ref(null)
const patronymic = ref(null)
const age = ref(null)
const phone = ref(null)
const email = ref(null)
const description = ref(null)
const small_description = ref(null)
const habits = ref(null)
const interests = ref(null)

const loadUser = ref(true)

async function fetchUser() {
      let res = null; // Создаем переменную для хранения результата
      
      try {
          const response = await newAxios.get('/profile-info/');
          if (response.data) {
              res = response.data; // Сохраняем данные в переменную
              console.log(`ПОЛУЧАЕМ ИНФОРМАЦИЮ ПО ЮЗЕРУ ${response.data}`)
          } else {
              console.warn("No user data found");
              console.log("No user data found");

          }
      } catch (error) {
          console.error("Error fetching user data:", error);
          console.log("Error fetching user data:", error);
          throw error; // Пробрасываем ошибку дальше
      } finally {
          // Здесь мы обновляем переменные только если res не null
          if (res) {
              fetch_user.value = res
              loadUser.value = false

              last_name.value = res.last_name
              first_name.value = res.first_name
              patronymic.value = res.patronymic
              photo.value = res.photo
              age.value = res.age
              phone.value = res.phone
              email.value = res.email
              description.value = res.description
              small_description.value = res.small_description
              habits.value = res.habits
              interests.value = res.interests
              


          } else {
            logout()
            navigateTo('/')
          }
      }
  }


onMounted(async () => {

await fetchUser()

})

const updateNikname = (event) => {
    form.value.nikname = event.target.value; // Обновляем значение никнейма
};

const updateLastName = (event) => {
    form.value.last_name = event.target.value; // Обновляем значение фамилии
};

const updateFirstName = (event) => {
    form.value.first_name = event.target.value; // Обновляем значение имени
};

const updatePatronymic = (event) => {
    form.value.patronymic = event.target.value; // Обновляем значение отчества
};

const handleFileUpload = (event) => {
    const file = event.target.files[0]; // Получаем первый выбранный файл
    if (file) {
        photo.value = file; // Сохраняем файл в объекте form
        console.log('File selected:', file); // Проверяем, что файл выбран
    }
};

const editProfile = async () => {
  
    const data = {
        last_name: last_name.value,
        first_name: first_name.value,
        patronymic: patronymic.value,
        age: age.value,
        phone: phone.value,
        email: email.value,
        description: description.value,
        small_description: small_description.value,
        habits: habits.value,
        interests: interests.value,
    };

    if (photo.value && photo.value != user?.value?.photo) {
        data.photo = photo.value;
    }
 
    if (
        last_name.value == user?.value?.last_name &&
        first_name.value == user?.value?.first_name &&
        patronymic.value == user?.value?.patronymic &&
        age.value == user?.value?.age &&
        phone.value == user?.value?.phone &&
        email.value == user?.value?.email &&
        description.value == user?.value?.description &&
        small_description.value == user?.value?.small_description &&
        habits.value == user?.value?.habits &&
        interests.value == user?.value?.interests
    ){
        location.reload();
    } else{
        try {
        const response = await newAxios.patch('profile-info/', data, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
        });
        console.log(response);
        console.log(data.photo);
        location.reload();
        } catch (error) {
            console.log(error);
        }
    }
}
</script>
<template>
<div class="user-layer wow animate__fadeInUp" style="visibility: visible; animation-name: fadeInUp;" v-if="!loadUser">
  <div class="form_layer">
    <form action="" method="post" enctype="multipart/form-data" @submit.prevent="editProfile">
      <input type="hidden" name="csrfmiddlewaretoken" value="oK2RM2m6iHGgJZXCuevdZxkCe39vic3pcHRrtI7dgaRtcpDQsJiCXweUlE7YLq03">
      <div class="profile_left">

        <p>
          <!-- <label for="id_photo">Avatar:</label> -->
          
        <img :src="`${base_url}${user?.photo}`" alt="">
          
          
      <input @change="handleFileUpload" type="file" name="photo" accept="image/*" id="id_photo" style="border-radius: 0px 0px 9px 9px;">         
        </p>  

        <p style="margin:0px 0px 15px 0px;">
          <label for="id_description">Описание страницы:</label>
          <textarea name="description" id="id_description" :value="description" @input="description = $event.target.value"></textarea>
        </p>
        <p>
          <label for="id_small_description">Краткое описание:</label>
          <input type="text" name="small_description" maxlength="99" id="id_small_description" :value="small_description"
           @input="small_description = $event.target.value"
          >
        </p>

 
      </div>
      <div class="profile_right">



        <div class="ineteres_layer">
          <div class="info">
            <h2>Основная информация</h2>
            <p>
              <label for="id_first_name">Имя:</label>
              <input type="text" name="first_name" :value="first_name" maxlength="100" id="id_first_name"
               @input="first_name = $event.target.value"
              >
              
              
            </p>
          
            
            <p>
              <label for="id_last_name">Фамилия:</label>
              <input type="text" name="last_name" v-model="last_name" :true-value="`asdasdsadasd`" maxlength="100" id="id_last_name"
              @input="last_name = $event.target.value"
              >
              
              
            </p>
          
            
            <p>
              <label for="id_patronymic">Отчество:</label>
              <input type="text" name="patronymic" :value="patronymic" maxlength="100" id="id_patronymic"
              @input="patronymic = $event.target.value"
              >
  
            </p>
            <p>
              <label for="id_age">Возраст:</label>
              <input type="number" name="age" :value="age" id="id_age"
              @input="age = $event.target.value"
              >           
            </p>
          </div>
          <h2>Интересы</h2>
          <p>
            <label for="id_habits">Привычки:</label>
            <select name="habits" id="id_habits" multiple="">      
            <!-- <option value="1">Курю</option>       -->
                <option :value="habbit.id" v-for="habbit in habits" @input="habits = $event.target.value">{{habbit.name}}</option>
            </select>
                      
          </p>
          <p>
            <label for="id_interests">Интересы:</label>
            <select name="interests" id="id_interests" multiple="">
            
            <option :value="interest.id" v-for="interest in interests" @input="interest = $event.target.value">{{interest.name}}</option>
                      
            <!-- <option value="1">Москва</option> -->
        </select>
            
            
          </p>
          <p>
            <label for="id_phone">Телефон:</label>
            <input type="text" name="phone" :value="phone" maxlength="24" id="id_phone"
            @input="phone = $event.target.value"
            >
          </p>
          
          <p>
            <label for="id_email">Емейл адрес:</label>
            <input type="email" name="email" :value="email" maxlength="254" id="id_email"
            @input="email = $event.target.value"
            readonly
            >                      
          </p>
        </div>  


  
  
  
  
      
  
      
        
      
<!--       
        <div class="password_info">
          <h2>Изменение пароля</h2>
  
          <p>
            <label for="id_password">Новый пароль:</label>
            <input type="password" name="password" id="id_password">      
          </p>
        
          <p>
            <label for="id_confirm_password">Подтвердите пароль:</label>
            <input type="password" name="confirm_password" id="id_confirm_password">
          </p>
  
  
        </div>
  
   -->

  
  
        <button type="submit">Сохранить</button>

        

      </div>

    </form>
  </div>
     
  </div>
</template>
<style scoped>
  .contant_info{
    width: 100%;
  }
  .ineteres_layer{
    width: 100%;
    margin: 0px 0px 15px 0px;
  }
  .form_layer{
    display: flex;
    flex-direction: column;
    width: 100%;
  }.form_layer form{
    display: flex;
    flex-direction: row;
    box-shadow: none;
    width: 100%;
    max-width: 100%;
    border: 1px solid #ffffff;
    justify-content: flex-start;
    align-items: flex-start;
    line-height: 1.9;
    justify-content: space-between;
  }.form_layer form p{
    display: flex;
    flex-direction: column;
    font-size: 12px;
    width: 100%;
    max-width: 100%;
  }.form_layer form input{
    width: 100%;
    padding: 15px 25px;
    border-radius: 9px;
    border: 1px solid #00000019;
    background-color: #00000009;
    font-size: 15px;
    margin: 0px 0px 25px 0px;
  }.form_layer form h2{
    margin: 0px 0px 15px 0px;
  }.form_layer form button{
    max-width: max-content!IMPORTANT;
    width: 100%!IMPORTANT;
    max-width: 100%!IMPORTANT;
    text-align: center!IMPORTANT;
    justify-content: center;
    height: 50px;
    background-color: #2963d6;
    color: #FFFFFF;
  }

  .user-layer {
    /* padding: 25px 25px 25px 25px; */
    border-radius: 25px;
    /* border: 1px solid #d2d2d2; */
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 1279px;
    width: calc(100% - 35px);
}

.form_layer form {
    display: flex;
    flex-direction: row;
    box-shadow: none;
    width: 100%;
    max-width: 100%;
    max-width: 1279px!IMPORTANT;
    width: calc(100% - 29px)!IMPORTANT;
    border: 1px solid #ffffff;
    justify-content: flex-start;
    align-items: flex-start;
    line-height: 1.9;
    justify-content: space-between;
    margin: 40px auto 0 auto;
}

.form_layer {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 0px 0px 100px 0px;
}

form {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: calc(100% - 27px);
    max-width: 768px;
    border-radius: 50px;
    border: 1px solid #00000015;
    padding: 5px 5px 5px 5px;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.05);
    font-weight: 500;
    font-size: 17px ! IMPORTANT;
    transition: all 0.3s;
    -moz-transition: all 0.3s;
    -webkit-transition: all 0.3s;
}

.form_layer form {
    display: flex;
    flex-direction: row;
    box-shadow: none;
    width: 100%;
    max-width: 100%;
    border: 1px solid #ffffff;
    justify-content: flex-start;
    align-items: flex-start;
    line-height: 1.9;
    justify-content: space-between;
}

.form_layer form input {
    width: 100%;
    padding: 15px 25px;
    border-radius: 9px;
    border: 1px solid #00000019;
    background-color: #00000009;
    font-size: 15px;
    margin: 0px 0px 25px 0px;
}

.profile_left {
    display: flex;
    flex-direction: column;
    width: 45%;
    margin: 0vw 2vw 0vw 0vw;
    max-width: 400px;
}

.form_layer form p {
    display: flex;
    flex-direction: column;
    font-size: 12px;
    width: 100%;
    max-width: 100%;
}

.profile_right {
    display: flex;
    flex-direction: column;
    width: 100%;
}

.ineteres_layer {
    width: 100%;
    margin: 0px 0px 15px 0px;
}

.info {
    width: 100%;
}

.form_layer form h2 {
    margin: 0px 0px 15px 0px;
}

.contant_info {
    width: 100%;
}

.password_info {
    width: 100%;
}

.form_layer form button {
    max-width: max-content;
}

.user-layer button {
    margin: 0px 0px 0px 0px;
    border-radius: 50px;
    border: 1px solid #ebebeb;
    padding: 9px 15px 9px 15px;
    font-size: 17px;
    display: inline-flex;
    align-items: center;
    border: 1px solid #DDD;
    /* border-radius: 7px; */
    box-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
}

.user-layer{
    width: 100%!IMPORTANT;
    justify-content: center;
    align-items: center;
    max-width: 100%;
}

.profile_left img{
    border-radius: 15px 15px 0px 0px;
}

textarea{
    font-family: "Inter", sans-serif;
    font-size: 15px;
    padding: 20px 20px 20px 20px;
    border-radius: 9px;
    border: 1px solid #00000019;
    background-color: #00000009;
    max-width: 400px;
    max-height: 400px;
}



select {
    cursor: pointer;
    padding: 20px 20px 20px 20px;
    border-radius: 9px;
    border: 1px solid #00000019;
    background-color: #00000009;
    display: flex;
    flex-wrap: wrap;
    margin: 0px 0px 20px 0px;
}

option{
    margin: 9px 0px 0px 0px;
    border-bottom: 2px solid #dcdcdc;
    padding: 9px 15px 9px 15px;
    font-size: 15px;
    border-radius: 9px;
    background-color: #FFFFFF;
    max-width: max-content;
}
</style>