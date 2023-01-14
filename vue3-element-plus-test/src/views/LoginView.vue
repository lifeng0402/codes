<template>
      <div>
            登录页面
      </div>
      <div class="login">
            <h1>{{ title }}</h1>
            <div v-if="noLogin">账号:<input v-model="username" type="text"></div>
            <div v-if="noLogin">密码:<input v-model="password" type="password"></div>
            <div class="button-title" v-on:click="click">{{ buttonTitle }}</div>
      </div>
</template>
<script>
export default {
      data() {
            return {
                  title: "欢迎您，未登录",
                  noLogin: true,
                  username: "",
                  password: "",
                  buttonTitle: "登录"
            }
      },
      methods: {
            click() {
                  if (this.noLogin) {
                        this.login()
                  } else {
                        this.logout()
                  }
            },
            // 登录
            login() {
                  if (this.username.length > 0 && this.password.length > 0) {
                        // 登录后刷新页面
                        alert(`username: ${this.username}`)
                        this.noLogin = false
                        this.title = `欢迎您: ${this.username}`
                        this.buttonTitle = "注销"
                        // 点击注销后，把用户名和密码置空字符串
                        this.username = ""
                        this.password = ""
                  } else {
                        alert("请输入账号或密码！")
                  }
            },
            // 登出
            logout() {
                  // 清空数据
                  this.noLogin = true
                  this.title = "欢迎您：未登录"
                  this.buttonTitle = "登录"
            }
      }
}
</script>
<style scoped lang="scss">
// 登录按钮的样式
div.button-title {
      border-radius: 30px;
      width: 100px;
      margin: 20px auto;
      color: white;
      background-color: blue;
}
</style>