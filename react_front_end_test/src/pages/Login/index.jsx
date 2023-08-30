// import axios from 'axios';
import React, { Component } from 'react';
import { Navigate } from 'react-router-dom'
import { Button, Form, Input, Radio, message } from 'antd';
import "./index.css"


export default class Login extends Component {

  from = React.createRef();

  state = {
    requiredMark: 'optional',
    isLogin: true, //初始化状态为登录
    username: "",
    password: "",
    isLoggedIn: false,
    errorMessage: "",
  };

  usernameChande = (e) => {
    console.log(555, e.target)
    this.setState({ "username": e.target.value })
  };

  passwordChande = (e) => {
    this.setState({ "password": e.target.value })
  };

  onRequiredTypeChange = (requiredMarkValue) => {
    this.setState({ "requiredMark": requiredMarkValue })
  };

  toggleLogin = () => {
    this.setState(preState => ({ isLogin: !preState.isLogin }));
  };

  messageInfo = (msg) => {
    message.info(msg);
  };

  handleSubmit = async () => {

    const { username, password } = this.state;

    console.log(username, password)
    if (username === 'debugfeng' && password === 'debugfeng') {
      console.log('登录成功!')
      // 更新登录成功的状态
      this.setState({ isLoggedIn: true });
      // 回调函数,更新登录状态
      this.props.onAuthenticated(true);
    } else {
      console.log('登录失败!')
      message.error('账号或密码错误!')
    }
  };

  render() {
    const { requiredMark, isLogin, isLoggedIn, errorMessage } = this.state;

    // 判断登录成功进入首页
    if (isLoggedIn) {
      return (
        <Navigate to='/home' />
      )
    }

    return (
      <div className='login'>
        <div className='card'>
          <div className='title'>
            AgileTC
            <span>一套敏捷的测试用例管理平台</span>
          </div>
          <Form
            form={this.form} layout="vertical"
            initialValues={{ requiredMarkValue: requiredMark }}
            onValuesChange={this.onRequiredTypeChange}
          >
            <Form.Item name="requiredMarkValue" requiredMark={requiredMark}
              onFinish={this.onFinish}>
              <Radio.Group>
                <Radio.Button className='radioButton' value="optional" onClick={this.toggleLogin} checked={isLogin}>
                  登录
                </Radio.Button>
                <Radio.Button className='radioButton' value={false} onClick={this.toggleLogin} checked={!isLogin}>
                  注册
                </Radio.Button>
              </Radio.Group>
            </Form.Item>
            <Form.Item name="username" rules={[{ required: true, message: "" }]} wrapperCol={{ span: 40 }}>
              <Input onChange={this.usernameChande} placeholder="账号:" />
            </Form.Item>
            <Form.Item name="password" rules={[{ required: true, message: "" }]} wrapperCol={{ span: 40 }}>
              <Input.Password onChange={this.passwordChande} placeholder="密码:" />
            </Form.Item>
            <Form.Item>
              <Button className='loginButton' type="primary" htmlType="submit" onClick={this.handleSubmit}>
                {isLogin ? "登录" : "注册并登录"}
              </Button>
            </Form.Item>
          </Form>
        </div>
      </div>
    )
  }
}