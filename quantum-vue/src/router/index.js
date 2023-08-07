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
import MyCoursesView from '../views/MyCoursesView.vue'
import CalendarView from '../views/CalendarView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      meta: {
        title: 'Авторизация'
      }
    },
    {
      path: '/',
      name: 'main',
      component: ProfileView,
      meta: {
        title: 'Профиль'
      }
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView,
      meta: {
        title: 'Профиль'
      }
    },
    {
      path: '/free-courses',
      name: 'free-courses',
      component: FreeCoursesView,
      meta: {
        title: 'Бесплатные курсы'
      }
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView,
      meta: {
        title: 'Регистрация'
      }
    },
    {
      path: '/logout',
      name: 'logout',
      component: LogoutView,
      meta: {
        title: 'Выход'
      }
    },
    {
      path: '/courses',
      name: 'courses',
      component: CoursesView,
      meta: {
        title: 'Каталог курсов'
      }
    },
    {
      path: '/cart',
      name: 'cart',
      component: CartView,
      meta: {
        title: 'Корзина'
      }
    },
    {
      path: '/course/:id',
      name: 'course',
      component: CourseView
    },
    {
      path: '/webinar/:id',
      name: 'webinar',
      component: WebinarView
    },
    {
      path: '/my-courses',
      name: 'my-courses',
      component: MyCoursesView
    },
    {
      path: '/calendar',
      name: 'calendar',
      component: CalendarView
    },
    {
      path: '/:pathMatch(.*)*',
      name: '404',
      component: NotFoundView,
      meta: {
        title: 'Ошибка 404 - страница не найдена'
      }
    }
  ]
})

export default router
