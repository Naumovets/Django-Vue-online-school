import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import ProfileView from '../views/ProfileView.vue'
import LogoutView from '../views/LogoutView.vue'
import NotFoundView from '../views/NotFoundView.vue'
import CoursesView from '../views/CoursesView.vue'
import CartView from '../views/CartView.vue'
import FreeCoursesView from '../views/FreeCoursesView.vue'
import CourseView from '../views/CourseView.vue'
import WebinarView from '../views/WebinarView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/free-courses',
      name: 'free-courses',
      component: FreeCoursesView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/logout',
      name: 'logout',
      component: LogoutView
    },
    {
      path: '/courses',
      name: 'courses',
      component: CoursesView
    },
    {
      path: '/cart',
      name: 'cart',
      component: CartView
    },
    {
      path: '/course/:slug',
      name: 'course',
      component: CourseView
    },
    {
      path: '/webinar/:code',
      name: 'webinar',
      component: WebinarView
    },
    {
      path: '/:pathMatch(.*)*',
      name: '404',
      component: NotFoundView
    }
  ]
})

export default router
