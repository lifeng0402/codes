<template>
  <div class="container">
    <!-- form表单容器 -->
    <div class="form-container">
      <div class="signin-signup">
        <!-- 登录 -->
        <h1>登录</h1>
        <!-- 注册 -->
        <h1>注册</h1>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginRegister",
};
</script>
<style scoped>
.container {
  position: relative;
  width: 100%;
  min-height: 100vh;
  background-color: #fff;
  overflow: hidden;
}

.form-container {
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
}

.signin-signup {
  position: relative;
  top: 50%;
  left: 75%;
  transform: translate(-50%, -50%);
  width: 44%;
  transition: 1s 0.7s ease-in-out;
  display: grid;
  grid-template-columns: 1fr;
  z-index: 5;
}
</style>
