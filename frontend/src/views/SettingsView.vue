<template>

   <div class="formBG">
   <label>Graph</label><br>
   <div id="all-maps">
       <select id="selected-graph" v-model="graph">
           <option v-for="i in this.maps" :key="i"> {{i[0]}} </option>
       </select>
   </div>
   <br><br>
   <label>Version</label> <br>
   <p id="app-version">
      Unable to view version
   </p>
   <div class="submit">
      <button type="button" @click="resetSettings">Reset</button>
   </div>
   <br>
   <div class="submit">
      <button type="button" @click="saveSettings">Save</button>
   </div>
   <br>
   <div class="submit">
      <button type="button" @click="wakeUpAPI">Wake Up</button>
   </div>
   <br><br>
   <p v-if="wakeUpCall" id="wakeUp-status" class="formBG">
      <center>
         <font color="#42b983">
         <b>API is awake!</b>
         </font>
      </center>
   </p>
   <p v-if="!wakeUpCall" id="wakeUp-status" class="formBG">
      <center>
         <font color="#ff0000">
         <b>API is asleep!</b>
         </font>
      </center>
   </p>
   <p v-if="recentSave" id="save-status" class="formBG">
      <center>
         <font color="#42b983">
         <b>Saved!</b>
         </font>
      </center>
   </p>
   <p v-if="recentReset" id="reset-status" class="formBG">
      <center>
         <font color="#42b983">
         <b>Restored to default</b>
         </font>
      </center>
   </p>

   </div>

</template>

<script>

export default  {
   setup(){
         //document.getElementById("selected-graph").value = this.graph
   },
   data() {
      return {
         graph : '',
         maps : [],
         recentSave : false,
         recentReset : false,
         wakeUpCall : false,
         defaultGraph : localStorage.getItem("defaultGraph")
      }
   },
   methods:{
      setGraph(graph){
         sessionStorage.setItem("savedGraph",graph)
      },
      fetchAllMaps(){
         console.log("fetching maps")
         const URL = "https://navxe.herokuapp.com/api/database/read/*"
         this.axios
             .get(URL)
             .then((response) => {
                 this.maps = response.data.result
                 console.log(this.maps)
             })
         },
      saveSettings(){
            let saveGraph = document.getElementById("selected-graph").value
            localStorage.setItem("defaultGraph",saveGraph) 
            this.recentSave = true
      },
      resetSettings(){
            localStorage.removeItem("defaultGraph")
            this.recentReset = true
            //window.location.reload(true)
      },
      async getVersion() {

            const URL = "https://navxe.herokuapp.com/api/update"

            const request = await this.axios.get(URL)

            const responseData = request.data.version

            document.getElementById("app-version").firstChild.data = responseData

            console.log("version from API",responseData)
            //console.log("local version",localVersion)

            /*if (localVersion != responseData){
               if (this.recentUpdate == false){
               localStorage.setItem("version",responseData)
               window.location.reload(true)
               this.recentUpdate = true
               document.getElementById("app-version").firstChild.data = responseData
            }
            }*/
      },
      async wakeUpAPI(){

            const URL = "https://navxe.herokuapp.com/api"

            const request = await this.axios.get(URL)

            const responseData = request.data.message

            console.log(responseData)

            if (responseData == "Hello World! from the API"){
                  this.wakeUpCall = true
            }


      },
   },
   created(){
      this.fetchAllMaps()
   },
   async mounted(){
      this.getVersion()
      this.wakeUpAPI()
   }
}

</script>

<style scoped>
.formBG {
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
select{
        width: 100%;
        padding: 10px 15px;
        border: none;
    }
.submit{
        text-align: center;
        align-self: center;
        margin: 10px;
        color: #aaa;
        font-size: 16px;
        text-decoration: none;
        display: block;
    }
</style>