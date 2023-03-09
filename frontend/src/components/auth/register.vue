<script setup>
import { ref } from 'vue';
import { useUsersStore } from '@/stores/users.store'
import Label from "@/components/forms/label.vue"
import Input from "@/components/forms/input.vue"
import Button from "@/components/forms/button.vue"
import FormSection from "@/components/forms/form-section.vue"

const userStore = useUsersStore()
const displayName = ref('')
const email = ref('')
const password = ref(null)
const password_verif = ref(null)

const submit = async() => {
    if(!displayName.value) {
        return alert('Type a display name')
    }
    if(!email.value) {
        return alert('Type your email address')
    }
    else if (password.value.length < 8){
      return alert('Password must have at least 8 characters')
    }
    else if (password.value !== password_verif.value) {
      return alert('Passwords do not match')
    }
    await userStore.register(email.value, password.value, displayName.value)
}
</script>

<template>
    <FormSection @submitted="submit">
      <template #title>
      Register
      </template>
      <template #form>
            <Label for="displayName" value="Display Name" />
            <Input id="displayName" type="text" v-model.trim="displayName" placeholder="Enter Display Name" required />

            <Label for="email" value="Email" />
            <Input id="email" type="email" v-model.trim="email" placeholder="Enter Email" required />

            <Label for="password" value="Password" />
            <Input type="password" v-model.trim="password" placeholder="Enter Password" required />

            <Label for="password_verif" value="Password Verification" />
            <Input type="password" v-model.trim="password_verif" placeholder="Enter Password" required />

          <div class="flex items-center justify-end">
              <Button type="submit" :disabled="userStore.loadingUser">
                  Create new account
              </Button>
        </div>
      </template>
    </FormSection>
</template>