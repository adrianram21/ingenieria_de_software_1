<template>
    <div class="first-layer">
    <h1>Admin</h1>
        <div>
        </div>

    </div>
  
</template>

<script setup>
    /* import { useLoginStore } from '@/store/Login'

    const store = useLoginStore()

    const sendToServer = async () => {
        const response = await fetch('http://127.0.0.1:8000/inventario/main', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': 'Bearer ' + store.jwt
            }
        })

        const res = await response.json()
        if(res.message == "Funciona") {
            alert("Si funciona")
        } else {
            alert("No funciona")
        }
    } */

</script>

<style lang='scss' scoped>

    h1 {
        color: $neutral-black;
        font-family: "Verdana";
    }
    .first-layer {
        display: flex;
        justify-content: center;
        align-items: center;  
        flex-direction: column;   
    } 

</style>