<script setup>
    import { ref } from 'vue'
    import { checklogin } from '../modules/login'
    import { toRaw } from 'vue'
    import { onBeforeMount, onMounted } from 'vue'
    import Sidebar from '../components/sidebar.vue'
    import Header from '../components/header.vue'
    import Footer from '../components/footer.vue'
    import { useRouter } from 'vue-router'
    import axios from 'axios'
    import VueCookies from 'vue-cookies'

    const orderItems = ref()


    axios({
    url: 'https://admin.lk-quantum.ru/api/v1/course/get-courses',
    method: 'get',
    headers: {'Authorization': VueCookies.get('Authorization')}
})
.then(function(response){
    orderItems.value = response.data
})
.catch(function(response){
    orderItems.value = null
})

onBeforeMount(() => {
    checklogin();
});

const router = useRouter();

function extend_course(id){
    const form_data = new FormData()
    form_data.append('id', id)
    axios({
        url: `https://admin.lk-quantum.ru/api/v1/order/extend_course/`,
        method: 'post',
        data: form_data,
        headers: { 'Authorization': VueCookies.get('Authorization') },
    })
    .then(function (response) {
        router.push('/cart')
    })
    .catch(function (error){
        alert('Произошла ошибка\nВы можете написать нам об ошибке')
    })
}

document.title = 'Мои курсы'

</script>

<template>
    <Sidebar />
    <main>
        <Header />

        <div class="container-fluid">
            <div class="row">
                <h1>Мои курсы</h1>
            </div>
            
            <div class="row">
                <div class="col-12">
                    <template v-if="orderItems !== undefined && orderItems !== null ">
                        <div class="card shadow-none border-0" v-for="orderItem in orderItems">
                            <div class="row g-0">
                                <div class="col-lg-3 col-12">

                                    <img :src="'https://admin.lk-quantum.ru' + orderItem.course.image" class="w-100 img-fluid rounded-start"
                                        alt="...">

                                </div>

                                <div class="col-md-6">

                                    <div class="card-body pt-2 h-100 d-flex flex-column justify-content-between">
                                        <div>
                                            <span class="badge text-bg-primary">{{ orderItem.course.exam }}</span>
                                            <span class="badge text-bg-info ms-2">{{ orderItem.course.subject}}</span>
                                            <span class="badge text-bg-success ms-2">{{ orderItem.course.status }}</span>
                                        </div>
                                        <h3 class="card-title">
                                            {{ orderItem.course.title }} <span v-if="orderItem.active == false">(неактивен)</span>
                                        </h3>

                                        <div class="d-flex align-items-center">
                                            <div class="avatar avatar-circle avatar-xs">
                                                <img v-if="orderItem.course.teacher.image" width="100%" :src="'https://admin.lk-quantum.ru' +orderItem.course.teacher.image" class="avatar-title">
                                                <img v-else width="100%" src="../assets/images/profiles/student.png" class="avatar-title">
                                            </div>
                                            <p class="mb-0 ms-2">{{ orderItem.course.teacher.first_name }} {{ orderItem.course.teacher.last_name }}</p>
                                        </div>

                                    </div>

                                </div>

                                <div class="col-8 col-sm-6 col-md-5 col-lg-3">
                                    <div class="card-body h-100 d-flex flex-row flex-lg-column justify-content-around align-items-center">
                                        <div>
                                            <RouterLink v-if="orderItem.active == true" :to="'course/'+orderItem.course.slug" type="button" class="btn btn-success">Перейти</RouterLink>
                                            <button v-else @click="extend_course(orderItem.course.id)" class="btn btn-success">Продлить</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </template>
                </div>
            </div>
        </div>

        <Footer />
    </main>
</template>

<style>
p.price {
    font-size: 20px;
}
</style>