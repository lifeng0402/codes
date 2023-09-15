import React, { Component } from 'react'
import { Select, Input, Tabs, Descriptions, Button, Empty } from 'antd';
import ParamsHeaders from './ParamsHeaders';
import BodyRequest from './BodyRequest'
import './index.css'


export default class CaseCreate extends Component {

      state = {
            isDefault: false
      }

      handleChange = (value) => { console.log(`selected ${value}`); };

      onChange = (key) => { console.log(key); };

      render() {
            const { isDefault } = this.state;
            const { isButton } = this.props;
            console.log(isButton)
            return (
                  <div>
                        <div className='request'>
                              <Select className='request-method' size='large' defaultValue="" onChange={this.handleChange} options={
                                    [
                                          {
                                                value: 'jack',
                                                label: 'Jack',
                                          },
                                          {
                                                value: 'debug',
                                                label: 'debug',
                                          },
                                          {
                                                value: 'disabled',
                                                label: 'Disabled',
                                          }
                                    ]
                              } />
                              <Input className='request-url' size='large' placeholder="https:https://debugfeng.com" />
                              {isButton ? null : <Button className='request-btn' type='primary' size='large'>Send</Button>}
                        </div>
                        <div>
                              <Tabs className='request-tab' defaultActiveKey="1" items={
                                    [
                                          {
                                                key: '1',
                                                label: `Params`,
                                                children: <ParamsHeaders />,
                                          },
                                          {
                                                key: '2',
                                                label: `Headers`,
                                                children: <ParamsHeaders />,
                                          },
                                          {
                                                key: '3',
                                                label: `Body`,
                                                children: <BodyRequest />,
                                          },
                                          {
                                                key: '4',
                                                label: `Pre-request Script`,
                                                children: `Content of Tab Pane 4`,
                                          },
                                          {
                                                key: '5',
                                                label: `Test`,
                                                children: `Content of Tab Pane 5`,
                                          },
                                    ]
                              } onChange={this.onChange} />
                        </div>
                        <br />
                        <div>
                              <h5>Reponse</h5>
                              {
                                    isDefault ? <Descriptions /> : <Empty description={false} />
                              }
                        </div>
                  </div>
            )
      }
}
