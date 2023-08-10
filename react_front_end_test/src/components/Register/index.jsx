import React, { Component } from 'react';
import { Button, Checkbox, Form, Input } from 'antd';
import "./index.css"

export default class Register extends Component {
      render() {
            const onFinish = (values) => {
                  console.log('Success:', values);
            };
            const onFinishFailed = (errorInfo) => {
                  console.log('Failed:', errorInfo);
            };
            return (
                  <div className='register-form'>
                        <Form name="basic" labelCol={{ span: 8, }} wrapperCol={{ span: 16, }} style={{ maxWidth: 600, }} onFinish={onFinish} onFinishFailed={onFinishFailed}>
                              <Form.Item label="用户名" name="username"
                                    rules={[
                                          {
                                                required: true,
                                                message: '请输入用户名!',
                                          },
                                    ]}>
                                    <Input />
                              </Form.Item>

                              <Form.Item label="密码" name="password"
                                    rules={[
                                          {
                                                required: true,
                                                message: '请输入密码!',
                                          },
                                    ]}>
                                    <Input.Password />
                              </Form.Item>


                              <Form.Item wrapperCol={{ offset: 8, span: 16, }}>
                                    <Button type="primary" htmlType="submit">
                                          注册
                                    </Button>
                              </Form.Item>
                        </Form>
                  </div>
            );
      }
}