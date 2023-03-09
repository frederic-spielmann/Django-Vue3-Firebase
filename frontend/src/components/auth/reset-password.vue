<script setup>
import { ref } from 'vue'
import { useUsersStore } from '@/stores/users.store'
import Label from "@/components/forms/label.vue"
import Input from "@/components/forms/input.vue"
import Button from "@/components/forms/button.vue"
import FormSection from "@/components/forms/form-section.vue"

const userStore = useUsersStore()
const email = ref(null)

const submit = async() => {
    if(!email.value){
        return alert('Fill the field')
    }
    await userStore.resetPassword(email.value)
}
</script>

<template>
    <FormSection @submitted="submit">
      <template #title>
      Reset Password
      </template>
      <template #form>
            <Label for="email" value="Email" />
            <Input id="email" type="email" v-model.trim="email" placeholder="Enter Email" required />
       <div class="flex items-center justify-end">
        <Button type="submit">
            Send a reset password
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