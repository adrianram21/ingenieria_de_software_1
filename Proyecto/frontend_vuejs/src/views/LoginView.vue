<template>
  <div class="first-layer">
    <h1>Boxy</h1>
    <div class="second-layer">
      <div class="title">
        <p>Inicio de sesión</p>
      </div>
      <div class="data">
        
        <div class="email">
          <label >Correo electronico </label>
          <input v-model="correo_electronico" type="email"/>
        </div>

        <div class="password">
          <label >Contraseña </label>
          <input v-model="password" type="password"/>
        </div>

        <button @click="authUser">Iniciar sesión</button>
        <p>¿No tienes una cuenta? Registrate <router-link :to="{name: 'register'}">aquí</router-link></p>
      </div>
    </div>
  </div>
  
</template>

<script setup>
  import { ref } from 'vue'
  import { useLoginStore } from '@/store/Login'
  import router from '@/router'

  const store = useLoginStore() 
  let correo_electronico = ref("")
  let password = ref("")

  const authUser = async () => {
    const success = await store.login(correo_electronico.value, password.value) 
    if(success == false) {
      alert("Login fallido")
    } else {
      router.push({name: 'main'})
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
    width: 300px;
    height: 350px;
  }

  .data {
    display: flex;
    flex-direction: column;
    align-items: center;   
    justify-content: center;
    gap: 25px;
    height: 80%;
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
