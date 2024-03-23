<template>
  <table class="table">
    <thead>
      <tr>
        <th scope="col">Item</th>
        <th scope="col" v-for="hour in hours" :key="hour">{{ hour }}</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(item, itemIndex) in items" :key="itemIndex">
        <td>{{ item.name }}</td>
        <td v-for="(hour, hourIndex) in hours" :key="hourIndex" :class="{'table-info': isReserved(itemIndex, hourIndex)}">
          <span v-if="isReserved(itemIndex, hourIndex)">
            {{ getReservationInfo(itemIndex, hourIndex) }}
          </span>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
import { ref } from 'vue';

const hours = ref(['9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00']);
const items = ref([
  { name: 'Item 1', reservations: [{ startHour: 10, endHour: 12, customer: 'John Doe' }] },
  { name: 'Item 2', reservations: [] },
  // Add more items as needed
]);

const isReserved = (itemIndex, hourIndex) => {
  const item = items.value[itemIndex];
  const hour = parseInt(hours.value[hourIndex].split(':')[0], 10);
  for (const reservation of item.reservations) {
    if (hour >= reservation.startHour && hour < reservation.endHour) {
      return true;
    }
  }
  return false;
};

const getReservationInfo = (itemIndex, hourIndex) => {
  const item = items.value[itemIndex];
  const hour = parseInt(hours.value[hourIndex].split(':')[0], 10);
  for (const reservation of item.reservations) {
    if (hour === reservation.startHour) {
      return `${reservation.customer} (${reservation.startHour}:00 - ${reservation.endHour}:00)`;
    }
  }
  return '';
};
</script>
