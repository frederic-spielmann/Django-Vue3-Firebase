<script setup>
import { useUsersStore } from '@/stores/users.store'
import Button from "@/components/forms/button.vue"
import FormSection from "@/components/forms/form-section.vue"

const userStore = useUsersStore()

const submit = function() {
  userStore.deleteUser()
}

</script>

<template>
    <div>
          <FormSection @submitted="submit">
            <template #form>
                <Button style="background-color: #e74c3c" type="submit" :disabled="userStore.loadingUser">
                    Delete Account
                </Button>
            </template>
          </FormSection>
    </div>
</template>