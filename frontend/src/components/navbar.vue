<script setup>
import { RouterLink } from 'vue-router'
import { useUsersStore } from '@/stores/users.store'

const userStore = useUsersStore()
</script>

<template>
    <nav v-if="!userStore.loadingSession" class="navbar navbar-expand navbar-dark bg-dark">
        <div v-if="userStore.userData" class="navbar-nav">
            <router-link to="/" class="nav-item nav-link">Home</router-link>
            <router-link to="/movies" class="nav-item nav-link">Movies</router-link>
            <router-link to="/profile" class="nav-item nav-link">My Profile</router-link>
            <a @click="userStore.logout" onmouseover="" style="cursor: pointer;" class="nav-item nav-link">Logout</a>
        </div>
        <div v-else class="navbar-nav">
            <router-link to="/login" class="nav-item nav-link">Login</router-link>
            <router-link to="/register" class="nav-item nav-link">Register</router-link>
        </div>
    </nav>
    <div v-else>
      Loading...
    </div>
</template>