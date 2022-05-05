<template>
    <form>
        <label>Home</label>
        <input type="text" v-model="home">
        <label>Destination</label>
        <input type="text" v-model="destn">
    </form>

    <p>
       Calculating route from {{home}} to {{destn}} 
    </p>
    
</template>

<script>
export default {
    data(){
        return {
            home : '',
            destn : ''
        }
    }
}
</script>

<style scoped>
    form {
        max-width: 420px;
        margin: 30px auto;
        background: whitesmoke;
        text-align: left;
        padding: 40px;
        border-radius: 10px;
    }
    label {
        color: #aaa;
        display: inline-block;
        margin: 25px 0 15px;
        font-size: 0.6em;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: bold;
    }
    input {
        display: block;
        padding: 10px 6px;
        width:  100%;
        box-sizing: border-box;
        border: none;
        border-bottom: 1px solid #ddd;
        color: #555;
    }
</style>