import { useUsersStore } from "@/stores/users.store";
import Home from "@/views/HomeView.vue";
import ProfileView from "@/views/ProfileView.vue";

export const requireAuth = async (to, from, next) => {
    const userStore = useUsersStore();
    userStore.loadingSession = true;
    const user = await userStore.currentUser();
    if (user) {
        next();
    } else {
        next("/login");
    }
    userStore.loadingSession = false;
};

export default {
    path: '/',
    beforeEnter: requireAuth,
    children: [
        { path: '', component: Home },
        { path: 'profile', component: ProfileView }
    ]
};