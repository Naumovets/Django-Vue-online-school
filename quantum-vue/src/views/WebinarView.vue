<script setup>
    import { onBeforeMount } from 'vue'
    import Sidebar from '../components/sidebar.vue'
    import Header from '../components/header.vue'
    import Footer from '../components/footer.vue'
    import { checklogin } from '../modules/login.js'
    import { ref } from 'vue'
    import VueCookies from 'vue-cookies'
    import axios from 'axios'
    import { useRoute, useRouter } from 'vue-router';

    const router = useRouter();
    const route = useRoute();
    const code = route.params.code;
    const webinar = ref()
    const curator = ref()


    onBeforeMount(() => {
        checklogin()
        axios({
            url: `https://admin.lk-quantum.ru/api/v1/course/webinar/${code}`,
            method: 'get',
            headers: {'Authorization': VueCookies.get('Authorization')}
        })
        .then(function(response){
            webinar.value = response.data.webinar
            curator.value = response.data.curator
        })
        .catch(function(error){
            router.push('/404');
        })
    });

    document.title = 'Вебинар'

</script>

<template>
    <Sidebar />
    <main>
        <Header />
        <div v-if="webinar" class="container-fluid">
            <div class="row mt-5">
                <div class="col-12 col-lg-12">
                    <div class="card shadow-none border-0">
                        <div class="row g-0 p-5">
                            <div class="row">
                                <h1>{{ webinar.title }}</h1>
                                <div>
                                    <span class="badge text-bg-primary">{{ webinar.course.exam }}</span>
                                    <span class="badge text-bg-info ms-2">{{ webinar.course.subject }}</span>
                                    <span class="badge text-bg-success ms-2">{{ webinar.course.status }}</span>
                                </div>
                            </div>

                            <div class="col-lg-8 col-12 p-5">
                                <iframe class="w-100 webinar-video" :src="'https://www.youtube.com/embed/' + webinar.code_of_translation" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                            </div>
                            <div class="col-lg-4 col-12 p-5">
                                <iframe class="w-100 h-100 webinar-chat" :src="'https://www.youtube.com/live\_chat?v='+ webinar.code_of_translation + '&amp;embed\_domain=lk-quantum.ru'" ></iframe>
                            </div>

                            <div class="col-md-8 col-12 p-5">
                                <ol class="list-group mt-5">
                                    <li class="list-group-item">
                                        <div class="d-flex justify-content-between">
                                            <span>Описание</span>
                                            <div class="col-8 d-flex align-items-center justify-content-end">
                                                <p>
                                                    {{ webinar.description }}
                                                </p>
                                            </div>
                                        </div>
                                    </li>
                                    <li class="list-group-item">
                                        <div class="d-flex justify-content-between">
                                            <span>Преподаватель</span>
                                            <div class="col-6 d-flex align-items-center justify-content-end">
                                                <a class="me-2" :href="webinar.course.teacher.vk_link">
                                                    {{ webinar.course.teacher.first_name }} {{ webinar.course.teacher.last_name }}
                                                </a>
                                                <div class="d-md-block d-none avatar avatar-circle avatar-xs">
                                                    <img v-if="webinar.course.teacher.image !== null" width="100%" :src="'https://admin.lk-quantum.ru' + webinar.course.teacher.image" class="avatar-title">
                                                    <img v-else width="100%" src="../assets/images/profiles/student.png" class="avatar-title">
                                                </div>
                                            </div>
                                        </div>
                                    </li>
                                    <li v-if="curator !== undefined && curator !== null" class="list-group-item">
                                        <div class="d-flex justify-content-between">
                                            <span>Куратор</span>
                                            <div class="col-9 d-flex align-items-center justify-content-end">
                                                <a class="me-2" :href="curator.vk_link">
                                                    {{ curator.first_name }} {{ curator.last_name }}
                                                </a>
                                                <div class="d-md-block d-none avatar avatar-circle avatar-xs">
                                                    <img v-if="curator.image !== null" width="100%" :src="'https://admin.lk-quantum.ru' + curator.image" class="avatar-title">
                                                    <img v-else width="100%" src="../assets/images/profiles/student.png" class="avatar-title">
                                                </div>
                                            </div>
                                        </div>
                                    </li>
                                    <li v-if="webinar.course.chat !== null && webinar.course.chat !== undefined" class="list-group-item">
                                        <div class="d-flex justify-content-between">
                                            <span>Беседа в VK</span>
                                            <div class="col-9 d-flex align-items-center justify-content-end">
                                                <a class="mw-100 text-right" :href="webinar.course.chat">
                                                    {{ webinar.course.chat }}
                                                </a>
                                            </div>
                                        </div>
                                    </li>
                                </ol>
                            </div>
                            <div class="col-md-4 col-12 p-5">
                                <h3 v-if="webinar.files" >Файлы</h3>
                                <ol class="list-group list-group-numbered w-100">
                                    <template v-for="file in webinar.files">
                                        <a :href="'https://admin.lk-quantum.ru'+file.file_of_webinar" class="list-group-item list-group-item-action" target="_blank">{{file.title}}</a>
                                    </template>
                                </ol>
                                <h3 v-if="webinar.tasks" class="mt-5">Тест</h3>
                                <ol class="list-group w-100">
                                    <template v-for="task in webinar.tasks">
                                        <li class="list-group-item">
                                            <img v-if="task.question_image" class="mw-100 mb-5" :src="'https://admin.lk-quantum.ru' + task.question_image" alt="">
                                            <label v-if="task.question" class="form-label" for="FormControlInput">{{ task.question }}</label>
                                            <input v-model="task.user_answer" type="text" id="FormControlInput" class="mt-2 form-control" placeholder="Ответ..">
                                            <div v-if="task.user_answer == task.answer" class="alert alert-success mt-2" role="alert">
                                                Верно!
                                            </div>
                                            <div v-else-if="task.user_answer && task.answer != task.user_answer" class="alert alert-danger mt-2" role="alert">
                                                Ошибка!
                                            </div>
                                            <div class="accordion accordion-flush" id="accordionFlushExample">
                                                <div class="accordion-item">
                                                    <h2 class="accordion-header" :id="'flush-heading'+task.id">
                                                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" :data-bs-target="'#flush-collapse'+task.id" aria-expanded="false" :aria-controls="'flush-collapse'+task.id">
                                                            Ответ
                                                        </button>
                                                    </h2>
                                                    <div :id="'flush-collapse'+task.id" class="accordion-collapse collapse" :aria-labelledby="'flush-heading'+task.id" data-bs-parent="#accordionFlushExample">
                                                        <div class="accordion-body">{{ task.answer }}</div>
                                                    </div>
                                                </div>
                                            </div>
                                        </li>
                                    </template>
                                </ol>
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
    .webinar-video{
        aspect-ratio: 16/9;
    }
    .webinar-chat{
        min-height: 300px;
    }
</style>
