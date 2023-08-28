// import axios from 'axios';
import React, { Component } from 'react';
import { Button, Form, Input, Radio, message } from 'antd';
import "./index.css"


export default class Login extends Component {

  from = React.createRef();

  state = {
    requiredMark: 'optional',
    isLogin: true, //初始化状态为登录
    username: "",
    password: "",
    errorMessage: "",
  };

  usernameChande = (e) => {
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
    // const { isLogin, username, password } = this.state;

    // 根据 isLogin 状态选择不同的接口路径
    // const url = isLogin ? 'http://127.0.0.1:8000/user/login' : 'http://127.0.0.1:8000/user/register';
    // 请求参数
    //   const data = { username: username, password: password };

    //   try {
    //     const response = await axios.post(url, data);

    //     if (response && response.status === 200) {

    //       if (response.data.status === 1) {
    //         // 存储Token到本地
    //         localStorage.setItem("token", response.data.data.token);
    //       } else {
    //         this.setState({ "errorMessage": response.data.err_msg });
    //       };
    //     };

    //   } catch (error) {
    //     console.error("错误信息：", error.message);
    //     this.setState({ "errorMessage": error.message });
    //   };
    this.setState({ isAuthenticated: true })
  };


  render() {
    const { requiredMark, isLogin, errorMessage } = this.state;
    console.log(errorMessage)

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
              <Button className='loginButton' type="primary" htmlType="submit"
                onClick={() => { this.handleSubmit(); this.messageInfo(errorMessage) }}>
                {isLogin ? "登录" : "注册并登录"}
              </Button>
            </Form.Item>
          </Form>
        </div>
      </div>
    )
  }
}