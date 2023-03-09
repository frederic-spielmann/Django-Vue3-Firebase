<script setup>
import { RouterView } from 'vue-router'
import Navbar from '@/components/navbar.vue'
</script>

<template>
    <div class="app-container">
        <Navbar />
<!--        <Alert />-->
        <div class="container pt-4 pb-4">
            <router-view />
        </div>
    </div>
</template>