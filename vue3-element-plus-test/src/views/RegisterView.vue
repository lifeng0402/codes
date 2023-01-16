<template>
      <div class="container" id="login">
            <div class="container">
                  <div>加入我们，一起创造美好世界</div>
                  <h1 class="title">注册你的账号</h1>
                  <div v-for="(item, index) in fields" :key="(item, index)" class="inputContainer">
                        <div class="fields">
                              {{ item.title }}
                              <span v-if="item.required" style="color: red;">*</span>
                              <input v-model="item.model" class="input" :type="item.type">
                              <div class="tip" v-if="index == 2">请确认密码程度需要大于6位</div>
                        </div>
                  </div>
                  <div class="subContainer">
                        <div class="setting">偏好设置</div>
                        <input v-model="receiveMsg" class="checkbox" type="checkbox">
                        <label class="label">接收更新邮件</label>
                  </div>
                  <div>
                        <button @click="createAccount" class="btn">注册账号</button>
                  </div>
            </div>

      </div>
</template>
<script>
export default {
      data() {
            return {
                  fields: [
                        {
                              title: "账号",
                              required: true,
                              type: "text"
                        },
                        {
                              title: "邮箱地址",
                              required: false,
                              type: "text"
                        },
                        {
                              title: "密码",
                              required: true,
                              type: "password"
                        }
                  ]
            }
      },
      computed: {
            name: {
                  get() {
                        return this.fields[0].model
                  },
                  set(value) {
                        this.fields.model[0] = value
                  }
            },
            email: {
                  get() {
                        return this.fields[1].model
                  },
                  set(value) {
                        this.fields.model[1] = value
                  }
            },
            password: {
                  get() {
                        return this.fields[2].model
                  },
                  set(value) {
                        this.fields.model[2] = value
                  }
            }
      },
      methods: {
            emailClick() {
                  var verify = /^\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}/;

                  if (!verify.test(this.email)) {
                        return false
                  } else {
                        this.true
                  }
            },
            // 登录
            createAccount() {
                  if (this.name.length == 0) {
                        alert("请输入用户名!")
                        return
                  } else if (this.password.length <= 6) {
                        alert("密码需要输入6位字符!")
                        return
                  } else if (this.email.length > 0 && !this.emailClick(this.email)) {
                        alert("请输入正确的邮箱!")
                        return
                  }
                  alert("注册成功!")
            }
      }
}
</script>
<style scoped lang="scss">
// 登录按钮的样式
@import "../scss/register.scss"
</style>