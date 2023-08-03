<script setup>
import { ref, onMounted } from 'vue';
import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import interactionPlugin from '@fullcalendar/interaction';
import { checklogin } from '../modules/login'
import { onBeforeMount } from 'vue'
import Sidebar from '../components/sidebar.vue'
import Header from '../components/header.vue'
import Footer from '../components/footer.vue'
import ruLocale from '@fullcalendar/core/locales/ru';

const calendarRef = ref(null);

onMounted(() => {
    const calendarEl = calendarRef.value;

    const calendar = new Calendar(calendarEl, {
        plugins: [dayGridPlugin, timeGridPlugin],
        initialView: 'dayGridMonth',
        headerToolbar: {
            left: 'dayGridMonth,timeGridWeek,timeGridDay',
            center: 'title',
            right: 'prev,today,next',
        },
        events: [
            // You can add your events here
            { title: 'My Event', start: '2023-08-03T10:00:00' }
        ],
        locales: ruLocale,
        locale: 'ru',
        firstDay: 1,
    });

    calendar.setOption('locale', 'ru');

    calendar.render();
});


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
  