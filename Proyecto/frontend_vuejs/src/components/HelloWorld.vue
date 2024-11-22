<template>
  <div>
    <p v-for="(texto, index) in textos" :key="index">{{ texto.texto }}</p>
  </div>
  
</template>

<script setup>
import axios from 'axios';
import { onBeforeMount } from 'vue';
import { ref } from 'vue';

let textos = ref([])

onBeforeMount(() => {
  getText()
})

const getText = () => {
  axios.get('http://127.0.0.1:8000/inventario/texto/')
    .then(response => {
    textos.value = response.data
  })
    .catch(error => {
      console.log(error)
    });
    
}

</script>

<style scoped>
  div {
    
    width: 200px;
    text-align: left;
  }
</style>
