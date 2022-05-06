<template>
   <h1>This is the settings page </h1>
</template>

<script>
export default  {
   data() {
      return {
         graph : ''
      }
   },
   methods:{
      setGraph(){
         sessionStorage.getItem("")
      }
   },
   moutned(){
      this.setGraph()
   }
}
</script>

<style scoped>

</style>