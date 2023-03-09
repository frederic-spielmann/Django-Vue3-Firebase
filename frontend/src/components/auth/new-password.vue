<script setup>
const props = defineProps({
  oobCode: String
})
import { ref } from 'vue'
import { useUsersStore } from '@/stores/users.store'
import Label from "@/components/forms/label.vue"
import Input from "@/components/forms/input.vue"
import Button from "@/components/forms/button.vue"
import FormSection from "@/components/forms/form-section.vue"

const userStore = useUsersStore()
const oobCode = ref(props.oobCode)
const newPassword = ref(null)

const submit = async() => {
    if(!oobCode.value || newPassword.value.length < 6){
        return alert('Fill the fields')
    }
    await userStore.confirmPasswordReset(oobCode.value, newPassword.value)
}

</script>
<template>
    <FormSection @submitted="submit">
      <template #title>
      Update Password
      </template>
      <p>oobCode = {{ oobCode }}</p>
      <template #form>
            <Label for="oobCode" value="Code" />
            <Input id="oobCode" type="text" v-model.trim="oobCode"  class="greyed" :value=oobCode disabled />

            <Label for="newPassword" value="New Password" />
            <Input type="password" v-model.trim="newPassword" placeholder="Enter your new Password" required />

          <div class="flex items-center justify-end">
              <Button type="submit" :disabled="userStore.loadingUser">
                  Update Password
              </Button>
        </div>
      </template>
    </FormSection>
</template>

<style scoped>
.greyed {
  color: #444;
}
</style>