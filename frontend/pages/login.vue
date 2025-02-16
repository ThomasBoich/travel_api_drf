<script setup>
import {useAuth} from '@/composables/auth';
const {login} = useAuth();

definePageMeta({
    layout: ['auth'],
    middleware: ['auth']
})

const email = ref('')
const password = ref('')

async function userLogin(){
    login(email.value, password.value)
}
</script>
<template>
<div class="text-layout">

            <div class="form1">
              <span style="white-space: wrap;display: inline;">
              Войдите в систему,
              чтобы открыть все возможности
              Trave<span style="color:#4dd8cf;">lo</span>.

              </span>
              <form method="post" action="" style="box-shadow: none;border:none;" @submit.prevent="userLogin">
                <input type="hidden" name="csrfmiddlewaretoken" value="NuGkOSv3jyHNNUNQbZJagWKaOMyq4XJOWDvXm2w2A4eWZ44Oo09VFn5fGFlOVfXK">

                <input type="email" name="username" id="id_username" placeholder="Электронная почта" required="" v-model="email">
                <input type="password" name="password" id="id_password" placeholder="Пароль" required="" v-model="password">
                <button type="submit">Войти</button>
              </form>
             <a id="new_form">Нет аккаунта? <span>Зарегистрироваться</span></a>
            </div>
            <!-- <div class="form2">
              <span>
Начните свой пусть на Trave<span style="color:#4dd8cf;">lo</span>.
              </span>
              <form class="" action="/registration/" method="post">
                <input type="hidden" name="csrfmiddlewaretoken" value="NuGkOSv3jyHNNUNQbZJagWKaOMyq4XJOWDvXm2w2A4eWZ44Oo09VFn5fGFlOVfXK">

                <input type="email" name="email" maxlength="254" id="id_email" placeholder="Электронная почта"> 
                <input type="text" name="first_name" maxlength="100" id="id_first_name" placeholder="Имя">             
                <input type="text" name="last_name" maxlength="100" id="id_last_name" placeholder="Фамилия">    
                <input type="text" name="patronymic" maxlength="100" id="id_patronymic" placeholder="Отчество">
                <input type="password" name="password" maxlength="128" required="" aria-invalid="true" id="id_password" placeholder="Пароль">

                <button type="submit">Создать аккаунт</button>
              </form>
              <a id="za_form">Есть аккаунт?<span>Войти</span></a>
            </div> -->
         <div class="copy">
          Продолжай, Вы соглашайтесь с <span>Условиями использования</span> и <span>Политикой конфиденциальности</span>, а так же с <span>Политикой использования файлов cookie</span>.
         </div>
          </div>
</template>
<style scoped>
.text-layout {
    font-weight: 900;
    font-size: 25px;
    width: 100%;
    padding: 2vw;
    display: inline-flex;
    flex-direction: column;
}

.text-layout input {
    font-size: 17px;
    font-weight: 700;
    border: 1px solid #000000;
    width: 100%;
    padding: 15px 15px 15px 25px;
    margin: 0px 0px 15px 0px;
    border-radius: 50px;
    font-size: 17px;
    font-weight: 700;
    border: 1px solid #d9d9d9;
    width: 100%;
    padding: 15px 15px 15px 25px;
    margin: 0px 0px 15px 0px;
    border-radius: 50px;
    background-color: #ececec;
    color: #000000!IMPORTANT;
}



.text-layout input:-webkit-autofill,
.text-layout input:-webkit-autofill:hover,
.text-layout input:-webkit-autofill:focus,
.text-layout input:-webkit-autofill:active{
    -webkit-box-shadow: 0 0 0 30px #ececec inset !important;
    color: #000000!IMPORTANT;
}

/*Change text in autofill textbox*/
.text-layout input:-webkit-autofill{
    -webkit-text-fill-color: #000000 !important;
}
.text-layout form {
    display: flex;
    flex-direction: column;
    margin: 25px 0px 0px 0px;
}

.text-layout button {
    font-size: 17px;
    font-weight: 700;
    background-color: #4dd8cf;
    padding: 15px;
    border-radius: 50px;
    margin: 0px 0px 25px 0px;
    width: 100%;
}

.text-layout button:hover {
    background-color: #54e9df;
}

.text-layout a {
    font-size: 17px;
    text-align: center;
    font-weight: 700;
}

.form1 a {
    margin: 0 auto;
    text-align: center;
    max-width: max-content;
    display: table;
}

.text-layout a span {
    cursor: pointer;
}

.text-layout a span {
    color: #4ac9c0;
}

.text-layout{
    width: 100%;
    max-width: 100%;
    border-radius: 0px;
    border: none;
    border-bottom: 2px solid #dddddd;
    border: 1px solid #dddddd;
    box-shadow: none;
    margin: 0px 0px 25px 0px;
    background-color: #ffffff;
    padding: 50px 50px 50px 50px;
    border-radius: 15px;
    display: flex;
    justify-content: center;
    max-width: 479px;
    margin: 0 auto;
}

.text-layout form {
    display: flex;
    flex-direction: column;
    margin: 25px 0px 0px 0px;
}

form {
    width: 100%;
    max-width: 100%;
    border-radius: 0px;
    border: none;
    box-shadow: none;
    margin: 0 auto;
    background-color: #ffffff;
}

.form1{
    display: flex;
    width: max-content;
    flex-direction: column;
    margin: 0 auto;
    width: 100%;
}

.text-layout .copy {
    font-size: 13px;
    text-align: center;
    font-weight: 700;
    margin: 25px 0px 0px 0px;
    color: #b5b5b5;
}
</style>