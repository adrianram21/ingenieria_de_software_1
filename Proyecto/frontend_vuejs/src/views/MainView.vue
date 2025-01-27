<template>
    <div class="first-layer">
    <h1>Autenticacion</h1>
        <div>
            <button @click="sendToServer">Autenticar</button>
        </div>
        <div>
            <router-link :to="{name: 'admin'}"><button>Prueba admin</button></router-link>
        </div>

    </div>
  
</template>

<script setup>
    import { useLoginStore } from '@/store/Login'
    import router from '@/router'

    const store = useLoginStore()

    const sendToServer = async () => {
        let response = await fetch('http://127.0.0.1:8000/inventario/main', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': 'Bearer ' + store.accessJWT
            }
        })

        if (response.status === 401) {
            const refreshed = await store.refreshToken()
            if (refreshed) {
                alert("Token refrescado")
                response = await fetch('http://127.0.0.1:8000/inventario/main', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Authorization': 'Bearer ' + store.accessJWT
                    }
                })
            } else {
                alert("Token de refresco vencido")
                store.logout()
                router.push({name: 'login'})
            }
            
        }

        const res = await response.json()

        if(res.message == "Funciona") {
            alert("Prueba de autenticacion exitosa")
        } else {
            alert("Prueba de autenticacion fallida")
            router.push({name: 'login'})
        }
    }

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
        gap: 10px; 
    } 

</style>