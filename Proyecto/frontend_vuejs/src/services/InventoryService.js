import axios from 'axios';

const API_URL = 'http://localhost:8000/api/productos/';

export default {
  getProductos() {
    return axios.get(API_URL);
  },
  getStockBajo() {
    return axios.get(API_URL + 'stock_bajo/');
  }
};
