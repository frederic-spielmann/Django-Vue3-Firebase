<script setup>
import { ref } from 'vue'
import { useUsersStore } from '@/stores/users.store'
import Label from "@/components/forms/label.vue"
import Input from "@/components/forms/input.vue"
import Button from "@/components/forms/button.vue"
import FormSection from "@/components/forms/form-section.vue"

const userStore = useUsersStore()
const email = ref(null)
const password = ref(null)

const submit = async() => {
    if(!email.value || password.value.length < 6){
        return alert('Fill the fields')
    }
    await userStore.login(email.value, password.value)
}

</script>

<template>
    <FormSection @submitted="submit">
      <template #title>
      Login
      </template>
      <template #form>
            <Label for="email" value="Email" />
            <Input id="email" type="email" v-model.trim="email" placeholder="Enter Email" required />

            <Label for="password" value="Password" />
            <Input type="password" v-model.trim="password" placeholder="Enter Password" required />

          <div class="flex items-center justify-end">
            <router-link to="/reset-password" class="right">Reset password ?</router-link>
              <Button type="submit" :disabled="userStore.loadingUser">
                  Log in
              </Button>
        </div>
      </template>
    </FormSection>
</template>

<style scoped>
.right {
  float: right;
}
</style>