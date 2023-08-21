import axios from 'axios';
import React, { Component } from 'react';
import { Button, Form, Input, Radio } from 'antd';
import { useHistory } from 'react-router-dom';
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
    this.setState({ "uesrname": e.target.value })
  };

  passwordChande = (e) => {
    this.setState({ "password": e.target.value })
  };

  onRequiredTypeChange = ({ requiredMarkValue }) => {
    this.setState({ "requiredMark": requiredMarkValue })
  };

  toggleLogin = () => {
    this.setState(preState => ({ isLogin: !preState.isLogin }));
  };

  handleSubmit = async () => {
    const history = useHistory();
    const { isLogin, uesrname, password } = this.state;

    // 根据 isLogin 状态选择不同的接口路径
    const url = isLogin ? 'http://127.0.0.1:8000/user/login' : 'http://127.0.0.1:8000/user/register';
    // 请求参数
    const data = { username: uesrname, password: password };

    try {
      const response = await axios.post(url, data);
      console.log("成功：", response.data);
      localStorage.setItem("token", response.data.data.token)
      history.pusg('/home')
    } catch (error) {
      console.error("错误：", error.response.data);
      this.setState({ errorMessage: error.response.data.message });
    }
  };

  render() {

    const { requiredMark, isLogin } = this.state;
    console.log(this.state.uesrname)
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
            onValuesChange={this.onRequiredTypeChange} onFinish={this.handleSubmit}
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
              <Button className='loginButton' type="primary" htmlType="submit">
                {isLogin ? "登录" : "注册并登录"}
              </Button>
            </Form.Item>
          </Form>
        </div>
      </div>
    )
  }
}