import React, { Component } from 'react'
import { Collapse, Button, Table } from 'antd';


export default class Project extends Component {

      onChange = (key) => { console.log(key) };

      render() {
            return (
                  <div>
                        <Collapse accordion items={[{
                              key: '1',
                              label: <div>
                                    <p>33333333333333333</p>
                                    <Button>运行按钮</Button>
                              </div>,
                              children: <div>
                                    <Table columns={[
                                          {
                                                title: 'Name',
                                                dataIndex: 'name',
                                                key: 'name',
                                          },
                                          {
                                                title: 'Age',
                                                dataIndex: 'age',
                                                key: 'age',
                                          },
                                          {
                                                title: 'Address',
                                                dataIndex: 'address',
                                                key: 'address',
                                          },
                                          {
                                                title: 'Action',
                                                dataIndex: 'action',
                                                key: 'address',
                                          }
                                    ]}></Table>
                                    <p>{555555}</p>
                                    <Button>子任务运行按钮</Button>
                              </div>,
                        }]} />
                  </div>
            )
      }
}
