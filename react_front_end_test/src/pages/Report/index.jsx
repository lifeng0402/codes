import React, { Component } from 'react'
import { Space, Table } from 'antd';
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
                                                <a>删除报告</a>
                                          </Space>
                                    )}
                              />
                        </Table>
                  </div >
            )
      }
}
