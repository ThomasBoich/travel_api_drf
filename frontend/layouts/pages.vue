<script setup>

</script>
<template>
    <Navigation :is-navigate="true"></Navigation>
    <div class="layout_pages">
        <div class="pages_content">
            <slot></slot>
        </div>
    </div>
    <Footer style="background-color: #F1F1F1;"></Footer>
</template>
<style scoped>
.layout_pages{
    background-color: #F1F1F1;
    /* background-color: #eef0f3;
    background-color: #eef0f2; */
    min-width: 100%;
    min-height: 100dvh;
}
.pages_content{
    width: 95%;
    max-width: 1269px;
    margin: 0 auto;
    padding: 49px 0px 49px 0px;
}
</style>