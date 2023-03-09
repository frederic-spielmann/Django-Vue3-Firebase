import { createRouter, createWebHistory } from 'vue-router'
import guest from './guest';
import members from './members';
import movies from './members/movies';

const routes = [
    { ...guest }, // public routes
    { ...members }, // authenticated users routes
    { ...movies }
];

const router = createRouter({
    routes,
    history: createWebHistory(),
});

export default router
