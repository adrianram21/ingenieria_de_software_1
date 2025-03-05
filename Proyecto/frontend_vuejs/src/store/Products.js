import { defineStore } from "pinia";

export const useProductsStore = defineStore("productos", {
  state: () => ({
    productos: [],
  }),
  actions: {
    async fetchProductos(id_organizacion, auth) {
      try {
        const res = await fetch("http://127.0.0.1:8000/inventario/showProducts/", {
            method: "POST",
            headers: {
                'Accept': "application/json",
                "Content-Type": "application/json",
                'Authorization': 'Bearer ' + auth
            },
            body: JSON.stringify({
              id_organizacion: id_organizacion,                       
            })
        });
        
        this.productos = await res.json();

      } catch (error) {
        console.error("Error al obtener productos:", error);
      }
    },
    async addProducto(newProduct, auth) {
      try {
        const res = await fetch("http://127.0.0.1:8000/inventario/addProduct/", {
            method: "POST",
            headers: {
                'Accept': "application/json",
                "Content-Type": "application/json",
                'Authorization': 'Bearer ' + auth
            },
            body: JSON.stringify({
              nombre: newProduct.nombre,
              precio: newProduct.precio,
              cantidad: newProduct.cantidad,
              categoria: newProduct.categoria,
              stock_minimo: newProduct.stock_minimo,
              id_organizacion: newProduct.id_organizacion,                       
            })
        });
        
        this.productos = await res.json();

      } catch (error) {
        console.error("Error al agregar producto:", error);
      }
    },
    async updateProducto(ProductID, Product, auth) {
      try {
        const res = await fetch("http://127.0.0.1:8000/inventario/updateProduct/", {
            method: "POST",
            headers: {
                'Accept': "application/json",
                "Content-Type": "application/json",
                'Authorization': 'Bearer ' + auth
            },
            body: JSON.stringify({
              id: ProductID,
              nombre: Product.nombre,
              precio: Product.precio,
              cantidad: Product.cantidad,
              categoria: Product.categoria,
              stock_minimo: Product.stock_minimo,
              id_organizacion: Product.id_organizacion,                       
            })
        });
        
        this.productos = await res.json();

      } catch (error) {
        console.error("Error al actualizar producto:", error);
      }
    },
    async deleteProductos(id_producto, auth) {
      try {
        const res = await fetch("http://127.0.0.1:8000/inventario/deleteProduct/", {
            method: "POST",
            headers: {
                'Accept': "application/json",
                "Content-Type": "application/json",
                'Authorization': 'Bearer ' + auth
            },
            body: JSON.stringify({
              id_producto: id_producto,             
            })
        });

        this.productos = await res.json();

      } catch (error) {
        console.error("Error al obtener productos:", error);
      }
    },
    
  },
});
