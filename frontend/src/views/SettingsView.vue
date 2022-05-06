<template>
   <h1>This is the settings page </h1>
   <!-- 
      HTML code here to set graph
   -->
</template>

<script>
import AboutView from './AboutView.vue'
export default  {
  components: { AboutView },
   data() {
      return {
         graph : ''
      }
   },
   methods:{
      setGraph(graph){
         sessionStorage.setItem("savedGraph",graph)
      }
   },
   moutned(){
   }
}
</script>

<style scoped>

</style>