<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue';

const email = ref('');
const password = ref('');
const router = useRouter();

const handleSubmit = (e) => {
    e.preventDefault();
    router.push('/categories');
}
</script>

<template>
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header">
                    <h3 class="card-title text-center">Login</h3>
                </div>
                <div class="card-body">
                    <form>
                        <div class="mb-3">
                            <label for="email" class="form-label">Email address</label>
                            <input type="email" class="form-control" id="email" placeholder="Enter email" v-model="email">
                        </div>
                        <div class="mb-3">
                            <label for="password" class="form-label">Password</label>
                            <input type="password" class="form-control" id="password" placeholder="Password" v-model="password">
                        </div>
                        <div class="mb-3 form-check">
                            <input type="checkbox" class="form-check-input" id="remember">
                            <label class="form-check-label" for="remember">Remember me</label>
                        </div>
                        <button 
                            type="submit" 
                            class="btn btn-primary w-100"
                            @click="handleSubmit"
                            v-bind:disabled="email.length === 0 || password.length === 0"
                        >
                        Login
                        </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
</div>

</template>

<style scoped>

</style>