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
   <br><br>
   <div class="submit">
      <button type="button" @click="saveSettings">Save</button>
   </div>
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
   data() {
      return {
         graph : '',
         maps : [],
         recentSave : false,
         recentReset : false,
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
         
         //document.getElementById("selected-graph").value = localStorage.getItem("defaultGraph")

         },
      saveSettings(){
            let saveGraph = document.getElementById("selected-graph").value
            localStorage.setItem("defaultGraph",saveGraph) 
            this.recentSave = true
      },
      resetSettings(){
            localStorage.removeItem("defaultGraph")
            this.recentReset = true
      },
      getVersion(){

            let version = localStorage.getItem("version")
            const URL = "https://navxe.herokuapp.com/api/update"
            this.axios
                .get(URL)
                .then((response) => {
                     console.log("version from API : ",response)
                     api_version = response.version
            })

            if (version == null || version == "null"){
               version = "0.0.0.0.0"
               localStorage.setItem("version",api_version)
               window.location.reload(true)
            }
            else if (version != api_version){
               localStorage.setItem("version",api_version)
               window.location.reload(true)
            }
            document.getElementById("app-version").firstChild.data = localStorage.getItem("version")
      },
   },
   created(){
      this.fetchAllMaps()
   },
   mounted(){
      this.getVersion()
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