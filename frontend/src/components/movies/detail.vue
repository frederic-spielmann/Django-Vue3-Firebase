<script setup>
import { storeToRefs } from 'pinia'
import { useRoute } from 'vue-router'
import { useMoviesStore } from "@/stores/movies.store"
import Spinner from "@/components/spinner.vue"

const route = useRoute()
const movie_id = route.params.id
const moviesStore = useMoviesStore()
const { movie } = storeToRefs(moviesStore)

moviesStore.getById(movie_id)

</script>
<template>
  <div v-if="!movie.loading">
    <h1>{{ movie.title }}</h1>
    <p>Category : {{ movie.category }}</p>
    <p>Created by
      <span v-if="movie.created_by">{{ movie.created_by.display_name }}</span>
      <span v-else>Unknown</span></p>
    <p>Description : {{ movie.description }}</p>
  </div>

  <div v-else>
    <Spinner />
  </div>
</template>