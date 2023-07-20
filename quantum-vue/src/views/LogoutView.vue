<script setup>

import { useRouter } from 'vue-router'
import VueCookies from 'vue-cookies'
import axios from 'axios'

const router = useRouter();

if (VueCookies.get('Authorization')!==null){
    const url = 'http://127.0.0.1:8000/api/v1/user/auth/token/logout'
    
    axios({
        url: url,
        method: 'post',
        headers: {'Authorization': VueCookies.get('Authorization')}
    });

    VueCookies.set('Authorization', null);
    router.push('/login');
}else{
    router.push('/login')
}


</script>

<template>
    dsds
</template>