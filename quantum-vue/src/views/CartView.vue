<script setup>
    import { checklogin } from '../modules/login'
    import { onBeforeMount } from 'vue'
    import Sidebar from '../components/sidebar.vue'
    import Header from '../components/header.vue'
    import Footer from '../components/footer.vue'
    import axios from 'axios'
    import VueCookies from 'vue-cookies'
    import { ref, computed } from 'vue'
    import { useFetch } from '@vueuse/core'
    import { watch } from 'vue'

    const courses = ref(null);
    const promocode = ref('');
    const errorCartItem = ref('')
    const data = ref();
    const jsonCartItem = computed(()=>{
        if(courses.value){
            return courses.value.map(item => ({'id': item.course.id, 'period': item.period }))
        }else{
            return null
        }
    })
    const url = computed(()=>{
        return `http://127.0.0.1:8000/api/v1/cart/price_cart_item?coupon_code=${promocode.value}`
    })


    function getCart(){
        // запрос корзины
        axios({
            url: 'http://127.0.0.1:8000/api/v1/cart/cart',
            headers: { 'Authorization': VueCookies.get('Authorization') },
            method: 'get',
        })
        .then(function (response) {
            courses.value = response.data.map(item => ({ ...item, 'period': 'full' }));
        })
    }

    function deleteCartItem(id){
        axios.delete(
            `http://127.0.0.1:8000/api/v1/cart/cart/${id}`,
            {
                headers: { 'Authorization': VueCookies.get('Authorization') },
            }
            
        )
        .then(function (response) {
            errorCartItem.value = response.data
            getCart();
        })
    }

    checklogin();
    getCart()

    watch([url, jsonCartItem], () => {
            if (courses.value){
                // Функция, которая будет выполнена при изменении переменных courses и url
                const response = useFetch(url, 
                {
                    method: 'POST', 
                    headers: { 
                        'Authorization': VueCookies.get('Authorization'),
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(jsonCartItem.value)
                }).json();
                data.value = response.data
            }
        });

</script>

<template>
    <Sidebar />
    <main>
        <Header />

        <div class="container-fluid">
            <h1>Корзина</h1>
            <div class="row">
                <div class="col-12 order-1 col-lg-9">
                    <div class="card border-0">
                        <div class="card-header border-0 card-header-space-between"><!-- Title -->
                            <h3 class="card-header-title h4 text-uppercase"> Курсы </h3>
                        </div><!-- Table -->
                        <div v-if="errorCartItem" class="mt-2 alert alert-danger" role="alert">
                            {{ errorCartItem.error }}
                        </div>
                        <div class="table-responsive">
                            <table id="projectsTable" class="table align-middle table-edge table-nowrap mb-0">
                                <thead class="thead-light">
                                    <tr>
                                        <th>Название</th>
                                        <th class="period">Период:</th>
                                        <th>Стоимость</th>
                                        <th class="text-end">Удалить</th>
                                    </tr>
                                </thead>
                                <tbody v-for="course in courses">
                                    <tr>
                                        <td class="fw-bold">
                                            <span>
                                                {{course.course.title}} 
                                                <span class="badge text-bg-primary">{{ course.course.status }}</span>
                                                <span class="badge text-bg-success ms-2">{{ course.course.subject }}</span>
                                            </span>
                                        </td>
                                        <td>
                                            <select v-model="course.period" class="form-select form-select-sm" aria-label=".form-select-sm example">

                                                <option value="full" selected>Полный курс</option>
                                            
                                                <option value="month">Месяц</option>
                                            
                                            </select>
                                        </td>
                                        <td>
                                            <span v-if="course.period == 'month'">{{course.course.price}} ₽.</span>
                                            <span v-else>{{course.course.full_price}} ₽.</span>
                                        </td>
                                        <td>
                                            <button @click="deleteCartItem(course.course.id)" type="button" class="btn btn-outline-primary">X</button>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div><!-- / .table-responsive -->
                    </div>
                </div>

                <div class="col-12 order-2 col-lg-3">
                    <div class="card border-0">
                        <div class="card-body mt-5 pt-0">
                            <h3>Детали</h3>
                            <label for="validationCustom01" class="form-label">Промокод</label>
                            <input v-model="promocode" type="text" class="form-control" id="validationCustom01" required>
                            <div v-if="data.value.error" class="mt-2 alert alert-danger" role="alert">
                                {{data.value.error}}
                            </div>
                            <div v-if="data.value.response" class="mt-2 alert alert-success" role="alert">
                                {{data.value.response}}
                            </div>
                            <hr>
                            <span class="mb-2 form-label">Цена без скидки:</span>
                            <p class="mb-0">{{ data.value.price }} ₽.</p>
                            <hr>
                            <span class="mb-2 form-label">Итого:</span>
                            <div class="d-flex align-items-center justify-content-between">
                                <span>{{data.value.price_with_discount}} ₽</span>
                                <button type="button" class="btn btn-outline-primary">Оплатить</button>
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
    th.period{
        min-width: 150px;
    }
</style>