import React from "react";
import App from "./App";
import Test from "./home";
import { createBrowserRouter as Router, Route } from "react-router-dom";


function router() {
      return (
            <Router>
                  <Route path="/" component={App} />
                  <React path="/test" component={Test} />
            </Router>
      );
}


export default router;