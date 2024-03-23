<script setup>
    import { defineProps } from 'vue';

const props = defineProps({
    data: {
        type: Object,
        required: true,
        },
    }
);

const showInfo = () => {
    alert( props.data.name );       
}


</script>

<template>
    <div class="card bg-primary m-2 rounded text-center flex-fill" @click="showInfo">
        <div class="card-body" >
            {{ props.data.name }}
        </div>
    </div>
</template>

<style scoped>
    .card {
        flex: 1 1 auto;
        min-width: 100px; 
        max-width: calc(100% / var(--cards-per-row)); 
    }
</style>