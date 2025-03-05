<template>

  <router-view />

</template>

<script setup>

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
