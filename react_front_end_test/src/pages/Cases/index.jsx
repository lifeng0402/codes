import React from 'react'
import { Link } from 'react-router-dom'
import CaseList from './CaseList'
import SearchTerms from './SearchTerms'


export default class Cases extends React.Component {

      render() {
            const { caseList } = this.props;
            return (
                  <div>
                        <SearchTerms />
                        <CaseList caseList={caseList} />
                  </div>
            )
      }
}
