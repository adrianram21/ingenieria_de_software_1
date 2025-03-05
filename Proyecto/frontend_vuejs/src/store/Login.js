import { defineStore } from "pinia"

export const useLoginStore = defineStore('login', {
    state: () => {
        return {
            accessJWT: null,
            refreshJWT: null,
            nombre: '',
            id_usuario: '',
            id_organizacion: '',
            rol: '',
            error: ''
        } 
    },
    actions: {
        async login(correo_electronico, password) {
            try {
                const res = await fetch('http://127.0.0.1:8000/inventario/login/', {
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        correo_electronico: correo_electronico,
                        password: password
                    })
                }) 
    
                const response = await res.json()
    
                if('error' in response) {
                    this.error = "Login fallido" 
                    return false
                }
                else {
                    this.error = "Login exitoso"
                }
                
                this.accessJWT = response.token.access
                this.refreshJWT = response.token.refresh
                this.nombre = response.user.nombre
                this.id_usuario = response.user.id
                this.id_organizacion = response.user.id_organizacion
                this.rol = response.user.rol
                return true
    
            } catch(error) {
                this.error = "Login fallido"
                return false
            }
        },
        async refreshToken() {
            const res = await fetch('http://127.0.0.1:8000/api/token/refresh/', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    refresh: this.refreshJWT                    
                })
            })

            const response = await res.json()

            if (res.status === 401) {
                this.error = "Error al refrescar el token"
                return false
            } else {
                this.error = "Token refrescado exitosamente"
            }

            this.accessJWT = response.access;
            return true
        },
        logout() {
            this.accessJWT = null,
            this.refreshJWT = null,
            this.nombre = '',
            this.id_usuario = '',
            this.id_organizacion = '',
            this.rol = '',
            this.error = ''
        }
    },
    persist: true
})