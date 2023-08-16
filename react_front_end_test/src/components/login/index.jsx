import React, { Component } from 'react';
import { Button, Form, Input, Radio } from 'antd';
import "./index.css"

export default class Login extends Component {

  from = React.createRef();

  state = {
    requiredMark: 'optional',
    isLogin: true //初始化状态为登录
  };

  onRequiredTypeChange = ({ requiredMarkValue }) => {
    this.setState({ "requiredMark": requiredMarkValue })
  };

  toggleLogin = () => {
    this.setState(preState => ({ isLogin: !preState.isLogin }));
  };

  render() {

    const { requiredMark, isLogin } = this.state;

    return (
      <div className='login'>
        <div className='card'>
          <div className='title'>
            AgileTC
            <span>一套敏捷的测试用例管理平台</span>
          </div>
          <Form
            form={this.form}
            layout="vertical"
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
              <Input placeholder="账号:" />
            </Form.Item>
            <Form.Item name="password" rules={[{ required: true, message: "" }]} wrapperCol={{ span: 40 }}>
              <Input.Password placeholder="密码:" />
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