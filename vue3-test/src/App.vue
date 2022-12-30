<template>
  <div id="app">
    <img src="./assets/logo.png">
    <HelloWorld msg="欢迎来到菜鸟教程！"/>
    <router-view />
  </div>
</template>

<script>
import HelloWorldVue from './components/HelloWorld.vue'
export default {
  name: 'App',
  components: {
    HelloWorldVue
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
