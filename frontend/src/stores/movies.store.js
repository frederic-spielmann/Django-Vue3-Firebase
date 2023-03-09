import { defineStore } from 'pinia'
import { cfetch } from "../utils/cfetch"
import router from "@/router"

const endpoint = "movies/"

export const useMoviesStore = defineStore({
    id: 'movies',
    state: () => ({
        movies: {
            loading: false
        },
        movie: {
            loading: false
        },
    }),
    actions: {
        async getAll() {
            this.movies = { loading: true }
            try {
                await cfetch.get(endpoint).then(data => { this.movies = data.results })
            } catch (error) {
                this.movies = { error }
            }
        },
        async getById(id) {
            try {
                this.movie = { loading: true }
                await cfetch.get(endpoint + `${id}`).then(data => { this.movie = data })
            } catch (error) {
                this.movie = { error }
            }
            finally {
                this.movie.loading = false
            }
        },
        async update(id, title, category, description) {
            await cfetch.put(endpoint + id + "/update/", {title, category, description})
            alert("Movie #" + id + " successfully updated!")
            router.push("/movies")
        },
        async create(title, category, description) {
            await cfetch.post(endpoint, {title, category, description})
            alert("Movie successfully created!")
            router.push("/movies")
        },

        async delete(id) {
            this.movies.find(x => x.id === id).isDeleting = true
            await cfetch.delete(endpoint + `${id}` + "/delete/")
            this.movies = this.movies.filter(x => x.id !== id)
        }
    }
})
