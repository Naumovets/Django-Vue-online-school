<script setup>
    import { onBeforeMount } from 'vue'
    import Sidebar from '../components/sidebar.vue'
    import Header from '../components/header.vue'
    import Footer from '../components/footer.vue'
    import { checklogin } from '../modules/login.js'
    import { ref } from 'vue'
    import VueCookies from 'vue-cookies'
    import axios from 'axios'
    import { useRoute, useRouter, RouterLink } from 'vue-router';

    const router = useRouter();
    const route = useRoute();
    const slug = route.params.slug;
    const orderItem = ref()
    const error = ref()


    onBeforeMount(() => {
        checklogin()
        axios({
            url: `http://localhost:7000/api/v1/course/${slug}`,
            method: 'get',
            headers: {'Authorization': VueCookies.get('Authorization')}
        })
        .then(function(response){
            orderItem.value = response.data
        })
        .catch(function(error){
            router.push('/404');
        })
    });

    document.title = 'Курс'
</script>

<template>
    <Sidebar />
    <main>
        <Header />
        <div v-if="orderItem" class="container-fluid">
            <div class="row mt-5">
                <div class="col-12 col-lg-12">
                    <div class="card shadow-none border-0">
                        <div class="row g-0 p-5">
                            <div class="row">
                                <h1>{{ orderItem.course.title }}</h1>
                                <div>
                                    <span class="badge text-bg-primary">{{ orderItem.course.exam }}</span>
                                    <span class="badge text-bg-info ms-2">{{ orderItem.course.subject }}</span>
                                    <span class="badge text-bg-success">{{ orderItem.course.status }}</span>
                                </div>
                            </div>

                            <div class="col-md-8 col-12 p-5">
                                <img :src="'http://localhost:7000' + orderItem.course.image" class="w-100 img-fluid rounded-start" alt="...">
                                <ol class="list-group mt-5">
                                    <li class="list-group-item">
                                        <div class="d-flex justify-content-between">
                                            <span>Описание</span>
                                            <div class="col-8 d-flex align-items-center justify-content-end">
                                                <p>
                                                    {{ orderItem.course.description }}
                                                </p>
                                            </div>
                                        </div>
                                    </li>
                                    <li class="list-group-item">
                                        <div class="d-flex justify-content-between">
                                            <span>Преподаватель</span>
                                            <div class="col-6 d-flex align-items-center justify-content-end">
                                                <a class="me-2" :href="orderItem.course.teacher.vk_link">
                                                    {{ orderItem.course.teacher.first_name }} {{ orderItem.course.teacher.last_name }}
                                                </a>
                                                <div class="avatar avatar-circle avatar-xs">
                                                    <img width="100%" :src="'http://localhost:7000' + orderItem.course.teacher.image" class="avatar-title">
                                                </div>
                                            </div>
                                        </div>
                                    </li>
                                    <li v-if="orderItem.curator" class="list-group-item">
                                        <div class="d-flex justify-content-between">
                                            <span>Куратор</span>
                                            <div class="col-9 d-flex align-items-center justify-content-end">
                                                <a class="me-2" :href="orderItem.curator.vk_link">
                                                    {{ orderItem.curator.first_name }} {{ orderItem.curator.last_name }}
                                                </a>
                                                <div class="avatar avatar-circle avatar-xs">
                                                    <img width="100%" :src="'http://localhost:7000' + orderItem.curator.image" class="avatar-title">
                                                </div>
                                            </div>
                                        </div>
                                    </li>
                                    <li v-if="orderItem.course.chat" class="list-group-item">
                                        <div class="d-flex justify-content-between">
                                            <span>Беседа в VK</span>
                                            <div class="col-9 d-flex align-items-center justify-content-end">
                                                <a class="mw-100 text-right" :href="orderItem.course.chat">
                                                    {{ orderItem.course.chat }}
                                                </a>
                                            </div>
                                        </div>
                                    </li>
                                </ol>
                            </div>

                            <div class="col-md-4 col-12 p-5">
                                    <h3>Вебинары</h3>
                                    <div class="list-group w-100">
                                        <template v-for="webinar in orderItem.webinars" :key="webinar.id">
                                            <RouterLink :to="'/webinar/' + webinar.code" class="list-group-item list-group-item-action">{{webinar.title}}</RouterLink>
                                        </template>
                                        <span v-if="!orderItem.webinars">Пока ничего нет</span>
                                    </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <Footer />
    </main>
</template>

<style>
</style>