import React, { Component } from 'react'
import { Divider, Radio, Table } from 'antd';



export default class Project extends Component {

      state = {
            columns: [
                  {
                        title: 'Name',
                        dataIndex: 'name',
                        render: (text) => <a>{text}</a>,
                  },
                  {
                        title: 'Age',
                        dataIndex: 'age',
                  },
                  {
                        title: 'Address',
                        dataIndex: 'address',
                  },
            ],
            data: [
                  {
                        key: '1',
                        name: 'John Brown',
                        age: 32,
                        address: 'New York No. 1 Lake Park',
                  },
                  {
                        key: '2',
                        name: 'Jim Green',
                        age: 42,
                        address: 'London No. 1 Lake Park',
                  },
                  {
                        key: '3',
                        name: 'Joe Black',
                        age: 32,
                        address: 'Sydney No. 1 Lake Park',
                  },
                  {
                        key: '4',
                        name: 'Disabled User',
                        age: 99,
                        address: 'Sydney No. 1 Lake Park',
                  },
            ]
      }

      rowSelection = {
            onChange: (selectedRowKeys, selectedRows) => {
                  console.log(`selectedRowKeys: ${selectedRowKeys}`, 'selectedRows: ', selectedRows);
            },
            getCheckboxProps: (record) => ({
                  disabled: record.name === 'Disabled User',
                  // Column configuration not to be checked
                  name: record.name,
            }),
      };



      render() {
            const { columns, data } = this.state;
            return (
                  <div>
                        <Radio.Group>
                              <Radio value="checkbox">Checkbox</Radio>
                              <Radio value="radio">radio</Radio>
                        </Radio.Group>

                        <Divider />

                        <Table columns={columns} dataSource={data} />
                  </div>
            )
      }
}
