import React, { Component } from 'react'
import { Space, Table, Button, Popconfirm, message } from 'antd';
import { Link } from 'react-router-dom'


const { Column } = Table;

export default class Report extends Component {
      state = {
            data: [
                  {
                        key: '1',
                        reportName: 'Joe',
                        createTime: '2023-09-05 19:47:55',
                        total: 32,
                        succeed: 10,
                        defeated: 22,
                        passingRate: '100%',
                  },
                  {
                        key: '2',
                        reportName: 'Joe',
                        createTime: '2023-09-05 19:47:44',
                        total: 32,
                        succeed: 10,
                        defeated: 22,
                        passingRate: '100%',
                  },
                  {
                        key: '3',
                        reportName: 'Joe',
                        createTime: '2023-09-05 19:47:05',
                        total: 32,
                        succeed: 10,
                        defeated: 22,
                        passingRate: '100%',
                  },
            ]
      }

      confirm = (e) => {
            console.log(e);
            message.success('Click on Yes');
      };

      cancel = (e) => {
            console.log(e);
            message.error('Click on No');
      };

      render() {
            const { data } = this.state;
            return (
                  <div>
                        <Table dataSource={data}>
                              <Column title="报告名称" dataIndex="reportName" key="reportName" />
                              <Column title="生成时间" dataIndex="createTime" key="createTime" />
                              <Column title="总数" dataIndex="total" key="total" />
                              <Column title="成功数" dataIndex="succeed" key="succeed" />
                              <Column title="失败数" dataIndex="defeated" key="defeated" />
                              <Column title="通过率" dataIndex="passingRate" key="passingRate" />
                              <Column
                                    title="操作"
                                    key="action"
                                    render={() => (
                                          <Space size="middle">
                                                <Link to='/report/details'>查看详情</Link>
                                                <Popconfirm
                                                      title="Delete the task"
                                                      description="Are you sure to delete this task?"
                                                      onConfirm={this.confirm}
                                                      onCancel={this.cancel}
                                                      okText="确定"
                                                      cancelText="取消"
                                                >
                                                      <Button type="link" block>删除报告</Button>
                                                </Popconfirm>
                                          </Space>
                                    )}
                              />
                        </Table>
                  </div >
            )
      }
}
