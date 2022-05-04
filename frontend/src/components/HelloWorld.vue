<template>
  <head>
  <title>navXE - a local navigation app</title>
  </head>
  <div class="hello">
    <p>
      To deliver the best user experience for you, I have decided to use Vue.JS to build a modern website.
      I'm also working on a PWA!
    </p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
