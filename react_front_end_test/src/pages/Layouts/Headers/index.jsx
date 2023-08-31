import React, { Component } from 'react'
import { Layout, Button, Space } from 'antd'
import { MediumOutlined } from '@ant-design/icons';
import './index.css'


export default class HeaderTitle extends Component {

      // 退出登录,回调方法修改登录后记录的状态
      handleLogout = () => {
            this.props.onLogout();
      }

      render() {
            return (
                  <div>
                        <Layout.Header className='title'>
                              <div className='title-logo'>
                                    <Space>
                                          <MediumOutlined rotate={0} />
                                    </Space>
                              </div>
                              <div className='title-name'>Debugfeng用例管理测试平台</div>
                              <div className='title-logout'>
                                    <Space wrap>
                                          <Button className='logout-btn' type='primary' onClick={this.handleLogout}>退出登录</Button>
                                    </Space>
                              </div>
                        </Layout.Header>
                        <hr />
                  </div>
            )
      }
}
