<template>

    <form>
        <label>Home</label>
        <input type="text" v-model="home">
        <label>Destination</label>
        <input type="text" v-model="destn">
        <label>Graph</label><br>
        <div id="all-maps">
            <select>
                <option v-for="i in this.maps" :key="i"> {{i[0]}} </option>
            </select>
        </div>
    </form>
    
</template>

<script>

export default {
    data(){
        return {
            home : '',
            destn : '',
            graph : '',
            maps : []
        }
    },
    methods:{
        fetchAllMaps(){
            const URL = "https://navxe.herokuapp.com/api/database/read/*"
            this.axios
                .get(URL)
                .then((response) => {
                    this.maps = response.data.result
                    console.log(this.maps)
                })
            }
        },
    mounted(){
        this.fetchAllMaps()
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
    select{
        width: 100%;
        padding: 10px 15px;
        border: none;
    }
        box-sizing: border-box;
</style>