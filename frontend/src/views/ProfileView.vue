<script setup>
import { ref } from 'vue'
import { useUsersStore } from '@/stores/users.store'
import Label from "@/components/forms/label.vue"
import Input from "@/components/forms/input.vue"
import Button from "@/components/forms/button.vue"
import FormSection from "@/components/forms/form-section.vue"
import DeleteAccount from "@/components/auth/deleteAccount.vue";

const userStore = useUsersStore()
const displayName = ref(userStore.userData?.displayName)
const photoURL = ref(userStore.userData?.photoURL)
const email = ref(userStore.userData?.email)
const password = ref(null)
const password_verif = ref(null)

const submit = async() => {
  await userStore.updateUser(displayName.value, photoURL.value, email.value, password.value)
}

</script>

<template>
  <FormSection @submitted="submit">
    <template #title>
    Profile
    </template>
    <template #form>
      <Label for="displayName " value="Display Name" />
      <Input id="displayName " type="text" v-model.trim="displayName" placeholder="Enter Display Name"/>

      <Label for="photoURL " value="Photo URL" />
      <Input id="photoURL " type="text" v-model.trim="photoURL" placeholder="Enter Photo URL" />

      <Label for="email" value="Change Email" />
      <Input id="email" type="email" v-model.trim="email" placeholder="Enter Email" />

      <Label for="password" value="Change Password" />
      <Input type="password" v-model.trim="password" placeholder="Type new Password" />

      <Label for="password_verif" value="Verify new Password" />
      <Input type="password" v-model.trim="password_verif" placeholder="Retype new Password" />

      <div class="flex items-center justify-end">
        <Button type="submit" :disabled="userStore.loadingUser">
            Save
        </Button>
      </div>
    </template>
  </FormSection>
  <DeleteAccount />
</template>

<style scoped>
hr {
  border: none;
  border-top: 2px dotted gray;
  margin-top: 5px;
  margin-bottom: 5px;
}
</style>