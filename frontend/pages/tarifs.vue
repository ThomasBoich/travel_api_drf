<script setup>
    import {useAuthStore} from '@/stores/auth';
    const {user, isAuthenticated} = storeToRefs(useAuthStore()); 

    function ActivePrime(){

    }
</script>
<template>
<div class="content">

    <div class="tarif-premium">
        <h2>Премиум доступ &#128142;<span v-if="user?.premium">- Активен</span></h2>
        <p>- Предоставление возможности создавать до 5 групп чатов</p>
        <p>- Неограниченные возможности создавать новые контакты в сутки (у Махнем 10 контактов в сутки)</p>
        <p>- Добаление больше 5 фото в аккаунт + видео (в дальнейшем доработаем чтобы на простых аккаунтах была закрыта эта возможность)</p>
        <p>- Возможность размещения до 10 объявлений в профиле (в обычном сделать в дальнейшем 2 объявления)</p>
        <p>- Занчок Премиум на автарке или имени</p>
        <span>399 руб за 30 дней</span>
        
        <form action="" v-if="!user?.premium" method="post" style="box-shadow: none;border: none;" @submit.prevent="ActivePrime">
          <button class="select-tarif" type="submit">Купить Премиум</button>
          <input name="summa" type="number" value="399" style="visibility: hidden;" />
     
        </form>

        <p v-if="user?.premium">Премиум Подписка Уже Активирована</p>

        <p v-if="!isAuthenticated">Чтобы купить, необходимо авторизироваться и подтвердить телефон</p>
        </div>



</div>
</template>
<style scoped>
.tarif-premium {
    display: flex;
    flex-direction: column;
    margin: 49px auto 125px auto;
    max-width: 100%;
    padding: 25px 25px 25px;
    background: #f0faf9;
    border-radius: 15px;
}

.tarif-premium h2 {
    font-size: 35px;
    margin: 0px 0px 25px 0px;
}

.tarif-premium p {
    margin: 0px 0px 15px 0px;
}

.tarif-premium span {
    font-size: 25px;
    font-weight: 700;
    margin: 25px 0px 25px 0px;
}

button {
    border: none;
    cursor: pointer;
    background-color: #2963d6;
    font-size: 15px;
    color: #FFFFFF;
    font-size: 17px;
    padding: 15px 25px 15px 25px;
    border-radius: 115px;
}


form{
    padding: 0px 0px 0px 0px;
    margin: 0px 0px 25px 0px;
    background-color: inherit;
    display: flex;

    p{
        font-size: 17px;
    }
}

p{
    font-size: 14px;
}
</style>