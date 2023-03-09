import Login from "@/components/auth/login.vue";
import Register from "@/components/auth/register.vue";
import ResetPassword from "@/components/auth/reset-password.vue";
import NewPassword from "@/components/auth/new-password.vue";
import { useUsersStore } from "@/stores/users.store";
import router from "@/router";

const isAlreadyConnected = async (to) => {
    const userStore = useUsersStore();
    const user = await userStore.currentUser();
    const authPages = [
        "/login",
        "/register",
        "/reset-password",
        "/new-password"
    ]
    if(authPages.includes(to.path) && user){
        router.push("/")
    }
};

export default {
    path: '/',
    beforeEnter: isAlreadyConnected,
    children: [
        { path: 'login', component: Login },
        { path: 'register', component: Register },
        { path: 'reset-password', component: ResetPassword },
        { path: 'new-password', component: NewPassword, props: (route) => ({oobCode: route.query.oobCode }) },
    ]
};