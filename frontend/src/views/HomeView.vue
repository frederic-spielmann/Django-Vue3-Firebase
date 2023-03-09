<script setup>
import { useUsersStore } from '@/stores/users.store'

const userStore = useUsersStore()
</script>

<template>
    <div>
      <h1>Home</h1>
      <p>You're logged in Django/Vue3/Firebase !</p>
      <p>Display Name : {{userStore.userData?.displayName}}</p>
      <p>Email : {{userStore.userData?.email}}</p>
      <p>UID : {{userStore.userData?.uid}}</p>
      <img alt="Profile Photo" v-if="userStore.userData?.photoURL" :src="userStore.userData?.photoURL">
      <p v-else> No profile photo</p>
    </div>
</template>