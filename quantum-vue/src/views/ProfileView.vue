<script setup>

import { onBeforeMount, onMounted } from 'vue'
import Sidebar from '../components/sidebar.vue'
import Header from '../components/header.vue'
import Footer from '../components/footer.vue'
import { checklogin } from '../modules/login.js'

import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import VueCookies from 'vue-cookies'
import axios from 'axios'


const tel = ref('')
const first_name = ref('')
const last_name = ref('')
const email = ref('')
const vk_link = ref('')
const orderItems = ref(null)


onBeforeMount(() => {
    checklogin();
});

axios({
    url: 'http://127.0.0.1:8000/api/v1/user/profile/',
    method: 'get',
    headers: {'Authorization': VueCookies.get('Authorization')}
    })
.then(function(response){
    tel.value = response.data.tel;
    email.value = response.data.email;
    vk_link.value = response.data.vk_link;
    first_name.value = response.data.first_name;
    last_name.value = response.data.last_name;
});
axios({
    url: 'http://127.0.0.1:8000/api/v1/course/get-courses',
    method: 'get',
    headers: {'Authorization': VueCookies.get('Authorization')}
})
.then(function(response){
    orderItems.value = response.data
});


</script>

<template>
    <Sidebar />
    <main>
        <Header />
        <div class="container-fluid">
            <h2>Профиль</h2>
            <!-- horizontal info panel -->
            <div class="card border-0 flex-fill w-100">
                <div class="card-body p-7">
                    <div class="row align-items-center h-100">
                        <div class="col-auto d-flex ms-auto ms-md-0">
                            <div class="avatar avatar-circle avatar-xxl">
                                <img src="../assets/images/profiles/student.png" alt="..." class="avatar-img" width="112" height="112">
                            </div>
                        </div>

                        <div class="col-auto me-auto d-flex flex-column">
                            <h3 class="mb-0">{{first_name}} {{last_name}}</h3>
                            <span class="small text-secondary fw-bold d-block mb-4">Ученик</span>

                            <div class="d-flex">

                                <RouterLink to="calendar" class="btn btn-primary btn-sm">Перейти в календарь</RouterLink>
                            </div>
                        </div>

                        <div class="col-12 col-md-auto ms-auto text-center mt-8 mt-md-0">
                            <div class="hstack d-inline-flex gap-6">
                                <div>
                                    <h4 v-if="orderItems" class="h2 mb-0">{{orderItems.length}}</h4>
                                    <p class="text-secondary mb-0">Курсов</p>
                                </div>
                            </div>
                        </div>
                    </div> <!-- / .row -->
                </div>
            </div>

            <div class="row">
                <!-- vertical info panel -->
                <div class="col-xl-4">

                    <!-- Card -->
                    <div class="card border-0">

                        <div class="card-body mt-5 pt-0">
                            <h3 class="h6 small text-secondary text-uppercase mb-3">Контакты</h3>

                            <ul class="list-unstyled mb-7">
                                <li class="py-2">
                                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" height="18" width="18" class="me-2"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4.285 2.24H4.274C3.27412 2.46215 2.37995 3.01876 1.73921 3.81786C1.09847 4.61696 0.749519 5.61074 0.75 6.635V7.525C0.75 7.92282 0.908036 8.30436 1.18934 8.58566C1.47064 8.86696 1.85218 9.025 2.25 9.025H6C6.39783 9.025 6.77936 8.86696 7.06066 8.58566C7.34197 8.30436 7.5 7.92282 7.5 7.525V7.525C7.5 7.12718 7.65804 6.74564 7.93934 6.46434C8.22064 6.18304 8.60218 6.025 9 6.025H15C15.3978 6.025 15.7794 6.18304 16.0607 6.46434C16.342 6.74564 16.5 7.12718 16.5 7.525C16.5 7.92282 16.658 8.30436 16.9393 8.58566C17.2206 8.86696 17.6022 9.025 18 9.025H21.75C22.1478 9.025 22.5294 8.86696 22.8107 8.58566C23.092 8.30436 23.25 7.92282 23.25 7.525V6.635C23.25 5.61108 22.9009 4.61777 22.2602 3.81908C21.6195 3.02039 20.7255 2.46408 19.726 2.242H19.715C14.6191 1.25482 9.38116 1.25414 4.285 2.24V2.24Z"></path><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3.75 12.025V18.025C3.75 19.2185 4.22411 20.3631 5.06802 21.207C5.91193 22.0509 7.05653 22.525 8.25 22.525H15.75C16.9435 22.525 18.0881 22.0509 18.932 21.207C19.7759 20.3631 20.25 19.2185 20.25 18.025V12.025"></path><path stroke="currentColor" stroke-width="1.5" d="M7.875 14.275C7.66789 14.275 7.5 14.1071 7.5 13.9C7.5 13.6929 7.66789 13.525 7.875 13.525"></path><path stroke="currentColor" stroke-width="1.5" d="M7.875 14.275C8.08211 14.275 8.25 14.1071 8.25 13.9C8.25 13.6929 8.08211 13.525 7.875 13.525"></path><path stroke="currentColor" stroke-width="1.5" d="M7.875 18.025C7.66789 18.025 7.5 17.8571 7.5 17.65C7.5 17.4429 7.66789 17.275 7.875 17.275"></path><path stroke="currentColor" stroke-width="1.5" d="M7.875 18.025C8.08211 18.025 8.25 17.8571 8.25 17.65C8.25 17.4429 8.08211 17.275 7.875 17.275"></path><path stroke="currentColor" stroke-width="1.5" d="M12 14.275C11.7929 14.275 11.625 14.1071 11.625 13.9C11.625 13.6929 11.7929 13.525 12 13.525"></path><path stroke="currentColor" stroke-width="1.5" d="M12 14.275C12.2071 14.275 12.375 14.1071 12.375 13.9C12.375 13.6929 12.2071 13.525 12 13.525"></path><g><path stroke="currentColor" stroke-width="1.5" d="M12 18.025C11.7929 18.025 11.625 17.8571 11.625 17.65C11.625 17.4429 11.7929 17.275 12 17.275"></path><path stroke="currentColor" stroke-width="1.5" d="M12 18.025C12.2071 18.025 12.375 17.8571 12.375 17.65C12.375 17.4429 12.2071 17.275 12 17.275"></path></g><g><path stroke="currentColor" stroke-width="1.5" d="M16.125 14.275C15.9179 14.275 15.75 14.1071 15.75 13.9C15.75 13.6929 15.9179 13.525 16.125 13.525"></path><path stroke="currentColor" stroke-width="1.5" d="M16.125 14.275C16.3321 14.275 16.5 14.1071 16.5 13.9C16.5 13.6929 16.3321 13.525 16.125 13.525"></path></g><g><path stroke="currentColor" stroke-width="1.5" d="M16.125 18.025C15.9179 18.025 15.75 17.8571 15.75 17.65C15.75 17.4429 15.9179 17.275 16.125 17.275"></path><path stroke="currentColor" stroke-width="1.5" d="M16.125 18.025C16.3321 18.025 16.5 17.8571 16.5 17.65C16.5 17.4429 16.3321 17.275 16.125 17.275"></path></g></svg>                                                  
                                    {{tel}}
                                </li>
                                <li class="py-2">
                                    <svg viewBox="0 0 24 24" height="18" width="18" class="me-2" xmlns="http://www.w3.org/2000/svg"><path d="M17.25,12A5.25,5.25,0,1,1,12,6.75,5.25,5.25,0,0,1,17.25,12Z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><path d="M17.25,12v2.25a3,3,0,0,0,6,0V12a11.249,11.249,0,1,0-4.5,9" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
                                    {{ email }}
                                </li>
                            </ul>

                            <h3 v-if="vk_link" class="h6 small text-secondary text-uppercase mb-3">Социальные сети</h3>

                            <ul v-if="vk_link" class="list-unstyled mb-0">
                                <li class="py-2">
                                    <svg viewBox="0 0 24 24" height="18" width="18" class="me-2" xmlns="http://www.w3.org/2000/svg"><path d="M1.874 17.625 A2.625 2.625 0 1 0 7.124 17.625 A2.625 2.625 0 1 0 1.874 17.625 Z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><path d="M8.249,23.25a4.25,4.25,0,0,0-7.5,0" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><path d="M16.874 17.625 A2.625 2.625 0 1 0 22.124 17.625 A2.625 2.625 0 1 0 16.874 17.625 Z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><path d="M23.249,23.25a4.25,4.25,0,0,0-7.5,0" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><path d="M9.374 3.375 A2.625 2.625 0 1 0 14.624 3.375 A2.625 2.625 0 1 0 9.374 3.375 Z" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><path d="M15.248,8.25a4.269,4.269,0,0,0-6.5,0" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><path d="M9.05,19.707a8.277,8.277,0,0,0,5.944-.018" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><path d="M6.348,6a8.217,8.217,0,0,0-2.6,6c0,.253.015.5.038.75" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path><path d="M20.211,12.75c.022-.248.038-.5.038-.75a8.214,8.214,0,0,0-2.6-6" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path></svg>
                                    <a :href="vk_link">Vkontakte</a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>

                <!-- courses -->
                <div class="col">
                    <div class="card border-0">
                        <div class="card-header border-0 card-header-space-between">
                    
                            <!-- Title -->
                            <h3 class="card-header-title h4 text-uppercase">
                                Мои курсы
                            </h3>
                        </div>

                        <!-- Table -->
                        <div class="table-responsive">
                            <table id="projectsTable" class="table align-middle table-edge table-nowrap mb-0">
                                <thead class="thead-light">
                                    <tr>
                                        <th class="w-50">Название</th>
                                        <th>Действует до:</th>
                                        <th class="w-150px text-end">Стоимость</th>
                                    </tr>
                                </thead>

                                <tbody>
                                    <tr v-for="orderItem in orderItems">
                                        <td class="fw-bold">
                                            <h4><RouterLink :to="'course/'+orderItem.course.slug">{{orderItem.course.title}}</RouterLink></h4>
                                        </td>
                                        <td>
                                            <p>{{orderItem.end_date}}</p>
                                        </td>
                                        <td>
                                            <p v-if="!orderItem.price_with_discount && orderItem.course.price">{{orderItem.course.price}}</p>
                                            <p v-else-if="orderItem.course.price">{{orderItem.price_with_discount}}₽ <sup><del class="h6">{{orderItem.course.price}}₽</del></sup></p>
                                            <p v-else>Бесплатно</p>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div> <!-- / .table-responsive -->
                    </div>
                </div>
            </div> 
        </div>
        <Footer />
    </main>
    
</template>