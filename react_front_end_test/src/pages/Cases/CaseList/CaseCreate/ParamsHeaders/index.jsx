import React, { Component } from 'react'
import { Table, Input } from 'antd';
import RequestKey from '../../../../../components/RequestKey';
import Description from '../../../../../components/Description';


export default class ParamsHeaders extends Component {

      state = {
            isHidden: true,
            data: [
                  {
                        key: '1',
                        requestKey: <RequestKey />,
                        requestValue: <Input placeholder='Value' />,
                        description: <Description />
                  },
            ],
      }

      render() {
            const { data } = this.state;
            return (
                  <div>
                        <Table dataSource={data} pagination={false}>
                              <Table.Column title="Key" dataIndex="requestKey" key='key' />
                              <Table.Column title="Value" dataIndex="requestValue" key='key' />
                              <Table.Column title="Description" dataIndex="description" key='key' />
                        </Table>
                  </div>
            )
      }
}
