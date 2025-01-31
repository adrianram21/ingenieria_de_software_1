<template>
    <div>
      <h2>Productos con Stock Bajo</h2>
      <table>
        <tr>
          <th>Nombre</th>
          <th>Cantidad</th>
          <th>Stock Mínimo</th>
        </tr>
        <tr v-for="producto in productos" :key="producto.id">
          <td>{{ producto.nombre }}</td>
          <td>{{ producto.cantidad }}</td>
          <td>{{ producto.stock_minimo }}</td>
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
      InventoryService.getStockBajo()
        .then(response => {
          this.productos = response.data;
        })
        .catch(error => {
          console.error('Error al obtener productos con stock bajo:', error);
        });
    }
  };
  </script>
  