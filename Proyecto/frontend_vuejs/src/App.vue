<template>
  <div id="app">

    <nav>
      <router-link to="/main">Inicio</router-link> |
      <router-link to="/inventario">Inventario</router-link> |
      <router-link to="/stock_bajo">Stock Bajo</router-link> |
      <router-link to="/admin">Administración</router-link> |
      <button @click="logout">Cerrar Sesión</button>
    </nav>

    <router-view />
  </div>
</template>

<script setup>
import { useLoginStore } from "@/store/Login";
import { useRouter } from "vue-router";

const store = useLoginStore();
const router = useRouter();


const logout = () => {
  store.$reset(); 
  router.push("/login"); 
};
</script>

<style>

body {
  margin: 0;
  font-family: Arial, sans-serif;
}

#app {
  text-align: center;
}

nav {
  background: #2c3e50;
  padding: 10px;
}

nav a {
  color: white;
  text-decoration: none;
  margin: 0 15px;
}

nav a:hover {
  text-decoration: underline;
}

button {
  margin-left: 20px;
  padding: 5px 10px;
  background-color: red;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}
</style>
