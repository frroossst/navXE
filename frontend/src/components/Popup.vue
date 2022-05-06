<template>
    <div class="card">
        Disclaimer
        <button @click="toggle = !toggle">Close</button>
        <teleport to="#main-form" v-if="toggle">
            <p>Message</p>
        </teleport>
    </div>
</template>

<script>
import { ref } from 'vue'
export default {
    setup(){
        return {toggle: ref(false)}
    }
}
</script>

<style scoped>

</style>