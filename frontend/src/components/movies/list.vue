<script setup>
import { storeToRefs } from 'pinia'
import { useMoviesStore } from "@/stores/movies.store"

import Spinner from "@/components/spinner.vue"

const moviesStore = useMoviesStore()
const { movies } = storeToRefs(moviesStore)

moviesStore.getAll()

</script>
<template>
    <h1>Movies</h1>
    <router-link to="/movies/add" class="btn btn-sm btn-success mb-2">Add Movie</router-link>
    <table class="table table-striped table-dark">
        <thead>
            <tr>
                <th style="width: 10%">ID</th>
                <th style="width: 30%">Movies</th>
                <th style="width: 30%">Category</th>
                <th style="width: 20%">Created by</th>
                <th style="width: 10%"></th>

            </tr>
        </thead>
        <tbody>
            <template v-if="movies.length">
                <tr v-for="movie in movies" :key="movie.id">
                    <td>{{ movie.id }}</td>
                    <td><router-link :to="`/movies/${movie.id}`">{{ movie.title }}</router-link></td>
                    <td>{{ movie.category }}</td>
                    <td v-if="movie.created_by">{{ movie.created_by.display_name }}</td>
                    <td v-else>Unknown</td>
                    <td style="white-space: nowrap">
                        <router-link :to="`/movies/edit/${movie.id}`" class="btn btn-sm btn-primary mr-1">Edit</router-link>
                        <button @click="moviesStore.delete(movie.id)" class="btn btn-sm btn-danger btn-delete-user" :disabled="movie.isDeleting">
                            <span v-if="movie.isDeleting" class="spinner-border spinner-border-sm"></span>
                            <span v-else>Delete</span>
                        </button>
                    </td>
                </tr>
            </template>
            <tr v-if="movies.loading">
                <td colspan="4" class="text-center">
                    <Spinner />
                </td>
            </tr>
<!--            <tr v-if="movies.error">-->
<!--                <td colspan="4">-->
<!--                    <div class="text-danger">Error loading users: {{movies.error}}</div>-->
<!--                </td>-->
<!--            </tr>-->
        </tbody>
    </table>
</template>