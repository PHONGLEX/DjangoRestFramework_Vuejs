import { createRouter, createWebHistory } from 'vue-router'
import Posts from '../views/Posts'
import Login from '../views/Login'
import Logout from '../views/Logout'

const routes = [
  {
    path: '/',
    name: 'posts',
    component: Posts,
    meta: {
        requiresLogin: true
      }
    },
  {
    path: '/login',
    name: 'login',
    component: Login,
  },
  {
    path: '/logout',
    name: 'logout',
    component: Logout,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
