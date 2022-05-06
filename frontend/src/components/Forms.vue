<template>

    <form @submit="handleSubmit">
        <label>Home</label>
        <input type="text" v-model="home">
        <label>Destination</label>
        <input type="text" v-model="destn">
        <label>Graph</label><br>
        <div id="all-maps">
            <select v-model="graph">
                <option v-for="i in this.maps" :key="i"> {{i[0]}} </option>
            </select>
        </div>
        <br><br>
        <div v-if="pressedScan" class="stream">
            <qr-stream @decode="onDecode" class="qrStream">
                <div style="color: red;" class="frame"></div>
            </qr-stream>
        </div>
        <div class="submit">
            <button type="button" @click="scanButtonPress">QR Scanner</button>
        </div>
        <div class="submit">
            <button type="button" @click="handleSubmit">Submit</button>
        </div>
        <br>
        <label>Route</label>
        <div v-if="this.route != null" class="route">
            {{this.route}}
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
            orientation : 'front',
            maps : [],
            route : null,
            pressedScan : false
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
            },
        getLastUsedGraph(){
            let lastGraph = localStorage.getItem("lastUsedGraph")
            this.graph = lastGraph
        },
        handleSubmit(){
            console.log("form submitted")
            console.log("Home : ",this.home)
            console.log("destination : ",this.destn)
            console.log("graph : ",this.graph)

            localStorage.setItem("lastUsedGraph",this.graph)

            // API call for calculating route
            const URL = "https://navxe.herokuapp.com/api/route/" + this.graph + "/" +  this.home + "/"+ this.destn + "/" + this.orientation 
            console.log(URL)
            this.axios
                .get(URL)
                .then((response) => {
                    console.log(response.data.route)
                    this.route = response.data.route
                })
        },
        onDecode(decodeStr) {
            console.log(decodeStr)
            this.home = decodeStr
        },
        scanButtonPress(){
            this.pressedScan = !this.pressedScan
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
        align-items: center;
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
    .submit{
        text-align: center;
        align-self: center;
        border: 1px;
        margin: 15%;
        color: #aaa;
        display: inline-block;
        font-size: 16px;
        text-decoration: none;
    }
    .qrStream{
        margin-top: 20px;
        padding-top: 20px;
        display: inline-block;
        margin: 0px;
        align-self: center;
        padding: 0px;
    }
</style>