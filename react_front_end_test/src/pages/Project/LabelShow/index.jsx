import React, { Component } from 'react';
import { Button, Select, Space } from 'antd';
import './index.css'


export default class LabelShow extends Component {

      state = {
            options: [
                  { value: 'TEST', label: '测试环境' },
                  { value: 'PRO', label: '预发环境' },
                  { value: 'PRE', label: '生产环境' },
            ]
      }

      render() {
            const { options } = this.state;
            return (
                  <div className='container'>
                        <div className='project-text'>
                              3333333333333333333333333333333333333
                              3333333333333333333333333333333333333333333333333333333333333333333333333333333333
                              222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222
                        </div>
                        <div className='build-env'>
                              <Select
                                    className='select-input'
                                    placeholder="构建环境"
                                    options={options}
                              />
                        </div>
                        <Button type="primary" className='build-btn'>构建</Button>
                  </div>
            )
      }
}
