import React, { Component } from 'react';
import { Button, Checkbox, Form, Input } from 'antd';
import "./index.css"

export default class Login extends Component {
  render() {
    const onFinish = (values) => {
      console.log('Success:', values);
    };
    const onFinishFailed = (errorInfo) => {
      console.log('Failed:', errorInfo);
    };
    return (
      <div className='login'>
        <div className='card'>
          <div className='title'>
            Tesing...
            <span>一套敏捷的接口测试及测试用例管理平台</span>
          </div>
          <span className='login_btn'>
            <Button type="dashed">登录</Button>
          </span>
          <span className='register_btn'>
            <Button type="dashed">注册</Button>
          </span>
          <div className='login_input'>
            <Form name="basic" labelCol={{ span: 8, }} wrapperCol={{ span: 16 }} style={{ maxWidth: 600, }}
              onFinish={onFinish} onFinishFailed={onFinishFailed} autoComplete="off">
              <Form.Item label="用户名" name="username" rules={[{ required: true, message: '请输入用户名!', },]}>
                <Input />
              </Form.Item>

              <Form.Item label="密  码" name="password" rules={[{ required: true, message: '请输入密码!', },]}>
                <Input.Password />
              </Form.Item>
            </Form>
            <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
              <Button type="primary" htmlType="submit">
                注册并登录
              </Button>
            </Form.Item>
          </div>
        </div>

      </div>
    );
  }
}