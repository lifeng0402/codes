import React, { Component } from 'react';
import { Button, Table, Space } from 'antd';


export default class Plan extends Component {
      render() {
            return (
                  <div>
                        <Table dataSource={[
                              {
                                    key: '1',
                                    name: 'John',
                                    age: 32,
                                    address: 'New York No. 1 Lake Park',
                              }
                        ]}>
                              <Table.Column title='计划名称' dataIndex='name' key='name' />
                              <Table.Column title='构建环境' dataIndex='age' key='age' />
                              <Table.Column title='最近一次构建时间' dataIndex='address' key='address' />
                              <Table.Column title='操作' key='action' render={
                                    () => (
                                          <Space size='middle'>
                                                <Button type="primary">构建</Button>
                                                <Button type='primary' danger ghost>删除</Button>
                                          </Space>
                                    )
                              } />
                        </Table>
                  </div>
            )
      }
}
