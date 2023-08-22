import React from 'react';
import { Breadcrumb, Layout, Menu, theme } from 'antd';
import "./index.css"

const { Header, Content, Footer } = Layout;
const App = () => {
      const { colorBgContainer } = theme.useToken();
      return (
            <Layout className="container">
                  <Header
                        style={{
                              display: 'flex',
                              alignItems: 'center',
                        }}
                  >
                        <div className="demo-logo" />
                        <Menu
                              theme="dark"
                              mode="horizontal"
                              defaultSelectedKeys={['1']}
                              items={new Array(15).fill(null).map((vat, index) => {
                                    const key = index + 1;
                                    return {
                                          key,
                                          label: `nav ${key}`,
                                    };
                              })}
                        />
                  </Header>
                  <Content className='content'>
                        <Breadcrumb className='breadcrumb'>
                              <Breadcrumb.Item>Home</Breadcrumb.Item>
                              <Breadcrumb.Item>List</Breadcrumb.Item>
                              <Breadcrumb.Item>App</Breadcrumb.Item>
                        </Breadcrumb>
                        <div className="site-layout-content" style={{ background: colorBgContainer, }}>
                              Content
                        </div>
                  </Content>
                  <Footer className='footer-info'>Ant Design ©2023 Created by Ant UED</Footer>
            </Layout>
      );
};
export default App;