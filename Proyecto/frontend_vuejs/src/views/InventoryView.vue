<template>
  <div class="first-layer">
    <h1>Inventario</h1>
    <router-link :to="{name: 'main'}"><button class="modify">Volver al menu principal</button></router-link>
    <button class="modify" @click="showAddProduct = true">Agregar producto</button>
    <div class="products">
      <div class="product" v-for="product in ProductsStore.productos" :key="product.id">
        <div class="information">
          <p>Nombre: {{ product.nombre }}</p>
          <p>Categoria: {{ product.categoria }}</p>
          <p>Precio: ${{ product.precio }}</p>
          <p>Cantidad: {{ product.cantidad }}</p>
          <p>Stock minimo: {{ product.stock_minimo }}</p>
        </div>
        <div class="buttons">
          <button class="modify" @click="editProduct(product)">Modificar</button>
          <button class="delete" @click="erase(product.id)">Eliminar</button>
        </div>
      </div>
    </div>
    
    <div v-if="showAddProduct" class="modal">
      <div class="modal-content">
        <h2>Agregar Producto</h2>
        <label>Nombre:</label>
        <input v-model="newProduct.nombre" type="text" />

        <label>Categoría:</label>
        <input v-model="newProduct.categoria" type="text" />

        <label>Precio:</label>
        <input v-model="newProduct.precio" type="number" />

        <label>Cantidad:</label>
        <input v-model="newProduct.cantidad" type="number" />

        <label>Stock mínimo:</label>
        <input v-model="newProduct.stock_minimo" type="number" />

        <div class="modal-buttons">
          <button class="modify" @click="addProduct">Confirmar</button>
          <button class="delete" @click="showAddProduct = false">Cancelar</button>
        </div>
      </div>
    </div>

    <div v-if="showEditProduct" class="modal">
      <div class="modal-content">
        <h2>Modificar Producto</h2>
        <label>Nombre:</label>
        <input v-model="selectedProduct.nombre" type="text" />

        <label>Categoría:</label>
        <input v-model="selectedProduct.categoria" type="text" />

        <label>Precio:</label>
        <input v-model="selectedProduct.precio" type="number" />

        <label>Cantidad:</label>
        <input v-model="selectedProduct.cantidad" type="number" />

        <label>Stock mínimo:</label>
        <input v-model="selectedProduct.stock_minimo" type="number" />

        <div class="modal-buttons">
          <button class="modify" @click="updateProduct">Guardar cambios</button>
          <button class="delete" @click="showEditProduct = false">Cancelar</button>
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
  import { ref } from 'vue'

  const showAddProduct = ref(false)
  const showEditProduct = ref(false)
  const selectedProduct = ref(null)
  const userStore = useLoginStore()
  const ProductsStore = useProductsStore()
  const newProduct = ref({
    nombre: '',
    categoria: '',
    precio: '',
    cantidad: '',
    stock_minimo: '',
    id_organizacion: userStore.id_organizacion
  });

  onMounted(() => {
    show()
  })

  const editProduct = (product) => {
    selectedProduct.value = { ...product }
    showEditProduct.value = true
  };

  const updateProduct = async () => {
  const refreshed = userStore.refreshToken()
    if (refreshed) {
      await ProductsStore.updateProducto(selectedProduct.value.id, selectedProduct.value, userStore.accessJWT)
      showEditProduct.value = false
      show()
    } else {
      userStore.logout()
      router.push({ name: 'login' })
    }
  };

  const erase = async (id_producto) => {
    const refreshed = userStore.refreshToken()
    if (refreshed) {
      await ProductsStore.deleteProductos(id_producto, userStore.accessJWT)
      show()
    }
    else {
      userStore.logout()
      router.push({name: 'login'})
    }
  }

  const addProduct = async () => {
    const refreshed = userStore.refreshToken();
    if (refreshed) {
      await ProductsStore.addProducto(newProduct.value, userStore.accessJWT)
      showAddProduct.value = false
      show()
    } else {
      userStore.logout()
      router.push({ name: 'login' })
    }
  };

  const show = async () => {
    const refreshed = userStore.refreshToken()
    if (refreshed) {
      await ProductsStore.fetchProductos(userStore.id_organizacion, userStore.accessJWT)
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
    width: 400px;
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
