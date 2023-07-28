<script setup>
    import { ref } from 'vue'
    import { checklogin } from '../modules/login'
    import { toRaw } from 'vue'
    import { onBeforeMount, onMounted } from 'vue'
    import Sidebar from '../components/sidebar.vue'
    import Header from '../components/header.vue'
    import Footer from '../components/footer.vue'
    import axios from 'axios'
    import VueCookies from 'vue-cookies'

    const data = ref();
    const main = ref(true);
    const free = ref(true);
    const special = ref(true);
    const exams = ref()
    const subjects = ref()


    function getCourses(){
        // запрос курсов
        axios({
            url: 'https://admin.lk-quantum.ru/api/v1/course/courses',
            headers: { 'Authorization': VueCookies.get('Authorization') },
            method: 'get',
        })
        .then(function (response) {
            data.value = response.data
        })
    }
    

    // запрос экзаменов (всех)
    axios({
        url: 'https://admin.lk-quantum.ru/api/v1/course/exams',
        method: 'get',
    })
    .then(function (response) {
        exams.value = response.data.map(item => ({ 'title': item.title, 'active': true }));
    })

    // запрос предметов (всех)
    axios({
        url: 'https://admin.lk-quantum.ru/api/v1/course/subjects',
        method: 'get',
    })
    .then(function (response) {
        subjects.value = response.data.map(item => ({ 'title': item.title, 'exam': item.exam, 'active': true }));
    })


    // Проверка активных экзаменов (для вывода курсов)
    function IsActiveExam(sub_exam){
        let card_exam = JSON.stringify({'title': sub_exam, 'active': true});
        for (let i = 0; i < toRaw(exams.value).length; i++){
            if( JSON.stringify(toRaw(exams.value)[i] ) === card_exam ){
                return true;
            }
        }
        return false;
    }

    // Проверка активных курсов (для вывода курсов)
    function IsActiveSubject(subject, exam){
        let card_exam = JSON.stringify({'title': subject, 'exam': exam, 'active': true});
        for (let i = 0; i < toRaw(subjects.value).length; i++){
            if( JSON.stringify(toRaw(subjects.value)[i] ) === card_exam ){
                return true;
            }
        }
        return false;
    }

    function deleteCartItem(id){
        axios.delete(
            `https://admin.lk-quantum.ru/api/v1/cart/cart/${id}`,
            {
                headers: { 'Authorization': VueCookies.get('Authorization') },
            }
            
        )
        .then(function (response) {
            getCourses();
        })
    }

    function addToCart(id){
        const form_data = new FormData()
        form_data.append('id', id)
        axios({
            url: 'https://admin.lk-quantum.ru/api/v1/cart/cart',
            method: 'post',
            data: form_data,
            headers: { 'Authorization': VueCookies.get('Authorization') },
        })
        .then(function (response) {
            getCourses();
        })
    }

    function addFreeCourseOrderItem(id){
        axios({
            url: `https://admin.lk-quantum.ru/api/v1/order/add_free_course/${id}`,
            method: 'post',
            headers: { 'Authorization': VueCookies.get('Authorization') },
        })
        .then(function (response) {
            getCourses();
        })
        .catch(function (error){
            alert('Произошла ошибка\nВы можете написать нам об ошибке в группе ВК')
        })
    }

    onBeforeMount(() => {
        checklogin();
        getCourses();
    }); 


    document.title = 'Каталог курсов'

</script>

<template>
    <Sidebar />
    <main>
        <Header />

        <div class="container-fluid">
            <div class="row">
                <h1>Каталог курсов</h1>
                <router-link class="h4" to="/cart">Перейти в корзину</router-link>
            </div>
            
            <div class="row">
                <div class="col-12 order-lg-1 order-2 col-lg-9">
                    <template v-if="data !== undefined">
                        <div class="card shadow-none border-0" v-for="card in data" :key="card.id">
                            <div v-if="((card.status == 'Основной' && main)
                                    || (card.status == 'Бесплатный' && free)
                                    || (card.status == 'Спецкурс' && special))
                                    && IsActiveExam(card.subject.exam)
                                    && IsActiveSubject(card.subject.title, card.subject.exam)
                                " class="row g-0">
                                <div class="col-lg-3 col-12">

                                    <img :src="'https://admin.lk-quantum.ru' + card.image" class="w-100 img-fluid rounded-start"
                                        alt="...">

                                </div>

                                <div class="col-md-6">

                                    <div class="card-body pt-2 h-100 d-flex flex-column justify-content-between">
                                        <div>
                                            <span class="badge text-bg-primary">{{ card.subject.exam }}</span>
                                            <span class="badge text-bg-info ms-2">{{ card.subject.title }}</span>
                                            <span class="badge text-bg-success">{{ card.status }}</span>
                                        </div>
                                        <h3 class="card-title">
                                            {{ card.title }}
                                        </h3>

                                        <div class="d-flex align-items-center">
                                            <div class="d-md-block d-none avatar avatar-circle avatar-xs">
                                                <img v-if="card.teacher.image" width="100%" :src="'https://admin.lk-quantum.ru' + card.teacher.image" class="avatar-title">
                                                <img v-else width="100%" src="../assets/images/profiles/student.png" class="avatar-title">
                                            </div>
                                            <p class="mb-0 ms-2">{{ card.teacher.first_name }} {{ card.teacher.last_name }}</p>
                                        </div>

                                    </div>

                                </div>

                                <div class="col-md-3">
                                    <div class="card-body h-100 d-flex flex-column justify-content-around">
                                        <p v-if="card.price" class="mb-0 price">{{ card.price }} ₽/мес.</p>
                                        <p v-else class="mb-0 price">Бесплатно</p>
                                        <div>
                                            <button v-if="card.price && !card.isAddedToCart" @click="addToCart(card.id)" type="button" class="btn btn-success">В корзину</button>
                                            <button v-else-if="card.isAddedToCart" @click="deleteCartItem(card.id)" type="button" class="btn btn-success">Удалить</button>
                                            <button v-else-if="!card.isAddedToOrder" @click="addFreeCourseOrderItem(card.id)" type="button" class="btn btn-success">Получить</button>
                                        </div>

                                    </div>

                                </div>
                            </div>
                        </div>
                    </template>

                </div>

                <div class="col-12 order-lg-2 order-1 col-lg-3">
                    <div class="card border-0">
                        <div class="card-body mt-5 pt-0">
                            <h3>Фильтр</h3>
                            <h5 class="mb-2">Экзамены</h5>
                            <div v-for="exam in exams" class="form-check mb-3">
                                <input v-model="exam.active" type="checkbox" id="formCheck2" class="form-check-input"
                                    checked>
                                <label class="form-check-label" for="formCheck2">{{ exam.title }}</label>
                            </div>
                            <hr>
                            <h5 class="mb-2">Предметы</h5>
                            <template v-for="subject in subjects">
                                <div v-if="IsActiveExam(subject.exam)" class="form-check mb-3">
                                    <input v-model="subject.active" type="checkbox" id="formCheck2" class="form-check-input" checked>
                                    <label class="form-check-label" for="formCheck2">{{subject.title}}({{subject.exam}})</label>
                                </div>
                            </template>
                            
                            <hr>
                            <h5 class="mb-2">Тип</h5>
                            <div class="form-check mb-3">
                                <input v-model="main" type="checkbox" id="formCheck2" class="form-check-input" checked>
                                <label class="form-check-label" for="formCheck2">Основной</label>
                            </div>
                            <div class="form-check mb-3">
                                <input v-model="special" type="checkbox" id="formCheck2" class="form-check-input" checked>
                                <label class="form-check-label" for="formCheck2">Спецкурс</label>
                            </div>
                            <div class="form-check mb-3">
                                <input v-model="free" type="checkbox" id="formCheck2" class="form-check-input" checked>
                                <label class="form-check-label" for="formCheck2">Бесплатный</label>
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
p.price {
    font-size: 20px;
}
</style>