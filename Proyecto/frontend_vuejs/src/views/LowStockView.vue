<template>
  <div class="first-layer">
    <h1>Productos con stock por debajo del minimo</h1>
    <router-link :to="{name: 'main'}"><button class="modify">Volver al menu principal</button></router-link>
    <div class="products">
      <div class="product" v-for="product in ProductsStore.productos" :key="product.id">
        <div class="information">
          <p>Nombre: {{ product.nombre }}</p>
          <p>Categoria: {{ product.categoria }}</p>
          <p>Precio: ${{ product.precio }}</p>
          <p>Cantidad: {{ product.cantidad }}</p>
          <p>Stock minimo: {{ product.stock_minimo }}</p>
        </div>
      </div>
    </div>
    

  </div>
</template>

<script setup>
  import { useProductsStore } from '@/store/Products'
  import { useLoginStore } from '@/store/Login'
  import { onMounted } from 'vue'
  import router from '@/router'

  const userStore = useLoginStore()
  const ProductsStore = useProductsStore()

  onMounted(() => {
    show()
  })

  const show = async () => {
    const refreshed = userStore.refreshToken()
    if (refreshed) {
      await ProductsStore.lowStock(userStore.id_organizacion, userStore.accessJWT)
    } 
    else {
      userStore.logout()
      router.push({name: 'login'})
    }
  }
</script>

<style scoped lang="scss">
  .modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 10px;
  width: 300px;
  text-align: center;
  
}

.modal-content input {
  width: 100%;
  margin-bottom: 10px;
  padding: 5px;
}

.modal-buttons {
  display: flex;
  justify-content: space-between;
  gap: 20px;
}

  input {
    display: block;
    margin: 5px 0;
  }
  button {
    margin-left: 10px;
  }
  
  .modify {
    margin: 0;
    background-color: $primary-blue;
    color: $primary-white;
    border: 3px solid $primary-blue;
    border-radius: 10px;
    width: 200px;
    height: 40px;
    font-weight: bold;
  }

  .modify:hover {
    cursor: pointer;
    background-color: $primary-white;
    color: $primary-blue;
    font-weight: bold;
  }

  .delete {
    margin: 0;
    background-color: $delete-red;
    color: $primary-white;
    border: 3px solid $delete-red;
    border-radius: 10px;
    width: 200px;
    height: 40px;
    font-weight: bold;
  }

  .delete:hover {
    cursor: pointer;
    background-color: $primary-white;
    color: $delete-red;
    font-weight: bold;
  }

  h1 {
    font-family: "Verdana";
    color: $primary-white;
    margin-bottom: 10px;
  }

  h2 {
    font-family: "Verdana";
    color: $neutral-black;
    
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
  
  .products {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    flex-direction: row;
    justify-content: center;
  }

  .product {
    background-color: $primary-white;
    border: 2px solid $primary-blue;
    border-radius: 30px;
    width: 200px;
    height: 200px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    gap: 40px;

    button {
      width: 100px;
    }
  }

  .buttons {
    display: flex;
    gap: 10px;
    flex-direction: column;
  }

  .information {
    text-align: left;
  }
</style>
