<script setup>
import { RouterLink } from 'vue-router'
</script>

<template>
    <nav id="mainNavbar" class="navbar navbar-vertical navbar-expand-lg scrollbar bg-white navbar-light">   
        <div class="container-fluid">
            
            <!-- Brand -->
            <span class="navbar-brand text-center">
                <img src="../assets/images/logo.png" class="navbar-brand-img logo-light logo-large" alt="..." width="125">
                <img src="../assets/images/logo-dark.png" class="navbar-brand-img logo-dark logo-large" alt="..." width="125">
            </span>
            

            <a href="javascript: void(0);" class="navbar-toggler collapsed" data-bs-toggle="collapse" data-bs-target="#sidenavCollapse" aria-controls="sidenavCollapse" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </a>

            <!-- Collapse -->
            <div class="collapse navbar-collapse" id="sidenavCollapse">
                <!-- Navigation -->
                <ul class="navbar-nav mb-lg-7">
                    <!-- <li class="nav-item">
                        <RouterLink class="nav-link" to="/">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="nav-link-icon" viewBox="0 0 16 16">
                                <path d="M8.354 1.146a.5.5 0 0 0-.708 0l-6 6A.5.5 0 0 0 1.5 7.5v7a.5.5 0 0 0 .5.5h4.5a.5.5 0 0 0 .5-.5v-4h2v4a.5.5 0 0 0 .5.5H14a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.146-.354L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.354 1.146ZM2.5 14V7.707l5.5-5.5 5.5 5.5V14H10v-4a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5v4H2.5Z"/>
                            </svg>
                            <span>Главная</span>
                        </RouterLink>
                    </li> -->
                    <!-- <li class="nav-item">
                        <RouterLink class="nav-link" to="/calendar">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="nav-link-icon" viewBox="0 0 16 16">
                                <path d="M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM2 2a1 1 0 0 0-1 1v1h14V3a1 1 0 0 0-1-1H2zm13 3H1v9a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V5z"/>
                                <path d="M11 7.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5v-1z"/>
                            </svg>
                            <span>Календарь</span>
                        </RouterLink>
                    </li>
                    <li class="nav-item">
                        <RouterLink class="nav-link" to="/webinar">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="nav-link-icon" viewBox="0 0 16 16">
                                <path d="M13.5 3a.5.5 0 0 1 .5.5V11H2V3.5a.5.5 0 0 1 .5-.5h11zm-11-1A1.5 1.5 0 0 0 1 3.5V12h14V3.5A1.5 1.5 0 0 0 13.5 2h-11zM0 12.5h16a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 0 12.5z"/>
                            </svg>
                            <span>Занятия</span>
                        </RouterLink>
                    </li> -->
                </ul>
                <!-- End of Navigation -->
            </div>
            <!-- End of Collapse -->
        </div>
    </nav>
</template>

<style>
.a{fill:none;stroke:currentColor;stroke-linecap:round;stroke-linejoin:round;stroke-width:1.5px;}
</style>