import React, { Component } from 'react';

export default class Search extends Component {

      search = () => {
            const { value } = this.keyWordElement
            console.log(value);
      }

      render() {
            return (
                  <section className='jumbotron'>
                        <h3 className='jumbotron-heading'>搜索github用户</h3>
                        <div>
                              <input ref={c => this.keyWordElement = c} type='text' placeholder='enter the name you search' />&nbsp;
                              <button onClick={this.search}>搜索</button>
                        </div>
                  </section>
            );
      }
}
