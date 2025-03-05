<template>
    <div class="first-layer">
        <div class="second-layer">
            <div>
                <h1>Menú principal</h1>
            </div>    
            <div class="buttons">
                <router-link :to="{name: 'inventario'}"><button>Inventario</button></router-link>
                <router-link :to="{name: 'informe'}"><button>Informe</button></router-link>
                <router-link :to="{name: 'stockBajo'}"><button>Productos con stock bajo</button></router-link>
                <router-link :to="{name: 'movimientos'}"><button>Historial de movimientos</button></router-link>
                <router-link :to="{name: 'registrarMovimiento'}"><button>Registrar movimiento</button></router-link>
            </div>
        </div>
    </div>
  
</template>

<script setup>

</script>

<style lang='scss' scoped>

    h1 {
        font-family: "Verdana";
        color: $neutral-black;
        margin-bottom: 10px;
    }

    .first-layer {
        display: flex;
        justify-content: center;
        align-items: center;  
        flex-direction: column;   
        height: 100vh;
        background: linear-gradient(135deg, $primary-blue, $primary-white);
    } 

    .buttons {
        width: 200px;
        display: flex;
        flex-direction: column;
        gap: 20px;
        justify-content: center;

        button {
            margin: 0;
            background-color: $primary-blue;
            color: $primary-white;
            border: 3px solid $primary-blue;
            border-radius: 10px;
            width: 200px;
            height: 40px;
            font-weight: bold;
        }
    }

    button:hover {
        cursor: pointer;
        background-color: $primary-white;
        color: $primary-blue;
        font-weight: bold;
    }

    .second-layer {
        background-color: $primary-white;
        border: 2px solid $primary-blue;
        display: flex;
        border-radius: 30px;
        width: 300px;
        height: 420px;
        align-items: center;
        flex-direction: column;
        gap: 30px;
    }

</style>