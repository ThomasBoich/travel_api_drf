<template>
  <div class="aboutUser aboutUser" style="border-bottom: 1px solid #ebebeb;margin: 15px 0px 15px 0px!IMPORTANT;padding: 0px 0px 15px 0px;">
      <span v-for="about in abouts.habits" :key="about.id"><img :src="about.image" alt="">{{ about.name }}</span>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({
  abouts: {
    type: Array,
  },
  margin: {
    type: String,
    default: '0px 0px 0px 0px'
}
})
</script>

<style scoped>
    .aboutUser{display: flex;flex-wrap: wrap;gap: 15px;}
    .aboutUser span{
        border-radius: 50px;
        border:1px solid #EBEBEB;
        padding: 9px 15px 9px 15px;
        min-width: max-content;width: max-content;
        display: flex;
        align-items: center;
        font-size: 15px;
        font-weight: 500;
    }
    .aboutUser span img{
        margin: 0px 5px 0px 0px;
        width: auto;
        height: 15px;
    }

    @media (max-width: 770px){
    .index-friends-layout{
        margin: 0px auto 35px;
    }
    .index-friends-title{
        width: calc(100% -30px);
        flex-direction: column;
        align-items: flex-start;
        padding: 0px 0px 0px 15px;
    }
    .index-friends-title h2{
        font-size: 5vw;
    }
    .aboutUser{
        overflow: hidden;
        overflow-x: auto;
        display: grid;
        grid-template-columns: repeat(7, 1fr);
    grid-template-rows: repeat(2, auto);
    padding: 0px 15px 0px 15px;
    }
    .index-friends-user{
        margin: 0px 15px 0px 0px;
    }
    .index-friends-user img{
        max-width: 135px;
    }.index-friends-user p{
        font-size: 12px;
        padding: 0px;
        width: 100%;
        margin: 0px 0px 0px 0px;
    }
    .index-friends-users{
        padding: 0px 15px 0px 15px;
        margin: 0px 0px 35px 0px;
    }
}
</style>