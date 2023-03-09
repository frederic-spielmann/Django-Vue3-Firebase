<script setup>
import FormSection from "../forms/form-section.vue";
import Label from "@/components/forms/label.vue"
import Input from "@/components/forms/input.vue"
import Button from "@/components/forms/button.vue"
import { useMoviesStore } from "@/stores/movies.store"
import { ref } from "vue";
import { useRoute } from "vue-router";
import Spinner from "@/components/spinner.vue"

const moviesStore = useMoviesStore()
const route = useRoute()
const movie_id = route.params.id

let title_page = 'Add Movie'
let button_name = ' Create'
let title = ref(null)
let description = ref(null)
let category = ref('None')

if(movie_id) {
  title_page = 'Edit Movie #' + movie_id
  button_name = 'Update'
  moviesStore.getById(movie_id).then(() => {
  title.value = moviesStore.movie.title
  description.value = moviesStore.movie.description
  category.value = moviesStore.movie.category
  })
}

const submit = async() => {
  try {
    if(movie_id) {
      await moviesStore.update(movie_id, title.value, category.value, description.value)
    }
    else {
      await moviesStore.create(title.value, category.value, description.value)
    }
  } catch (error) {
    alert(error)
  }

}
</script>
<template>
  <div v-if="!moviesStore.movie.loading">
    <FormSection @submitted="submit">
      <template #title>
      {{ title_page }}
      </template>
      <template #form>
            <Label for="title" value="Title" />
            <Input id="title" type="text" v-model.trim="title" placeholder="Enter title" required />
            <Label for="description" value="Description" />
            <Input id="description" type="text" v-model.trim="description" placeholder="Enter Description" />
            <Label for="category" value="Category" /><br />
            <select name="category" v-model="category" class="list">
              <option disabled value="None">Please select one</option>
              <option value="Cartoon">Cartoon</option>
              <option value="Documentary">Documentary</option>
              <option value="Action">Action</option>
            </select>
          <div class="flex items-center justify-end">
              <Button type="submit" :disabled="moviesStore.load">
                  {{ button_name }}
              </Button>
          </div>
      </template>
    </FormSection>
  </div>
  <div v-else class="center">
    <Spinner />
  </div>
</template>
<style scoped>
.list {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #202020;
  background-color: #222;
  color: #ccc;
}
.center {
  margin: auto;
  width: 50%;
}
</style>