<script setup>

</script>
<template>
    <div class="auth_layout" style="display: flex;flex-direction: column;justify-content: center;align-items: center;height: 100dvh">
        <div class="content">
            <slot></slot>
        </div>
    </div>
</template>
<style scoped>
    .auth_layout{
        /* background-color: #F1F1F1; */
        min-width: 100%;
        min-height: 100dvh;
    }
</style>