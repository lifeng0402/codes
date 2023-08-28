import React, { Component } from 'react'
import { Layout, Button, Space } from 'antd'
import { MediumOutlined } from '@ant-design/icons';
import './index.css'


export default class HeaderTitle extends Component {
      render() {
            return (
                  <div>
                        <Layout.Header className='title'>
                              <div className='title-logo'>
                                    <Space>
                                          <MediumOutlined rotate={0} />
                                    </Space>
                              </div>
                              <div className='title-name'>Debugfeng用例测试管理平台</div>
                              <div className='title-logout'>
                                    <Space wrap>
                                          <Button className='logout-btn' type='primary'>退出登录</Button>
                                    </Space>
                              </div>
                        </Layout.Header>
                        <hr />
                  </div>
            )
      }
}
