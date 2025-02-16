<script setup>
const inputWhere = ref()
const inputWhere1 = ref()
const menu = ref(null);
const menu1 = ref(null);

// изначально класс active отсутствует
const wathClass = ref('')

// добавляем класс active по клику
function addInputWhere(){
  wathClass.value = 'active'
}

function saveWhere(){
  inputWhere.value = inputWhere1.value
  wathClass.value = ''
}

const handleClickOutside = (event) => {
      if (!menu1.value.contains(event.target) && !menu.value.contains(event.target)) {
        wathClass.value = ''
      }
    };

onMounted(() => {
      document.addEventListener('click', handleClickOutside);
});



</script>
<template>
<div class="where-layout">
    <div ref="menu" :class="wathClass" class="where-content">
        <input type="text" placeholder="Город" v-model="inputWhere1">
        <button @click.prevent="saveWhere()">Сохранить</button>
    </div>
    <input ref="menu1" type="text" v-model="inputWhere" placeholder="Откуда?" @click="addInputWhere()" readonly style="outline: none;cursor: pointer;"/>
</div>
</template>
<style scoped>
::-webkit-input-placeholder { /* WebKit, Blink, Edge */
    color:    #000000;
}
:-moz-placeholder { /* Mozilla Firefox 4 to 18 */
   color:    #000000;
   opacity:  1;
}
::-moz-placeholder { /* Mozilla Firefox 19+ */
   color:    #000000;
   opacity:  1;
}
:-ms-input-placeholder { /* Internet Explorer 10-11 */
   color:    #000000;
}
::-ms-input-placeholder { /* Microsoft Edge */
   color:    #000000;
}
::placeholder { /* Most modern browsers support this now. */
   color:    #000000;
}
.where-layout button{
  width: 100%;
  background-color: #000;
  color: #FFFFFF;
  padding: 9px 9px 9px 9px;
  border-radius: 9px;
  margin: 0px 0px 0px 0px;
}
.where-layout button:hover{
    background-color: #252525;
}
.where-layout button:focus{
    background-color: #00c7bb;
}
.where-layout{
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 100%;
  padding: 0px 0px 0px 25px;
  border-right: 1px solid #d9d9d9;
}
.where-content{
  visibility: hidden;
  width: 350px;
  max-width: 400px;
  position: absolute;
  height: max-content;
  border-radius: 15px;
  /* transition: all 0.3s; */
  top: 35px;
  border: 1px solid #00000025;
  z-index: 999;
  background-color: #FFFFFF;
  box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  padding: 25px 25px 25px 25px;
}.where-content input {
  padding: 9px 15px 9px 15px;
  border-radius: 9px;
  border: 1px solid #00000025;
  width: 100%;
  margin: 0px 0px 25px 0px;
  font-weight: 700;
}
.active{
  visibility: visible;
}

@media (max-width: 770px){
  .where-layout{
    width: calc(100% - 30px);
    padding: 15px 0px 15px 0px;
    border-bottom: 1px solid #00000025;
    border-right: none;
  }.where-content{
    width: calc(100% + 39px);
    left: -19px;
    top: 49px;
    padding: 9px;
    max-width: calc(100% + 35px);
  }.where-content button{
    margin: 0px 0px 9px 0px;
  }
  .where-content input{
    margin: 0px 0px 9px 0px;
  }
}
</style>