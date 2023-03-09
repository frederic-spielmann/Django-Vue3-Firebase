<script>
    import { defineComponent } from 'vue'
    import SectionTitle from "@/components/forms/section-title.vue";

    export default defineComponent({
        emits: ['submitted'],

        components: {
            SectionTitle,
        }
    })
</script>

<template>
        <SectionTitle>
            <template #title><slot name="title"></slot></template>
            <template #description><slot name="description"></slot></template>
        </SectionTitle>
        <div>
            <form @submit.prevent="$emit('submitted')">
                <div>
                    <slot name="form"></slot>
                </div>
            </form>
        </div>
</template>

<style scoped>
form {
  border: 1px solid #202020;
  background-color: #161616;
  border-radius: 10px;
  padding: 16px;
  margin: auto;
  width: 400px;
}
</style>