<template>

<div ref="whatSearhLayout" class="what-search-layout">
<div class="what-search-content">
  <span style="font-weight: 700;">Я ищу:</span> <span class="ff2" @click="OpenWhat()" style="color: #999999;
    margin: 0px 0px 0px 9px;font-size: 700!IMPORTANT;">{{ what }}</span> <span></span>
</div>
<div :class="addClass" class="what-navigation">
<div class="ff" ref="ff">
<select v-model="what" class="what-search">
<!-- <option value="Я ищу" selected disabled>Я ищу</option> -->
<option value="Мужчину">Мужчину</option>
<option value="Женжину">Женщину</option>
<option value="Семью">Семью</option>
<option value="Не важно" selected>Не важно</option>
</select>
<p>Возраст</p>
<div class="whatAge">
  <input type="text" placeholder="от"> <input type="text" placeholder="до">
</div>
<button ref="buttonSave" class="save" @click.prevent="saveWhat">Сохранить</button>
</div>
</div>
</div>


</template>

<script lang="ts" setup>
const whatSearhLayout = ref()
const addClass = ref('')
const what = ref('Не важно')

function OpenWhat(){
  addClass.value = 'active'
}

const WhatNavigation = ref()


function outsideClick(event){
  const ff = document.querySelector('.ff')
  const ff2 = document.querySelector('.ff2')
  if (!ff.contains(event.target) && !ff2.contains(event.target)){
    addClass.value = '';
    console.log(ff)
  }
}


function saveWhat(event) {
  const buttonSave = document.querySelector('.save');
  if (buttonSave && buttonSave.contains(event.target)) {
    addClass.value = '';
    console.log(buttonSave);
  }
}

onMounted(() => {
  document.addEventListener('click', outsideClick);
})

const people = ['Мужчину', 'Женщину', 'Пару', 'Семью', 'Не важно']
const selected = ref()
const query = ref('')
</script>

<style scoped>
.ff{
  display: flex;
  flex-direction: column;
  width: 95%;
  height: max-content;
  margin: 0 auto;
}
.whatAge{
  display: flex;
  justify-content: space-between;
  width: 100%;
  height: max-content;
}.whatAge input{
  width: 47%;
  border: 1px solid #00000025;
  border-radius: 9px;
  padding: 9px 15px 9px 15px;
  font-weight: 500;
}
p{
  height: 25px!IMPORTANT;
  margin: 15px 0px 15px 0px!IMPORTANT;
  font-size: 17px!IMPORTANT;
  font-weight: 700;
}
.what-search-content{display: flex;justify-content: flex-start;align-items: center;}

.what-search-layout{display: flex;flex-direction: column;width: 100%;border-right: 1px solid #FFFFFF;position: relative;padding: 0px 0px 0px 25px;cursor: pointer;font-weight: 700;flex-direction: row;}

.what-navigation{position: absolute;
width: 350px;
height: max-content;
background-color: #FFFFFF;
border-radius: 15px;
padding: 25px 25px 25px 25px;
visibility: hidden;
z-index: 145;
top: 35px;
box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
border: 1px solid #00000025;
z-index: 147;
}
.what-navigation button{
  width: 100%;
  background-color: #000000;
  padding: 9px 15px 9px 15px;
  border-radius: 9px;
  color: #FFFFFF;
  margin: 15px 0px 0px 0px;
}
.active{
  visibility: visible;
}
.what-search {
  border-bottom: 1px solid #00000025;
  width: 100% !important;
  display: flex;
  box-shadow: none !important;
  padding: 9px 15px 9px 0px;
  font-size: 17px !important;
  outline: none;
  margin: 0px 0px 0px 0px;
  border-radius: 0px;
  -webkit-appearance: none;
  cursor: pointer;
}.what-search:hover select{
  opacity: 0.9;
}
.what-search label{
  color: white;
}
.what-search option{
  font-size: 15px!IMPORTANT;
  padding: 5px;
  margin: 15px 0px 0px 0px;
}
.what-search-layout::before{
    content: "asd";
    content: "💙";
    display: flex;
    align-items: center;
    position: relative;
    margin: 0px 9px 0px 0px;
  }

@media(max-width: 770px){
  .what-search-layout{
    width: calc(100% - 30px);
    padding: 15px 0px 15px 0px;
    border-bottom: 1px solid #00000025;
    border-right: none;
    display: flex;
    flex-direction: row;
  }
  .what-navigation{
    width: calc(100% + 39px);
    left: -19px;
    padding: 9px 9px 9px 9px;
    top: 47px;
  }
  .what-navigation p{
    text-align: left;
  }
}
.what-search{
  padding: 10px 10px  10px 10px;
  border-radius: 9px;
  border: 1px solid #00000025;
}
</style>
