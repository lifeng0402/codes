import React, { Component } from 'react'
import { Tabs, Select, Input } from 'antd';
import ParamsHeaders from '../ParamsHeaders';
import './index.css'


export default class BodyRequest extends Component {

      state = {
            isRawSelected: false,
      }

      onChange = (key) => { console.log(key); };

      isRawOnChange = (key) => {
            if (key === '4' || key === '6') {
                  // 当选择 "raw" 选项卡时，将 isRawSelected 设置为 true
                  this.setState({ isRawSelected: true });
            } else {
                  this.setState({ isRawSelected: false });
            }
      };

      render() {
            const { isRawSelected } = this.state;
            return (
                  <div>
                        <Tabs defaultActiveKey="1" items={
                              [
                                    {
                                          key: '1',
                                          label: 'none',
                                          children: '',
                                    },
                                    {
                                          key: '2',
                                          label: 'from-data',
                                          children: <ParamsHeaders />,
                                    },
                                    {
                                          key: '3',
                                          label: 'x-www-from-urlencoded',
                                          children: <ParamsHeaders />,
                                    },
                                    {
                                          key: '4',
                                          label: 'raw',
                                          children: <Input className='input-raw' />,
                                    },
                                    {
                                          key: '5',
                                          label: 'binary',
                                          children: <Input className='input-binary' />,
                                    },
                                    {
                                          key: '6',
                                          label: 'GraphQL',
                                          children: <Input className='input-graphql' />,
                                    }
                              ]
                        } onChange={this.isRawOnChange} tabBarExtraContent={(
                              isRawSelected && (
                                    <Select className='params-method' bordered={false} options={
                                          [
                                                {
                                                      value: 'jack',
                                                      label: 'Json',
                                                },
                                                {
                                                      value: 'lucy',
                                                      label: 'JavaScript',
                                                },
                                                {
                                                      value: 'Yiminghe',
                                                      label: 'Text',
                                                },
                                                {
                                                      value: 'disabled',
                                                      label: 'HTML',
                                                },
                                                {
                                                      value: 'disableds',
                                                      label: 'XML',
                                                }
                                          ]
                                    } />
                              )
                        )} />
                  </div>
            )
      }
}
