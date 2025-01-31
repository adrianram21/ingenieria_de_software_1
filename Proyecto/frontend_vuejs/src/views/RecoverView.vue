<template>
    <div class="first-layer">
      <h1>Boxy</h1>
      <div class="second-layer">
        <div class="data">
          <div class="email">
            <label >Ingresa tu correo electronico </label>
            <input v-model="correo_electronico" type="email"/>
          </div>
          
          <div class="buttons">
            <router-link :to="{name: 'login'}"><button>Volver</button></router-link>
            <button>Enviar</button> 
          </div>

        </div>
      </div>
    </div>
    
  </template>
  
  <script setup>
    import { ref } from 'vue'

    let correo_electronico = ref("")
  
  </script>
  
  <style scoped lang="scss">
  
    h1 {
      font-family: "Verdana";
      color: $primary-white;
      margin-bottom: 10px;
    }
    button {
      background-color: $primary-blue;
      color: $primary-white;
      border: 1px solid $primary-blue;
      border-radius: 10px;
      width: 100px;
      height: 25px;
    }

    .buttons {
        display: flex;
        gap: 10px;
    }

    .router-link:hover {
        cursor: pointer;
    }
  
    button:hover {
      cursor: pointer;
    }
  
    input {
      color: $neutral-black;
      font-family: "Verdana";
    }
  
    label {
      font-size: 18px;
      color: $neutral-black;
      font-family: "Verdana";
    }
  
    p {
      margin: 5%;
      color: $neutral-black;
      font-family: "Verdana";
    }
    
    .first-layer {
      display: flex;
      justify-content: center;
      align-items: center;  
      flex-direction: column;   
      height: 100vh;
      background: linear-gradient(135deg, $primary-blue, $primary-white);
    } 
  
    .second-layer {
      background-color: $primary-white;
      border: 2px solid $primary-blue;
      border-radius: 30px;
      width: 300px;
      height: 150px;
    }
  
    .data {
      display: flex;
      flex-direction: column;
      align-items: center;   
      justify-content: center;
      gap: 25px;
      height: 100%;
      width: 100%;  
  
      p {
        text-align: center;
        margin-top: 5px;
        margin-bottom: 5px;
      }
    }
  
    .email, .password {
      margin: 0px;
      display: flex;
      flex-direction: column;
      align-items: center;   
      justify-content: center;
      gap: 5px;
    }
  
  
  
    .title {
      display: flex;
      justify-content: center;
      align-items: center; 
      height: 20%;
      font-size: 30px;
      border-bottom: 2px solid $primary-blue;
    }
  
  </style>
  