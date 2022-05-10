<template>

    <form @submit="handleSubmit" id="main-form">
        <label>Home</label>
        <input @keypress="searchFuncHome" type="text" id="home-text-main">
        <div id="searchDropdownHome" class="dropdownSearchText">

            <!--<ul v-for="h in JSON.parse(JSON.stringify(this.searchThrough)).homeNodes" :key="h">-->
            <ul v-for="h in this.result_array_home" :key="h">
                <li @click="clickList(h,'home')">{{h}}</li>
            </ul>

        </div>

        <label>Destination</label>
        <input @keypress="searchFuncDestn" type="text" id="destn-text-main">
        <div id="searchDropdownDestn" class="dropdownSearchText">
            <ul v-for="h in this.uniqueDestn" :key="h">
                <li @click="clickList(h,'destn')">{{h}}</li>
            </ul>
        </div>

        <label>Graph</label><br>
        <div id="all-maps">
            <select id="selected-graph" v-model="graph">
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
        <div class="qrBtn">
            <button type="button" @click="handleSubmit">Submit</button>
        </div>
        <br>

        <label>Route</label>
        <div v-if="this.route != null" class="route">
            <div v-for="j in this.route" :key="j">
                <div class="toDoLabel">
                    <p>{{j[0]}}</p>
                </div>
                <div class="toDo">
                    <input type="checkbox"/>
                </div>
            </div>
        </div>
    </form>
    
</template>

<script>

export default {
    inject:['currentPage','pagesArray'], //For adding swipe gestures
    setup(){

    },
    data(){
        return {
            home : '',
            destn : '',
            graph : '',
            orientation : 'front',
            maps : [],
            route : null,
            pressedScan : false,
            currGraphData : '',
            searchThrough : Object(),
            SQ_obj_h : null,
            SQ_obj_d : null,
            result_array_home : [],
            result_array_destn : [],
            uniqueDestn : null,
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
            const URL = "https://navxe.herokuapp.com/api/route/" + this.graph + "/" +  document.getElementById("home-text-main").value.toLowerCase() + "/"+ document.getElementById("destn-text-main").value.toLowerCase() + "/" + this.orientation 
            console.log(URL)
            this.axios
                .get(URL)
                .then((response) => {
                    console.log(response.data.route)
                    this.route = response.data.route
                })
        },
        onDecode(decodeStr) {
			const decodeStrObj = JSON.parse(decodeStr)
			console.log(decodeStrObj)
            this.home = decodeStrObj.nodeName.toLowerCase()
			this.graph = decodeStrObj.graph
			this.orientation = decodeStrObj.orientation
            this.scanButtonPress()
        },
        scanButtonPress(){
            this.pressedScan = !this.pressedScan
        },
        setDefaultGraph(){
            this.graph = localStorage.getItem("defaultGraph")
            document.getElementById("selected-graph").value = this.graph
        },
        isUpdate(){
            const URL = "https://navxe.herokuapp.com/api/update"
            this.axios
                .get(URL)
                .then((response) => {
                    console.log(response)
                    let updateAvail = response.data.hasNewUpdate
                    if (updateAvail == true || updateAvail == "true"){
                        console.log("There is an update available");
                        let currVer = localStorage.getItem("version")
                        if (currVer != response.data.version) {
                            console.log(response.data.version)
                            window.location.reload();
                            localStorage.setItem("version",response.data.version)
                        }
                    }
                })
            
        },
        setHomeAndDestnNodes(){

            const curr_graph = document.getElementById("selected-graph").value 

            if (this.curr_graph == "" || this.curr_graph === undefined){
                this.curr_graph = localStorage.getItem("lastUsedGraph")
            }

            const URL = "https://navxe.herokuapp.com/api/database/read/" + this.curr_graph
            this.axios
                .get(URL)
                .then((response) => {
                    this.currGraphData = response.data.result[0][0]
                    this.currGraphData = JSON.parse(this.currGraphData)

                    const searchThroughHomeProxy= Object.keys(this.currGraphData)
                    const searchThroughDestnProxy = Object.values(this.currGraphData)
                    
                    /*
                        [INFO] Data is stored as proxy convert it into relevant key, values when needed
                    */

                    const searchObj = {"homeNodes" : JSON.parse(JSON.stringify(searchThroughHomeProxy)), "destnNodes" : JSON.parse(JSON.stringify(searchThroughDestnProxy))};

                    this.searchThrough = searchObj;

                    this.result_array_home = JSON.parse(JSON.stringify(this.searchThrough)).homeNodes
                    this.result_array_destn = JSON.parse(JSON.stringify(this.searchThrough)).destnNodes

                    this.setUniqueDestn(this.searchThrough);

                })
        },
        searchFuncHome(){
            document.getElementById("searchDropdownDestn").style.display = "none";
            document.getElementById("searchDropdownHome").style.display = "block";
            let searchQueryTyped = document.getElementById("home-text-main").value.toLowerCase()
            this.SQ_obj_h = JSON.parse(JSON.stringify(this.searchThrough)).homeNodes
            let result_array = []

            for (let iter = 0; iter < this.SQ_obj_h.length; iter++){
                if (this.SQ_obj_h[iter].includes(searchQueryTyped)){
                    result_array.push(this.SQ_obj_h[iter])
                }
            }
            console.log(result_array)

            this.result_array_home = result_array
            //JSON.parse(JSON.stringify(this.searchThrough)).homeNodes = result_array

        },
        searchFuncDestn(){
            document.getElementById("searchDropdownHome").style.display = "none";
            document.getElementById("searchDropdownDestn").style.display = "block";
            let keys_pressed = document.getElementById("destn-text-main").value
        },
        clickList(a,li){
            console.log("you selected : ",a);

            if (li == "home"){
                document.getElementById("searchDropdownHome").style.display = "none";
                document.getElementById("home-text-main").value = a
                this.home = a
                document.getElementById("searchDropdownDestn").style.display = "none";
            }
            else if (li == "destn"){
                document.getElementById("searchDropdownDestn").style.display = "none";
                document.getElementById("destn-text-main").value = a
                this.destn = a
                document.getElementById("searchDropdownHome").style.display = "none";
            }
        },
        setUniqueDestn(prx){
            let destnLi = JSON.parse(JSON.stringify(prx)).destnNodes;
            destnLi.push.apply(destnLi,this.searchThrough.homeNodes)
            const trackLi = [].concat(...destnLi);
            const trackLiUnique = [...new Set(trackLi)];
            this.uniqueDestn = trackLiUnique.sort()
            console.log(this.uniqueDestn)
        },
        defocusAll(){
            console.log("detected click outside")
        }
        },
    mounted(){
        this.fetchAllMaps()
        this.setHomeAndDestnNodes()
        this.setDefaultGraph()
        console.log(this.currentPage,this.pagesArray)
    },
    created(){
        this.isUpdate()
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
    ul{
        list-style-type: none;
        align-items: center;
        align-content: center;
    }
    li{
        align-content: center;
        align-items: center;
        align-self: center;
        margin: 10px;
        padding: 5px;
    }
    .submit{
        text-align: center;
        align-self: center;
        margin: 15px;
        color: #aaa;
        font-size: 16px;
        text-decoration: none;
        display: block;
    }
    .qrBtn{
        text-align: center;
        display: block;
        align-self: center;
        border: none;
        color: #aaa;
        font-size: 16px;
        text-decoration: none;
        margin: 10px;
    }
    .qrStream{
        margin-top: 20px;
        padding-top: 20px;
        margin: 0px;
        align-self: center;
        padding: 0px;
    }
    .toDo{
        display: inline-block;
        position: relative;
        vertical-align: middle;
    }
    .toDoLabel{
        display: inline-block;
        position: relative;
        top: 0px; 
    }
    .dropdownSearchText{
        visibility: visible;
        display: none;
        max-height: 200px;
        overflow: auto;
    }
    .dropdownSearchText{
        align-items: center;
        text-align: left;

    }
</style>