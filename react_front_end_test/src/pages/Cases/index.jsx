import React, { Component } from 'react'
import CaseList from './CaseList'
import SearchTerms from './SearchTerms'


export default class Cases extends Component {
      render() {
            return (
                  <div>
                        <SearchTerms />
                        <CaseList />
                  </div>
            )
      }
}
