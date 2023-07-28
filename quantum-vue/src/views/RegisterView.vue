<script setup>
    import { ref, reactive } from 'vue'
    import { isAuthorized } from '../modules/login.js'
    import { onBeforeMount } from 'vue'
    import axios from 'axios'
    import Footer from '../components/footer.vue'
    import { useRouter } from 'vue-router';

    const router = useRouter();
    const first_name = ref('')
    const last_name = ref('')
    const email = ref('')
    const tel = ref('')
    const link = ref('')
    const info = ref('')
    const password = reactive({
        value: '',
        type: 'password'
    })
    const repeatPassword = reactive({
        value: '',
        type: 'password'
    })
    const agree = ref(false)

    function changeTypePassword(pass) {
        if(pass.type === 'password'){
            pass.type = 'text'
        }else{
            pass.type = 'password'
        }
    }

    function comparePassword(){
        return password.value === repeatPassword.value
    }

    function register(){
        if(!comparePassword()){
            info.value = 'Пароли должны совпадать!'
        }
        else if(first_name.value == ''){
            info.value = 'Введите имя!'
        }
        else if(last_name.value == ''){
            info.value = 'Введите фамилию!'
        }
        else if(email.value == ''){
            info.value = 'Введите email!'
        }
        else if(!agree){
            info.value = 'Вы должны принять политику обработки персональных данных!'
        }
        else if(tel.value == ''){
            info.value = 'Введите номер телефона!'
        }
        else if(link.value == ''){
            info.value = 'Введите ссылку на свой вк профиль!'
        }
        else{ 
            let form_data = new FormData();
            form_data.append('email', email.value);
            form_data.append('password', password.value)
            form_data.append('tel', tel.value)
            form_data.append('first_name', first_name.value)
            form_data.append('last_name', last_name.value)
            form_data.append('vk_link', link.value)
            axios({
            url: 'https://admin.lk-quantum.ru/api/v1/user/users/',
            method: 'post',
            data: form_data,
            headers:{'Content-Type':'multipart/form-data'}
            })
            .then(function(response){
            if(response.status == 201){
                    router.push('/login');
            }})
            .catch(function(error){
                info.value = Object.values(error.response.data)[0][0]
            })
        }
    }

    onBeforeMount(() => {
        isAuthorized()
    });

    document.title = 'Регистрация'


</script>

<template>
    <!-- MAIN CONTENT -->
    <main class="container">
        <div class="row align-items-center justify-content-center vh-100">
            <div class="col-11 col-md-8 col-lg-6 col-xl-5 col-xxl-4 py-6">

                <!-- Title -->
                <h1 class="mb-2 text-center">
                    Регистрация
                </h1>

                <!-- Subtitle -->
                <p class="text-secondary text-center">
                    Зарегистрируйте свой аккаунт
                </p>

                <!-- Form -->
                <form @submit.prevent="register">
                    <div class="row">
                        <div class="col-6">
                            <div class="mb-4">

                                <!-- Label -->
                                <label class="form-label">
                                    Имя
                                </label>

                                <!-- Input -->
                                <input v-model='first_name' type="text" class="form-control" placeholder="Имя" required>
                            </div>
                        </div>

                        <div class="col-6">
                            <div class="mb-4">

                                <!-- Label -->
                                <label class="form-label">
                                    Фамилия
                                </label>

                                <!-- Input -->
                                <input v-model='last_name' type="text" class="form-control" placeholder="Фамилия" required>
                            </div>
                        </div>

                        <div class="col-6">
                            <div class="mb-4">

                                <!-- Label -->
                                <label class="form-label">
                                    Телефон
                                </label>

                                <!-- Input -->
                                <input v-model='tel' type="phone" class="form-control" placeholder="+79998883322" required>
                            </div>
                        </div>

                        <div class="col-6">
                            <div class="mb-4">

                                <!-- Label -->
                                <label class="form-label">
                                    Ссылка на ВК
                                </label>

                                <!-- Input -->
                                <input v-model='link' type="text" class="form-control" placeholder="https://vk.com/id1" required>
                            </div>
                        </div>
                        
                        <div class="col-12">
                            <div class="mb-4">

                                <!-- Label -->
                                <label class="form-label">
                                    Email адрес
                                </label>

                                <!-- Input -->
                                <input v-model='email' type="email" class="form-control" placeholder="example@mail.com" required>
                            </div>
                        </div>
                    </div> <!-- / .row -->

                    <div class="row">
                        <div class="col-12">
                            <div class="mb-4">

                                <!-- Label -->
                                <label class="form-label">
                                    Пароль
                                </label>
                                <!-- Input -->
                                <div class="input-group input-group-merge">
                                    <input v-model='password.value' :type='password.type' class="form-control" autocomplete="off" data-toggle-password-input placeholder="Введите пароль" required>
                                    
                                    <button @click='changeTypePassword(password)' type="button" class="input-group-text px-4 text-secondary link-primary" data-toggle-password></button>
                                </div>
                            </div>
                        </div>

                        <div class="col-12">
                            <div class="mb-4">

                                <!-- Label -->
                                <label class="form-label">
                                    Повторите пароль
                                </label>

                                <!-- Input -->
                                <div class="input-group input-group-merge">
                                    <input v-model='repeatPassword.value' :type="repeatPassword.type" class="form-control" autocomplete="off" data-toggle-password-input placeholder="Повторите пароль" required>
                                    
                                    <button @click='changeTypePassword(repeatPassword)' type="button" class="input-group-text px-4 text-secondary link-primary" data-toggle-password></button>
                                </div>
                            </div>
                        </div>
                    </div> <!-- / .row -->

                    <div class="form-check">

                        <!-- Input -->
                        <input v-model='agree' type="checkbox" class="form-check-input" id="agree" required>

                        <!-- Label -->
                        <label class="form-check-label" for="agree">
                            Я согласен с <a href="javascript: void(0);">политикой обработки персональных данных</a>
                        </label>
                    </div>

                    <div v-if="info" class="alert alert-danger" role="alert">

                        {{ info }}
                    
                    </div>

                    <div class="row align-items-center text-center">
                        <div class="col-12">

                            <!-- Button -->
                            <button type="submit" class="btn w-100 btn-primary mt-6 mb-2">Зарегистрироваться</button>
                        </div>

                        <div class="col-12">

                            <!-- Link -->
                            <small class="mb-0 text-muted">Уже есть аккаунт? <RouterLink class="fw-semibold" to="/login">Войти</RouterLink></small>
                        </div>
                    </div> <!-- / .row -->
                </form>
            </div>
        </div> <!-- / .row -->
        <Footer />
    </main> <!-- / main -->
</template>