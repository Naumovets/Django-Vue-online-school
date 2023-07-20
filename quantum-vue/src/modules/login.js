

import { useRouter } from 'vue-router'
import VueCookies from 'vue-cookies';
import axios from 'axios'


export function checklogin(){
    const router = useRouter();
    const url = 'http://127.0.0.1:8000/api/v1/user/check_token/'
    
    axios({
        url: url,
        method: 'get',
        headers: {'Authorization': VueCookies.get('Authorization')}
    })
    .catch(error=>(router.push('/login')))
}

export function isAuthorized(){
    const router = useRouter();
    const url = 'http://127.0.0.1:8000/api/v1/user/check_token/'
    axios({
        url: url,
        method: 'get',
        headers: {'Authorization': VueCookies.get('Authorization')}
    })
    .then(response=>(router.push('/profile')))
}