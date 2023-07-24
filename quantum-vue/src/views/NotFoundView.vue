<script setup>

import { checklogin } from '../modules/login.js'
import Footer from '../components/footer.vue'
checklogin();
document.title = 'Ошибка 404 - страница не найдена'

</script>

<template>
    <main class="container">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <div class="row align-items-center justify-content-between vh-100 py-6">
                    <div class="col-lg-6 order-lg-last">
    
                        <!-- Image -->
                        <div class="text-center">
                           <img src="../assets/images/illustrations/error-illustration.svg" alt="..." class="img-fluid">
                        </div>
                   </div>
    
                    <div class="col-lg-6 py-6">
    
                        <!-- Title -->
                        <h1 class="mb-2">Ошибка 404</h1>

                        <!-- Heading -->
                        <p class="text-secondary">Уууууупс.. Похоже такой страницы не существует</p>
    
                        <div class="row align-items-center justify-content-md-between text-center text-md-start">
                            <div class="col-md-auto">

                                <!-- Link -->
                                <RouterLink  class="btn btn-primary mt-3 mb-1" to="/profile">Вернуться в профиль</RouterLink>
                            </div>
                        </div> <!-- / .row -->
                    </div>
                </div> <!-- / .row -->
            </div>
        </div> <!-- / .row -->
        <Footer />
    </main> <!-- / main -->
</template>

<style>
</style>