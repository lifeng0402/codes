import React, { Component } from 'react';
import { Breadcrumb, Layout } from 'antd';
import Menus from './Menus';
import Footers from './Footers';
import Headers from './Headers'
import Cases from '../Cases';
import './index.css'


export default class Layouts extends Component {

      render() {
            return (
                  <div>
                        <Layout>
                              <Headers />
                              <Layout.Content className='content-app'>
                                    <Breadcrumb className='breadcrumb-item-app' items={[
                                          { title: '|Home' }, { title: '百度一下' }
                                    ]} />
                                    <hr />
                                    <Layout className='layout-app'>
                                          <Layout.Sider className='sider-app'>
                                                <Menus />
                                          </Layout.Sider>
                                          <Layout.Content className='content-item-app'>
                                                <Cases />
                                          </Layout.Content>
                                    </Layout>
                              </Layout.Content>
                              <Footers />
                        </Layout>
                  </div>
            )
      }
}



