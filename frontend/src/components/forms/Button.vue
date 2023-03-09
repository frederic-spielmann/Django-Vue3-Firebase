<script>
    import { defineComponent } from 'vue'

    export default defineComponent({
        props: {
            type: {
                type: String,
                default: 'submit',
            },
        }
    })
</script>

<template>
    <button :type="type">
        <slot></slot>
    </button>
</template>

<style scoped>
button {
  background-color: #2ecc71;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  border-radius: 5px;
  font-size: 16px;
}

button:hover {
  opacity: 0.8;
}
</style>