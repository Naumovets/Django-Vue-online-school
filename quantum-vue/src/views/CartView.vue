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
    const data = ref({response:'', error: ''});
    const jsonCartItem = computed(()=>{
        if(courses.value){
            return courses.value.map(item => ({'id': item.course.id, 'period': item.period }))
        }else{
            return null
        }
    })
    const url = computed(()=>{
        return `https://admin.lk-quantum.ru/api/v1/cart/price_cart_item?coupon_code=${promocode.value}`
    })

    document.title = 'Корзина'


    function getCart(){
        // запрос корзины
        axios({
            url: 'https://admin.lk-quantum.ru/api/v1/cart/cart',
            headers: { 'Authorization': VueCookies.get('Authorization') },
            method: 'get',
        })
        .then(function (response) {
            courses.value = response.data.map(item => ({ ...item, 'period': 'full' }));
        })
    }

    function deleteCartItem(id){
        axios.delete(
            `https://admin.lk-quantum.ru/api/v1/cart/cart/${id}`,
            {
                headers: { 'Authorization': VueCookies.get('Authorization') },
            }
            
        )
        .then(function (response) {
            errorCartItem.value = response.data
            getCart();
        })
    }

    function addOrderItems(){
        if(!data.value.error){
            axios.post(`https://admin.lk-quantum.ru/api/v1/order/add_order_items/${promocode.value}`, jsonCartItem.value, {
                headers: {
                    'Authorization': VueCookies.get('Authorization'),
                    'Content-Type': 'application/json'
                }
            })
            .then(function (response) {
                // <form name="t-payform" onsubmit="pay(this); return false;">
                //     <input class="t-payform-row" type="hidden" name="terminalkey" value="1690624343703DEMO">
                //     <input class="t-payform-row" type="hidden" name="frame" value="false">
                //     <input class="t-payform-row" type="hidden" name="language" value="ru"> 
                //     <input class="t-payform-row" type="hidden" value="2000" name="amount" required>
                //     <input class="t-payform-row" type="text" placeholder="Номер заказа" name="order">
                //     <input class="t-payform-row" type="text" placeholder="Описание заказа" name="description">
                //     <input class="t-payform-row" type="text" placeholder="ФИО плательщика" name="name">
                //     <input class="t-payform-row" type="text" placeholder="E-mail" name="email">
                //     <input class="t-payform-row" type="text" placeholder="Контактный телефон" name="phone">
                //     <input class="t-payform-row" type="submit" value="Оплатить">
                // </form>
                const price = response.data.price;
                const orderId = response.data.id;
                const phone = response.data.phone;
                form_data = new FormData()
                form_data.append('terminalkey', '1690624343703DEMO');
                form_data.append('frame', 'false');
                form_data.append('language', 'ru');
                form_data.append('amount', price.value);
                form_data.append('order', orderId.value);
                form_data.append('phone', phone.value);
                return form_data;
            })
            .catch(function(error){
                alert('Что-то пошло не так, заявите об этом в поддержку!')
            })
        }else{
            axios.post('https://admin.lk-quantum.ru/api/v1/order/add_order_items/', jsonCartItem.value, {
                headers: {
                    'Authorization': VueCookies.get('Authorization'),
                    'Content-Type': 'application/json'
                }
            })
            .then(function (response) {
                const price = response.data.price;
                const orderId = response.data.id;
                const phone = response.data.phone;
                form_data = new FormData()
                form_data.append('terminalkey', '1690624343703DEMO');
                form_data.append('frame', 'false');
                form_data.append('language', 'ru');
                form_data.append('amount', price.value);
                form_data.append('order', orderId.value);
                form_data.append('phone', phone.value);
                return form_data;
            })
            .catch(function(error){
                alert('Что-то пошло не так, заявите об этом в поддержку!')
            })
        }
    }
    
    onBeforeMount(() => {
        checklogin();
        getCart();
    });

    watch([url,jsonCartItem], () => {
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

    // Добавляем скрипт Tinkoff
    const script = document.createElement('script');
    script.src = 'https://securepay.tinkoff.ru/html/payForm/js/tinkoff_v2.js';
    script.async = true;
    document.body.appendChild(script);
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
                            <template v-if="data.value !== null && data.value !== undefined && courses !== null && courses !== undefined">
                                <div v-if="data.value.error !== null && data.value.error !== undefined" class="mt-2 alert alert-danger" role="alert">
                                    {{data.value.error}}
                                </div>
                                <div v-if="data.value.response !== null && data.value.response !== undefined" class="mt-2 alert alert-success" role="alert">
                                    {{data.value.response}}
                                </div>
                                <hr>
                                <span class="mb-2 form-label">Цена без скидки:</span>
                                <p class="mb-0">{{ data.value.price }} ₽.</p>
                                <hr>
                                <span class="mb-2 form-label">Итого:</span>
                                <div class="d-flex align-items-center justify-content-between">
                                    <span>{{data.value.result_price}} ₽</span>
                                    <form name="t-payform" onsubmit="form_data=addOrderItems(); pay(form_data); return false;">
                                        <button :disabled="courses.length==0" type="button" class="btn btn-outline-primary">Оплатить</button>
                                    </form>
                                </div>
                            </template>
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