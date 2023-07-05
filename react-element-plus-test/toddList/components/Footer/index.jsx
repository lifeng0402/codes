import React, { Component } from 'react'
import './index.css'

export default class Footer extends Component {

      handleCheckAll = (event) => {
            this.props.checkAllTodo(event.target.checked)
      }

      handleClearAllDone = ()=>{
            this.props.clearAllDone()
      }

      render() {
            const { todos } = this.props
            // 已完成的个数
            const doneCount = todos.reduce((pre, todo) => { return pre + (todo.done ? 1 : 0) }, 0)
            // 总数
            const total = todos.length
            return (
                  <div className="todo-footer">
                        <label>
                              <input type="checkbox" onChange={this.handleCheckAll} checked={doneCount === total && total ? true : false} />
                        </label>
                        <span>
                              <span>已经完成0</span> / 全部2
                        </span>
                        <button onClick={this.handleClearAllDone} className="btn btn-danger">清除已完成任务</button>
                  </div>
            )
      }
}
