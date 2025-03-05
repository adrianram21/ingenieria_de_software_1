import { createRouter, createWebHistory } from "vue-router"
import LoginView from "@/views/LoginView.vue"
import RegisterView from "@/views/RegisterView.vue"
import MainView from "@/views/MainView.vue"
import { useLoginStore } from "@/store/Login"
import AdminView from "@/views/AdminView.vue"
import RecoverView from "@/views/RecoverView.vue" 
import InventoryView from "@/views/InventoryView.vue"
import RegisterMovementView from "@/views/RegisterMovementView.vue"
import LowStockView from "@/views/LowStockView.vue"
import MovementView from "@/views/MovementView.vue"
import InformView from "@/views/InformView.vue"

const routes = [
    {
        path: '/',
        redirect: 'login',
    },
    {
        path: '/login',
        name: 'login',
        component: LoginView,
        meta: {
            requireAuth: false,
            needAdmin: false
        }
    },
    {
        path: '/recover',
        name: 'recover',
        component: RecoverView,
        meta: {
            requireAuth: false,
            needAdmin: false
        }
    },
    {
        path: '/register',
        name: 'register',
        component: RegisterView,
        meta: {
            requireAuth: false,
            needAdmin: false
        }
    },
    {
        path: '/main',
        name: 'main',
        component: MainView,
        meta: {
            requireAuth: true,
            needAdmin: false
        }
    },
    {
        path: '/admin',
        name: 'admin',
        component: AdminView,
        meta: {
            requireAuth: true,
            needAdmin: true
        }
    },
    {
        path: '/inventario',
        name: 'inventario',
        component: InventoryView,
        meta: {
            requireAuth: true,
            needAdmin: false
        }
    },
    {
        path: '/registrarMovimiento',
        name: 'registrarMovimiento',
        component: RegisterMovementView,
        meta: {
            requireAuth: true,
            needAdmin: false
        }
    },
    {
        path: '/stockBajo',
        name: 'stockBajo',
        component: LowStockView,
        meta: {
            requireAuth: true,
            needAdmin: false
        }
    },
    {
        path: '/movimientos',
        name: 'movimientos',
        component: MovementView,
        meta: {
            requireAuth: true,
            needAdmin: false
        }
    },
    {
        path: '/informe',
        name: 'informe',
        component: InformView,
        meta: {
            requireAuth: true,
            needAdmin: false
        }
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes 
})


router.beforeEach((to, from, next) => {
    const store = useLoginStore()
    const Auth = store.accessJWT
    const Rol = store.rol

    if ((to.meta.requireAuth) && (Auth == null)) {
        next('login')  
    } else {
        if ((to.meta.needAdmin && Rol == "Administrador") || (!to.meta.needAdmin)) {
            next()
        } else {
            alert("No cuentas con los permisos para acceder")
            next(from.name)
        }
    }
})

export default router
