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
    const id = route.params.id;
    const webinar = ref()
    const curator = ref()


    onBeforeMount(() => {
        checklogin()
        axios({
            url: `https://admin.lk-quantum.ru/api/v1/course/webinar/${id}`,
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

    function assertAnswer(task){
        task.right_answered = 0;
        task.error_answered = 0;
        task.count_right = 0;

        if(!task.checkbox_answer_1.user_answer && !task.checkbox_answer_2.user_answer && !task.checkbox_answer_3.user_answer && !task.checkbox_answer_4.user_answer && !task.checkbox_answer_5.user_answer){
            task.checkbox_answer_1.is_valid = false;
            task.checkbox_answer_1.is_invalid = false;
            
            task.checkbox_answer_2.is_valid = false;
            task.checkbox_answer_2.is_invalid = false;

            task.checkbox_answer_3.is_valid = false;
            task.checkbox_answer_3.is_invalid = false;

            task.checkbox_answer_4.is_valid = false;
            task.checkbox_answer_4.is_invalid = false;

            task.checkbox_answer_5.is_valid = false;
            task.checkbox_answer_5.is_invalid = false;
            alert('Выберите хотя бы один ответ');

        }else{
            task.count_right = task.checkbox_answer_1.right + task.checkbox_answer_2.right + task.checkbox_answer_3.right + task.checkbox_answer_4.right + task.checkbox_answer_5.right;
            // Для первого чекбокса
            if(task.checkbox_answer_1.right && task.checkbox_answer_1.user_answer){
                task.checkbox_answer_1.is_valid = true;
                task.checkbox_answer_1.is_invalid = false;
                task.right_answered+=1;
            }
            else if(!task.checkbox_answer_1.right && task.checkbox_answer_1.user_answer){
                task.checkbox_answer_1.is_invalid = true;
                task.checkbox_answer_1.is_valid = false;
                task.error_answered+=1;
            }
            else{
                task.checkbox_answer_1.is_invalid = false;
                task.checkbox_answer_1.is_valid = false;
            }

            // для второго чекбокса
            if(task.checkbox_answer_2.right && task.checkbox_answer_2.user_answer){
                task.checkbox_answer_2.is_valid = true;
                task.checkbox_answer_2.is_invalid = false;
                task.right_answered+=1;
            }
            else if(!task.checkbox_answer_2.right && task.checkbox_answer_2.user_answer){
                task.checkbox_answer_2.is_invalid = true;
                task.checkbox_answer_2.is_valid = false;
                task.error_answered+=1;
            }
            else{
                task.checkbox_answer_2.is_invalid = false;
                task.checkbox_answer_2.is_valid = false;
            }

            // для третьего чекбокса
            if(task.checkbox_answer_3.right && task.checkbox_answer_3.user_answer){
                task.checkbox_answer_3.is_valid = true;
                task.checkbox_answer_3.is_invalid = false;
                task.right_answered+=1;
            }
            else if(!task.checkbox_answer_3.right && task.checkbox_answer_3.user_answer){
                task.checkbox_answer_3.is_invalid = true;
                task.checkbox_answer_3.is_valid = false;
                task.error_answered+=1;
            }
            else{
                task.checkbox_answer_3.is_invalid = false;
                task.checkbox_answer_3.is_valid = false;
            }

            // для четвертого чекбокса
            if(task.checkbox_answer_4.right && task.checkbox_answer_4.user_answer){
                task.checkbox_answer_4.is_valid = true;
                task.checkbox_answer_4.is_invalid = false;
                task.right_answered+=1;
            }
            else if(!task.checkbox_answer_4.right && task.checkbox_answer_4.user_answer){
                task.checkbox_answer_4.is_invalid = true;
                task.checkbox_answer_4.is_valid = false;
                task.error_answered+=1;
            }
            else{
                task.checkbox_answer_4.is_invalid = false;
                task.checkbox_answer_4.is_valid = false;
            }

            // для пятого чекбокса
            if(task.checkbox_answer_5.right && task.checkbox_answer_5.user_answer){
                task.checkbox_answer_5.is_valid = true;
                task.checkbox_answer_5.is_invalid = false;
                task.right_answered+=1;
            }
            else if(!task.checkbox_answer_5.right && task.checkbox_answer_5.user_answer){
                task.checkbox_answer_5.is_invalid = true;
                task.checkbox_answer_5.is_valid = false;
                task.error_answered+=1;
            }
            else{
                task.checkbox_answer_5.is_invalid = false;
                task.checkbox_answer_5.is_valid = false;
            }
        }


        
    }

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
                        <div class="row g-0 p-1 p-md-5">
                            <div class="row">
                                <h1>{{ webinar.title }}</h1>
                                <div>
                                    <span class="badge text-bg-primary">{{ webinar.course.exam }}</span>
                                    <span class="badge text-bg-info ms-2">{{ webinar.course.subject }}</span>
                                    <span class="badge text-bg-success ms-2">{{ webinar.course.status }}</span>
                                </div>
                            </div>

                            <div class="col-lg-8 col-12 p-1 p-md-5">
                                <iframe class="w-100 webinar-video" :src="'https://www.youtube.com/embed/' + webinar.code_of_translation" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                            </div>
                            <div class="col-lg-4 col-12 p-1 p-md-5">
                                <iframe class="w-100 h-100 webinar-chat" :src="'https://www.youtube.com/live\_chat?v='+ webinar.code_of_translation + '&amp;embed\_domain=lk-quantum.ru'" ></iframe>
                            </div>

                            <div class="col-md-8 col-12 p-1 p-md-5">
                                <h3>Информация о вебинаре</h3>
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
                            <div class="col-md-4 col-12 p-1 p-md-5">
                                <h3 v-if="webinar.files" >Файлы</h3>
                                <ol class="list-group list-group-numbered w-100">
                                    <template v-for="file in webinar.files">
                                        <a :href="'https://admin.lk-quantum.ru'+file.file_of_webinar" class="list-group-item list-group-item-action" target="_blank">{{file.title}}</a>
                                    </template>
                                </ol>
                            </div>

                            <div class="col-12 p-1 p-md-5">
                                <h3 v-if="webinar.tasks" class="mt-5 mb-0">Задачи для самопроверки!</h3>
                                <ol class="list-group-flush list-group w-100">
                                    <template v-for="task in webinar.tasks">
                                        <li class="list-group-item mt-5">
                                            <div class="col-md-8 col-12 pe-md-5">
                                                <img v-if="task.question_image" class="mw-100 mb-5" :src="'https://admin.lk-quantum.ru' + task.question_image" alt="">
                                                <p class="fs-3" v-if="task.question">{{ task.question }}</p>
                                            </div>

                                            <template v-if="task.is_multi_answer === false">
                                                <div class="row mt-2">
                                                    <div class="col-md-8 col-12 align-items-center">
                                                        <input v-model="task.user_answer" type="text" id="FormControlInput" class="form-control" placeholder="Ответ..">
                                                    </div>
                                                    <div class="col-md-4 col mt-5 mt-md-0 align-items-center">
                                                        <button v-if="(task.solution !== '' && task.solution !== null) || task.solution_image !== null || task.answer" type="button" class="btn text-bg-info-soft" data-bs-toggle="modal" :data-bs-target="'.modal'+task.id">Решение</button>
                                                    </div>
                                                </div>
                                                
                                                <div v-if="task.user_answer == task.answer" class="alert alert-success mt-2" role="alert">
                                                    Верно!
                                                </div>
                                                <div v-else-if="task.user_answer && task.answer != task.user_answer" class="alert alert-danger mt-2" role="alert">
                                                    Ошибка!
                                                </div>
                                                                                            

                                                <div class="modal fade" :class="'modal' + task.id" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
                                                    <div class="modal-dialog modal-lg" role="document">
                                                        <div class="modal-content">
                                                            <div class="modal-header">
                                                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                                            </div>
                                                            <div class="modal-body">
                                                                <strong>Условие</strong>
                                                                <p v-if="task.question !== '' && task.question !== null" id="myLargeModalLabel">{{task.question}}</p>
                                                                <img v-if="task.question_image !== null" :src="'https://admin.lk-quantum.ru' + task.question_image" class="w-100 img-fluid rounded-start" alt="...">
                                                                <hr>
                                                                <strong>Решение</strong>
                                                                <img v-if="task.solution_image !== null" :src="'https://admin.lk-quantum.ru' + task.solution_image" class="w-100 img-fluid rounded-start" alt="...">
                                                                <p class="mt-5" v-if="task.solution !== null && task.solution !== ''">
                                                                    {{ task.solution }}
                                                                </p>
                                                                <p class="mt-5" v-if="task.answer !== null && task.answer !== '' ">
                                                                    Ответ: {{ task.answer }}
                                                                </p>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                            </template>

                                            <template v-else>
                                                <ul class="list-group my-6">

                                                    <li v-if="task.checkbox_answer_1.answer !== null" class="list-group-item">
                                                
                                                        <input v-model="task.checkbox_answer_1.user_answer" :class="{'is-invalid' : task.checkbox_answer_1.is_invalid, 'is-valid': task.checkbox_answer_1.is_valid}" class="form-check-input me-1" type="checkbox" value="" :id="task.id + 'firstCheckbox'">
                                                
                                                        <label class="form-check-label" :for="task.id + 'firstCheckbox'">{{task.checkbox_answer_1.answer}}</label>
                                                
                                                    </li>
                                                
                                                    <li v-if="task.checkbox_answer_2.answer !== null" class="list-group-item">
                                                
                                                        <input v-model="task.checkbox_answer_2.user_answer" :class="{'is-invalid' : task.checkbox_answer_2.is_invalid, 'is-valid': task.checkbox_answer_2.is_valid}" class="form-check-input me-1" type="checkbox" value="" :id="task.id + 'secondCheckbox'">
                                                
                                                        <label class="form-check-label" :for="task.id + 'secondCheckbox'">{{task.checkbox_answer_2.answer}}</label>
                                                
                                                    </li>
                                                
                                                    <li v-if="task.checkbox_answer_3.answer !== null" class="list-group-item">
                                                
                                                        <input v-model="task.checkbox_answer_3.user_answer" :class="{'is-invalid' : task.checkbox_answer_3.is_invalid, 'is-valid': task.checkbox_answer_3.is_valid}" class="form-check-input me-1" type="checkbox" value="" :id="task.id + 'thirdCheckbox'">
                                                
                                                        <label class="form-check-label" :for="task.id + 'thirdCheckbox'">{{task.checkbox_answer_3.answer}}</label>
                                                
                                                    </li>
                                                    
                                                    <li v-if="task.checkbox_answer_4.answer !== null" class="list-group-item">
                                                
                                                        <input v-model="task.checkbox_answer_4.user_answer" :class="{'is-invalid' : task.checkbox_answer_4.is_invalid, 'is-valid': task.checkbox_answer_4.is_valid}" class="form-check-input me-1" type="checkbox" value="" :id="task.id + 'fourCheckbox'">
                                                
                                                        <label class="form-check-label" :for="task.id + 'fourCheckbox'">{{task.checkbox_answer_4.answer}}</label>
                                                
                                                    </li>

                                                    <li v-if="task.checkbox_answer_5.answer !== null" class="list-group-item">
                                                
                                                        <input v-model="task.checkbox_answer_5.user_answer" :class="{'is-invalid' : task.checkbox_answer_5.is_invalid, 'is-valid': task.checkbox_answer_5.is_valid}" class="form-check-input me-1" type="checkbox" value="" :id="task.id + 'fiveCheckbox'">
                                                
                                                        <label class="form-check-label" :for="task.id + 'fiveCheckbox'">{{task.checkbox_answer_5.answer}}</label>
                                                
                                                    </li>
                                                
                                                </ul>
                                                <p v-if="task.count_right !== 0">Верно решенных: {{task.right_answered}} / {{ task.count_right }}</p>
                                                <p v-if="task.error_answered !== 0">Ошибок допущенно: {{task.error_answered}}</p>
                                                <button type="button" @click="assertAnswer(task)" class="mb-5 me-2 btn text-bg-primary-soft">Ответить</button>
                                                <button v-if="(task.solution !== '' && task.solution !== null) || task.solution_image !== null" type="button" class="mb-5 btn text-bg-info-soft" data-bs-toggle="modal" :data-bs-target="'.modal'+task.id">Решение</button>

                                                <div class="modal fade" :class="'modal' + task.id" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
                                                    <div class="modal-dialog modal-lg" role="document">
                                                        <div class="modal-content">
                                                            <div class="modal-header">
                                                                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                                                            </div>
                                                            <div class="modal-body">
                                                                <strong>Условие</strong>
                                                                <p v-if="task.question !== '' && task.question !== null" id="myLargeModalLabel">{{task.question}}</p>
                                                                <img v-if="task.question_image !== null" :src="'https://admin.lk-quantum.ru' + task.question_image" class="w-100 img-fluid rounded-start" alt="...">
                                                                <hr>
                                                                <strong>Решение</strong>
                                                                <img v-if="task.solution_image !== null" :src="'https://admin.lk-quantum.ru' + task.solution_image" class="w-100 img-fluid rounded-start" alt="...">
                                                                <p class="mt-5" v-if="task.solution !== null && task.solution !== ''">
                                                                    {{ task.solution }}
                                                                </p>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>

                                            </template>
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
