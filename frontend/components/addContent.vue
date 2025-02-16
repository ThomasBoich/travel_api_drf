<template>
  <UDropdown :items="items" :popper="{ placement: 'bottom-start' }">
    <UButton
      color="white"
      label="Создать"
      trailing-icon="i-heroicons-chevron-down-20-solid"
    />
  </UDropdown>
  <UModal v-model="isOpen" style="z-index: 999999;">
      <div class="p-4 create-travel-layer">
        <h1>Создать путешествие</h1>
        <form action="" method="post" class="create-travel-form">
          <div class="form-user-info">
          <div>
            <label for="gender">Я</label>
          <select name="gender" id="gender">
            <option value="Мужчина">Мужчина</option>
            <option value="Женщина">Женщина</option>
          </select>
          </div>
          <div>
            <label for="search">Ищу</label>
            <select name="search" id="search">
              <option value="Семейную пару">Семейную пару</option>
              <option value="Женщину">Женщину</option>
            </select>
          </div>
          <div style="width: 100%;">
            <label for="">Откуда едем</label>
            <input type="text" placeholder="Новосибирск">
          </div>
        </div>
        <div class="where">
          <label for="" style="border-bottom: 1px solid #E1E1E1;padding: 0px 0px 9px 0px;margin: 0px 0px 15px 0px;">Куда</label>
          <div class="where-content">
            <div>
              <input type="checkbox" name="abh" id="abh">
              <label for="abh">Абхазия</label>
            </div>
            <div>
              <input type="checkbox" name="arm" id="arm">
              <label for="arm">Армения</label>
            </div>
            <div>
              <input type="checkbox" name="abh" id="abh">
              <label for="abh">Абхазия</label>
            </div>
            <div>
              <input type="checkbox" name="arm" id="arm">
              <label for="arm">Армения</label>
            </div>
            <div>
              <input type="checkbox" name="abh" id="abh">
              <label for="abh">Абхазия</label>
            </div>
            <div>
              <input type="checkbox" name="arm" id="arm">
              <label for="arm">Армения</label>
            </div>
          </div>
        </div>
        <div class="form-city">
          <label for="">Город, курорт</label>
          <input type="text" placeholder="Новосибирск">
        </div>
        <div class="form-date">
          <div>
            <label for="">Когда</label>
            <input type="date" id="start" name="trip-start" value="2024-07-22" min="2018-01-01" max="3999-12-31" />
          </div>
          <div>
            <label for="">Кол-во дней</label>
            <input type="number" placeholder="15" style="max-width: 70px;text-align: center;">
          </div>
          <div style="flex-direction: row;align-items: center;margin: 25px 0px 0px 0px;">
            <label for="" style="margin: 0px 15px 0px 0px;">Уже отдыхаю</label>
            <UToggle v-model="selected" />
          </div>
        </div>
        <textarea name="" id="" cols="15" rows="2" placeholder="Опишите ваше путешествие ....."></textarea>
        <button>Опубликовать</button>
        </form>
        <Placeholder class="h-48" />
      </div>
    </UModal>
</template>

<script lang="ts" setup>
const isOpen = ref(false)
const selected = ref(false)
const items = [
  // [
  //   {
  //     label: "Profile",
  //     avatar: {
  //       src: "https://avatars.githubusercontent.com/u/739984?v=4",
  //     },
  //   },
  // ],
  [
    {
      label: "Путешествие",
      icon: "i-heroicons-pencil-square-20-solid",
      shortcuts: ["E"],
      click: () => {
        isOpen.value = true
      },
      disabled: false,
    },
    // {
    //   label: "Запись в блоге",
    //   icon: "i-heroicons-document-duplicate-20-solid",
    //   shortcuts: ["D"],
    //   disabled: false,
    // },
  ],
  [
    // {
    //   label: "Archive",
    //   icon: "i-heroicons-archive-box-20-solid",
    // },
    {
      label: "Выйти из системы",
      icon: "i-heroicons-arrow-right-circle-20-solid",
      disabled: false,
    },
  ],
  // [
  //   {
  //     label: "Delete",
  //     icon: "i-heroicons-trash-20-solid",
  //     shortcuts: ["⌘", "D"],
  //   },
  // ],
];
</script>

<style scoped>

.form-date{
  display: flex;
  justify-content: flex-start;
  margin: 0px 0px 15px 0px;
  align-items: center;
}
.form-date div{
  display: flex;
  flex-direction: column;
  margin: 0px 15px 0px 0px;
}
.form-date input{
  width: 100%;
  padding: 10px;
  border: 1px solid #E1E1E1;
  border-radius: 5px;
  margin: 0px 0px 0px 0px;
}
.form-date label{
  margin: 0px 0px 5px 0px;
  font-weight: 700;
}
.form-city{
  display: flex;
  margin: 15px 0px 15px 0px;
  flex-direction: column;
}.form-city label{
  margin: 0px 0px 5px 0px;
  font-weight: 700;
}
.form-city input{
  width: 100%;
  padding: 10px;
  border: 1px solid #E1E1E1;
  border-radius: 5px;
}
form textarea{
  width: 100%;
  padding: 10px;
  border: 1px solid #E1E1E1;
  border-radius: 5px;
  margin: 0px 0px 15px 0px;
}
form .where{
  width: 100%;
  display: flex;
  flex-direction: column;
  background-color: #F5F5F5;
  border-radius: 9px;
  padding: 15px 15px 15px 15px!important;
  height: auto;
}.where label{
  font-weight: 700;
  font-weight: 700;
}
.where-content{
  display: grid;
  grid-auto-rows: auto;
  grid-column: auto;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr; /* Равномерное разделение на 3 колонки */
  grid-gap: 10px; /* Пространство между элементами */
}.where-content label{
  font-weight: 500;
  margin: 0px 0px 0px 5px;
}
form{
  width: 100%;
  display: block;
  border: none;
  border-radius: 0px;
  box-shadow: none;
  overflow: auto;
  padding: 0px 0px 0px 0px;
}
form button{
  background-color: #000;
  color: #FFFFFF;
  border-radius: 50px;
  text-align: center;
  margin: 0 auto;
  justify-content: center;
  padding: 9px 15px 9px 15px;
}
.form-user-info{
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}
form label{
  font-size: 17px;
  font-weight: 500;
  width: 100%;
  clear: both;
  content: "";
  margin: 0px 0px 5px 0px;
  font-weight: 700;
}.form-user-info div{
  width: 47%;
  display: flex;
  flex-direction: column;
  margin: 0px 0px 15px 0px;
}.form-user-info div select{
  width: 100%;
  padding: 10px;
  border: 1px solid #E1E1E1;
  border-radius: 5px;
}.form-user-info input{
  width: 100%;
  padding: 10px;
  border: 1px solid #E1E1E1;
  border-radius: 5px;
}.form-user-info input:focus{
  outline: none;
  border: 1px solid #000;
}.form-user-info input:focus-visible{
  outline: none;
  border: 1px solid #000;
}
.create-travel-layer{}
.create-travel-layer h1{
  font-size: 35px;
  font-weight: 700;
  text-align: center;
  border-bottom: 1px solid #E1E1E1;
  padding: 15px 0px 25px 0px;
  margin: 0px 0px 15px 0px;
}
button {
  border: none;
  font-size: 17px;
  --tw-ring-opacity: 0;
  box-shadow: none;
  border-right: 1px solid #d6d6d6 !important;
  padding: 0px 25px 0px 0px;
  border-radius: 0px;
}
</style>
