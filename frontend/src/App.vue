<script setup>
import { RouterLink, RouterView } from 'vue-router'
import NavbarVue from './components/Navbar.vue'
import { onMounted} from 'vue'
onMounted(() => {
  document.documentElement.setAttribute('data-bs-theme', 'dark');
})
</script>

<template>
  <body >
    <NavbarVue></NavbarVue>
    <RouterView />
  </body>
  


</template>

<style>

</style>

