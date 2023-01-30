<template>
      <div class="login">
            <el-form ref="ruleFormRef" :model="ruleForm" status-icon :rules="rules" class="login-wrap">

                  <el-form-item prop="pass">
                        <label>邮箱</label>
                        <el-input v-model="ruleForm.pass" type="password" autocomplete="off" />
                  </el-form-item>

                  <el-form-item prop="checkPass">
                        <label>账号</label>
                        <el-input v-model="ruleForm.checkPass" type="password" autocomplete="off" />
                  </el-form-item>

                  <el-form-item prop="age">
                        <label>密码</label>
                        <el-input v-model.number="ruleForm.age" />
                  </el-form-item>

                  <el-form-item>
                        <el-button type="primary" @click="submitForm(ruleFormRef)" class="block">登录</el-button>
                  </el-form-item>
            </el-form>
      </div>
</template>
    
<script lang="ts" setup>
import { reactive, ref } from 'vue'
import type { FormInstance } from 'element-plus'

const ruleFormRef = ref<FormInstance>()

const checkAge = (rule: any, value: any, callback: any) => {
      if (!value) {
            return callback(new Error('Please input the age'))
      }
      setTimeout(() => {
            if (!Number.isInteger(value)) {
                  callback(new Error('Please input digits'))
            } else {
                  if (value < 18) {
                        callback(new Error('Age must be greater than 18'))
                  } else {
                        callback()
                  }
            }
      }, 1000)
}

const validatePass = (rule: any, value: any, callback: any) => {
      if (value === '') {
            callback(new Error('Please input the password'))
      } else {
            if (ruleForm.checkPass !== '') {
                  if (!ruleFormRef.value) return
                  ruleFormRef.value.validateField('checkPass', () => null)
            }
            callback()
      }
}
const validatePass2 = (rule: any, value: any, callback: any) => {
      if (value === '') {
            callback(new Error('Please input the password again'))
      } else if (value !== ruleForm.pass) {
            callback(new Error("Two inputs don't match!"))
      } else {
            callback()
      }
}

const ruleForm = reactive({
      pass: '',
      checkPass: '',
      age: '',
})

const rules = reactive({
      pass: [{ validator: validatePass, trigger: 'blur' }],
      checkPass: [{ validator: validatePass2, trigger: 'blur' }],
      age: [{ validator: checkAge, trigger: 'blur' }],
})

const submitForm = (formEl: FormInstance | undefined) => {
      if (!formEl) return
      formEl.validate((valid) => {
            if (valid) {
                  console.log('submit!')
            } else {
                  console.log('error submit!')
                  return false
            }
      })
}
</script>
    
<style scoped>
.login-wrap {
      margin: auto;
      width: 330px;
}

.block {
      width: 100%;
      display: block;
}
</style>