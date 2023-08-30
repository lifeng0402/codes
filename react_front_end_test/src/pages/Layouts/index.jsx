import React, { Component } from 'react';
import { Breadcrumb, Layout } from 'antd';
import { Routes, Route } from 'react-router-dom'
import Menus from './Menus';
import Headers from './Headers'
import Cases from '../Cases';
import Index from '../Index';
import './index.css'


export default class Layouts extends Component {

      render() {
            const { modules, caseList, onLogout } = this.props;
            return (
                  <div>
                        <Layout>
                              <Headers onLogout={onLogout} />
                              <Layout>
                                    <Layout.Sider className='layout-sider'>
                                          <Menus modules={modules} />
                                    </Layout.Sider>
                                    <Layout className='layout'>
                                          <Breadcrumb
                                                className='layout-breadcrumb'
                                                items={[
                                                      { title: 'Home' }, { title: 'An Application' }
                                                ]}
                                          />
                                          <Layout.Content className='layout-content'>
                                                <Routes>
                                                      <Route path='/cases' element={<Cases caseList={caseList} />} />
                                                      <Route path='/home' element={<Index />} />
                                                </Routes>
                                          </Layout.Content>
                                          <Layout.Footer className='layout-footer'>
                                                Debugfeng ©2023 Created by Debugfeng.
                                          </Layout.Footer>
                                    </Layout>
                              </Layout>
                        </Layout>
                  </div>
            )
      }
}



