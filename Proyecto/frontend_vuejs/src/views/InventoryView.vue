<template>
    <div>
      <h2>Inventario</h2>
      <table>
        <tr>
          <th>Nombre</th>
          <th>Categoría</th>
          <th>Cantidad</th>
          <th>Precio</th>
        </tr>
        <tr v-for="producto in productos" :key="producto.id">
          <td>{{ producto.nombre }}</td>
          <td>{{ producto.categoria }}</td>
          <td>{{ producto.cantidad }}</td>
          <td>${{ producto.precio }}</td>
        </tr>
      </table>
    </div>
  </template>
  
  <script>
  import InventoryService from '../services/InventoryService';
  
  export default {
    data() {
      return {
        productos: []
      };
    },
    mounted() {
      InventoryService.getProductos()
        .then(response => {
          this.productos = response.data;
        })
        .catch(error => {
          console.error('Error al obtener productos:', error);
        });
    }
  };
  </script>
  