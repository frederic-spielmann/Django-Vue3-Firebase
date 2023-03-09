import { requireAuth } from "./index"
import List from "@/components/movies/list.vue"
import Detail from "@/components/movies/detail.vue"
import AddEdit from "@/components/movies/add_edit.vue"

export default {
    path: '/movies',
    beforeEnter: requireAuth,
    children: [
        { path: '', component: List },
        { path: ':id', component: Detail },
        { path: 'add', component: AddEdit },
        { path: 'edit/:id', component: AddEdit }
    ]
};