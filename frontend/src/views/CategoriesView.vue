<script setup>
    import DataCard from '../components/CategoryCard.vue';
    import { ref } from 'vue';

    const items = ref([
        { id: 1, name: 'Name 1' },
        { id: 2, name: 'Name 2' },
        { id: 3, name: 'Name 3' },
        { id: 4, name: 'Name 4' },
        { id: 5, name: 'Name 5' },
        { id: 6, name: 'Name 6' },
    ]);
</script>

<template>
    <div class="container">
        <div class="row">
            <div v-for="item in items" :key="item.id" class="col-sm-12 col-md-6 col-lg-4 col-xl-3 d-flex align-items-stretch">
                <data-card :data="item"></data-card>
            </div>
        </div>
    </div>
</template>
