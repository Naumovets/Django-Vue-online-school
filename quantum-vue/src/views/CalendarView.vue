<script setup>
import { ref, onMounted } from 'vue';
import { Calendar } from '@fullcalendar/core';
import interactionPlugin from '@fullcalendar/interaction';
import listPlugin from '@fullcalendar/list';
import { checklogin } from '../modules/login'
import { onBeforeMount } from 'vue'
import Sidebar from '../components/sidebar.vue'
import Header from '../components/header.vue'
import Footer from '../components/footer.vue'
import ruLocale from '@fullcalendar/core/locales/ru';
import axios from 'axios';
import VueCookies from 'vue-cookies';
import { useRouter } from 'vue-router';


const calendarRef = ref(null);

onMounted(() => {
	
    const data = ref();
    axios({
            url: 'https://admin.lk-quantum.ru/api/v1/course/calendar_webinar',
            headers: { 'Authorization': VueCookies.get('Authorization') },
            method: 'get',
        })
    .then(function (response) {
        data.value = response.data;
		const calendarEl = calendarRef.value;

    	const calendar = new Calendar(calendarEl, {
    		plugins: [listPlugin, interactionPlugin],
    		initialView: 'listWeek',
    		headerToolbar: {
    	    		left: 'listMonth,listWeek,listDay',
    	    		center: 'title',
    	    		right: 'prev,today,next',
    		},
    		events: data.value,
    		locales: ruLocale,
    		locale: 'ru',
    		firstDay: 1,
			views: {
    			listDay: { buttonText: 'На день' },
    			listWeek: { buttonText: 'На неделю' },
    			listMonth: { buttonText: 'На месяц' },
    		},
		});
		calendar.render();	
    })

});


document.title = 'Расписание'


onBeforeMount(() => {
    checklogin();
});
</script>

<template>
    <Sidebar />
    <main>
        <Header />

        <div class="container-fluid">
            <h1>Расписание</h1>
            <div class="row">
                <div ref="calendarRef"></div>
            </div>
        </div>
    
        <Footer />
    </main>
</template>
  
<style>
/* You can add styles for your calendar here */
</style>
  
