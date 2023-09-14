import React, { Component } from 'react'
import { Collapse, Button, Table } from 'antd';
import Plan from './Plan';
import LabelShow from './LabelShow';
import './index.css'


export default class Project extends Component {

      state = {
            items: [
                  {
                        key: '1',
                        label: <LabelShow />,
                        children: <Plan />
                  },
                  {
                        key: '2',
                        label: <LabelShow />,
                        children: <Plan />
                  }
            ]
      }

      render() {
            const { items } = this.state;

            return (
                  <div>
                        <Button type="primary" className='new-project'>新增测试项目</Button>
                        <Collapse accordion items={items} />
                  </div>
            )
      }
}
