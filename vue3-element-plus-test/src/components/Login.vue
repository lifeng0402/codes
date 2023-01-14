<template>
      <div class="login" style="text-align:center">
            <h1>{{ title }}</h1>
            <div>{{ buttonTitle }}</div>
      </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
@Options({
      props: {
            title: String,
            buttonTitle: String,
      },
})
export default class Login extends Vue {
      title!: string;
      buttonTitle!: string;
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
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
