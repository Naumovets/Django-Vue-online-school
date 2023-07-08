<script setup>
    import { ref, reactive, computed } from 'vue'
    import { useFetch } from '@vueuse/core'

    const name = ref('')
    const email = ref('')
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

    function send_data(){
        if (comparePassword() & name.value !== '' & email !== '' & agree !== false){

        }
    }

</script>

<template>
    <!-- MAIN CONTENT -->
    <main class="container">
        <div class="row align-items-center justify-content-center vh-100">
            <div class="col-11 col-sm-8 col-md-6 col-lg-5 col-xl-4 col-xxl-3 py-6">

                <!-- Title -->
                <h1 class="mb-2 text-center">
                    Регистрация
                </h1>

                <!-- Subtitle -->
                <p class="text-secondary text-center">
                    Зарегистрируйте свой аккаунт
                </p>

                <!-- Form -->
                <form>
                    <div class="row">
                        <div class="col-12">
                            <div class="mb-4">

                                <!-- Label -->
                                <label class="form-label">
                                    Имя
                                </label>

                                <!-- Input -->
                                <input v-model='name' type="text" class="form-control" placeholder="Даниил" required>
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

                    <div class="row align-items-center text-center">
                        <div class="col-12">

                            <!-- Button -->
                            <button type="button" class="btn w-100 btn-primary mt-6 mb-2">Зарегистрироваться</button>
                        </div>

                        <div class="col-12">

                            <!-- Link -->
                            <small class="mb-0 text-muted">Уже есть аккаунт? <RouterLink class="fw-semibold" to="/login">Войти</RouterLink></small>
                        </div>
                    </div> <!-- / .row -->
                </form>
            </div>
        </div> <!-- / .row -->
    </main> <!-- / main -->
</template>