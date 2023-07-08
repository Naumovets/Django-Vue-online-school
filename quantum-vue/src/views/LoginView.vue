<script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  import VueCookies from 'vue-cookies'
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  const username = ref('')
  const password = ref('')
  const passwordType = ref('password')
  const rememberMe = ref(false)

  function showPassword(){
    if (passwordType.value === 'password'){
      passwordType.value = 'text';
    }else{
      passwordType.value = 'password'
    }
  }

  const url = 'http://127.0.0.1:8000/api/v1/user/auth/token/login'

  let form_data = new FormData();
  function login(){
    if(password.value !== '' & username.value !== ''){
        form_data.append('username', username.value);
        form_data.append('password', password.value)
        axios({
          url: url,
          method: 'post',
          data: form_data,
          headers:{'Content-Type':'multipart/form-data'}
        })
        .then(function (response) {
          if(response.status == 200){
            if(rememberMe){
              VueCookies.set('Authorization' , 'Token ' + response.data.auth_token, "12m") 
            }else{
              VueCookies.set('Authorization' , 'Token ' + response.data.auth_token, "14d") 
            }
            router.push('/success');
          }
          else{
            
          }
          

        });
    }else{
      alert('Введите логин и пароль')
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
                    Вход
                </h1>

                <!-- Subtitle -->
                <p class="text-secondary text-center">
                    Введите имя пользователя и пароль
                </p>

                <!-- Form -->
                <form @submit.prevent="login" id="form">
                    <div class="row">
                        <div class="col-12">
                            <div class="mb-4">

                                <!-- Label -->
                                <label class="form-label">
                                    Имя пользователя
                                </label>

                                <!-- Input -->
                                <input v-model='username' type="text" class="form-control" placeholder="username" required>
                            </div>
                        </div>

                        <div class="col-12">
                            <!-- Password -->
                            <div class="mb-4">

                                <div class="row">
                                    <div class="col">

                                        <!-- Label -->
                                        <label class="form-label">
                                            Пароль
                                        </label>
                                    </div>

                                    <div class="col-auto">
                                        
                                        <!-- Help text -->
                                        <a href="./reset-password-illustration.html" class="form-text small text-muted link-primary">Забыли пароль?</a>
                                    </div>
                                </div> <!-- / .row -->

                                <!-- Input -->
                                <div class="input-group input-group-merge">
                                    <input :type='passwordType' class="form-control" v-model='password' autocomplete="off" data-toggle-password-input placeholder="Пароль.." required>
                                    <button @click="showPassword" type="button" class="input-group-text px-4 text-secondary link-primary" data-toggle-password></button>
                                  </div>
                            </div>
                        </div>
                    </div> <!-- / .row -->

                    <div class="form-check">

                        <!-- Input -->
                        <input v-model="rememberMe" type="checkbox" class="form-check-input" id="remember">

                        <!-- Label -->
                        <label class="form-check-label" for="remember">
                            Запомнить меня
                        </label>
                    </div>

                    <div class="row align-items-center text-center">
                        <div class="col-12">

                            <!-- Button -->
                            <button type="submit" class="btn w-100 btn-primary mt-6 mb-2">Войти</button>
                        </div>

                        <div class="col-12">

                            <!-- Link -->
                            <small class="mb-0 text-muted">Еще нет аккаунта?
                              <RouterLink class="fw-semibold" to="/register">Зарегистрироваться</RouterLink></small>
                        </div>
                    </div> <!-- / .row -->
                </form>
            </div>
        </div> <!-- / .row -->
    </main> <!-- / main -->
</template>
