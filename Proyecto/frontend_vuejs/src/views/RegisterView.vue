<template>
    <div class="first-layer">
      <h1>Boxy</h1>
      <div class="second-layer">
        <div class="title">
          <p>Registro</p>
        </div>
        <div class="data">
          
            <div class="nombre">
                <label>Nombre</label>
                <input v-model="nombre" type="text"/>
            </div>

            <div class="rol">
                <label>Rol</label>
                <div>
                    <input type="radio" id="Administrador" value="Administrador" v-model="rol"/>
                    <label for="Administrador">Administrador</label>
                </div>
                
                <div>
                    <input type="radio" id="Usuario" value="Usuario" v-model="rol" />
                    <label for="Usuario">Usuario</label>
                </div>
            </div>

            <div class="organizacion">
                <label>Organizacion</label>
                <input v-model="organizacion" type="text">
            </div>

            <div class="email">
                <label >Correo electronico</label>
                <input v-model="correo_electronico" type="email"/>
            </div>
    
            <div class="password">
                <label >Contraseña</label>
                <input v-model="password" type="password"/>
            </div>
    
            <button @click="register">Registrarse</button>
            <p>Volver a <router-link :to="{name: 'login'}">inicio de sesion</router-link></p>
        </div>
      </div>
    </div>
    
  </template>
  
  <script setup>
    import { ref } from 'vue'
    import RegisterService from '../services/RegisterService'
    import router from '@/router'

    let nombre = ref("")
    let rol = ref("Administrador")
    let organizacion = ref("")
    let correo_electronico = ref("")
    let password = ref("")

    const register = async () => {
      const registerUser = new RegisterService()
      const success = await registerUser.register(nombre.value, rol.value, organizacion.value, correo_electronico.value, password.value) 
      if(success) {
        alert("Registro exitoso")
        router.push({name: 'login'})
      } else {
        alert("Registro fallido. Vuelva a intentarlo")
        nombre.value = ""
        rol.value = "Administrador"
        organizacion.value = ""
        correo_electronico.value = ""
        password.value = ""
      }
    } 

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
      width: 400px;
      height: 600px;
    }
  
    .data {
      display: flex;
      flex-direction: column;
      align-items: center;   
      justify-content: center;
      gap: 25px;
      height: 90%;
      width: 100%;  
  
      p {
        text-align: center;
        margin-top: 5px;
        margin-bottom: 5px;
      }
    }
  
    .email, .password, .nombre, .rol, .nombre, .organizacion {
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
      height: 10%;
      font-size: 30px;
      border-bottom: 2px solid $primary-blue;
    }
  
  </style>
  