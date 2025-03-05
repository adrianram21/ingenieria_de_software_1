<template>
  <div class="first-layer">
    <h1>Registro de movimientos</h1>
    <router-link :to="{name: 'main'}"><button class="modify">Volver al menu principal</button></router-link>
    <br>
    <div class="select">
      <label for="producto">Selecciona un producto:</label>
      <select id="producto" v-model="productoSeleccionado">
        <option v-for="producto in productos" :key="producto.id" :value="producto">
          {{ producto.nombre }}
        </option>
      </select>
      <label>Movimiento:</label>
      <select v-model="tipo_movimiento">
        <option value="entrada">Entrada</option>
        <option value="salida">Salida</option>
      </select>

      <label>Fecha:</label>
      <input v-model="fecha" type="date" />

      <label>Cantidad:</label>
      <input v-model="cantidad" type="number" />
      
      <label>Descripcion:</label>
      <textarea id="descripcion" v-model="descripcion" type="text" />

      <div class="buttons">
        <button class="modify" @click="updateProduct">Confirmar</button>
      </div>
    </div>

    
  </div>
  
</template>

<script setup>
import { useProductsStore } from '@/store/Products'
import { useLoginStore } from '@/store/Login'
import { onMounted, ref } from 'vue'
import router from '@/router'

const userStore = useLoginStore()
const ProductsStore = useProductsStore()
const productos = ref([])
const productoSeleccionado = ref(null)
const tipo_movimiento = ref(null)
const fecha = ref(null)
const descripcion = ref(null)
const cantidad = ref(null)

onMounted(() => {
    show()
  })


const show = async () => {
    const refreshed = userStore.refreshToken()
    if (refreshed) {
      await ProductsStore.fetchProductos(userStore.id_organizacion, userStore.accessJWT)
      productos.value = ProductsStore.productos
    } 
    else {
      userStore.logout()
      router.push({name: 'login'})
    }
  }
</script>

<style scoped lang="scss">
  select {
    height: 30px;
    width: 200px;
    border-radius: 20px;
    border: 2px solid $primary-blue;
  }

  #descripcion {
    height: 140px; 
    width: 250px; 
    border-radius: 20px;
    border: 2px solid $primary-blue;
  }

  input {
    height: 20px;
    width: 200px;
    border-radius: 20px;
    border: 2px solid $primary-blue;
  }

  .modify {
    margin: 0;
    background-color: $primary-blue;
    color: $primary-white;
    border: 3px solid $primary-blue;
    border-radius: 10px;
    width: 180px;
    height: 30px;
    font-weight: bold;
  }

  .modify:hover {
    cursor: pointer;
    background-color: $primary-white;
    color: $primary-blue;
    font-weight: bold;
  }

  .select {
    background-color: $primary-white;
    border: 2px solid $primary-blue;
    display: flex;
    border-radius: 30px;
    width: 300px;
    height: 500px;
    align-items: center;
    flex-direction: column;
    gap: 10px;
    padding-top:30px
  }

  .first-layer {
    display: flex;
    align-items: center;  
    flex-direction: column;   
    height: 100%;
    background: linear-gradient(135deg, $primary-blue, $primary-white);
    gap: 20px;
    min-height: 100vh;
  } 

  h1 {
    font-family: "Verdana";
    color: $primary-white;
    margin-bottom: 10px;
  }
</style>