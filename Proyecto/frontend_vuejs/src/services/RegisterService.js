import { ref } from "vue"

class RegisterService {

    constructor() {
        this.nombre = ref('')
        this.rol = ref('')
        this.organizacion = ref('')
        this.correo_electronico = ref('')
        this.password = ref('')
        this.error = ref('')
    }

    getNombre() {
        return this.nombre
    }

    getRol() {
        return this.rol
    }

    getOrganizacion() {
        return this.organizacion
    }

    getCorreoElectronico() {
        return this.correo_electronico
    }

    getPassword() {
        return this.password
    }

    getError() {
        return this.error
    }

    async register(nombre, rol, organizacion, correo_electronico, password) {
        try {
            const res = await fetch('http://127.0.0.1:8000/inventario/register/', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    nombre: nombre,
                    rol: rol,
                    organizacion: organizacion,
                    correo_electronico: correo_electronico,
                    password: password
                })
            }) 
            
            const response = await res.json()

            if('error' in response) {
                this.error.value = response.error
                return false
            }

            return true

        } catch(error) {
            console.log(error)
        }
    }
}

export default RegisterService