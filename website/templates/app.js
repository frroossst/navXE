console.log("Hello World!")

let app = Vue.createApp({
    data : function(){
      return {
        greeting : "Hello Vue 3",
        isVisible : true,
        num : 45
      }
    }
  })
  app.mount('#app')