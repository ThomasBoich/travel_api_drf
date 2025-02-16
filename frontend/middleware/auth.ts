import {useAuthStore} from '@/stores/auth';

export default defineNuxtRouteMiddleware((to, from) => {
    const {isAuthenticated} = useAuthStore()
    // if (isAuthenticated && to.path == '/login' || to.path == '/registration') return navigateTo("/")
    // if (!isAuthenticated && to.path !== '/login' || to.path !== '/registration') return navigateTo("/")

    // const {isAuthenticated} = useAuthStore()
    if (!isAuthenticated && to.path !== '/login' && to.path !== '/registration') return navigateTo("/login")
})