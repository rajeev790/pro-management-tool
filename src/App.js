import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import ProjectList from './components/ProjectList';
import TaskList from './components/TaskList';
import UserList from './components/UserList';

function App() {
  return (
    <Router>
      <div className="App">
        <Switch>
          <Route path="/projects" component={ProjectList} />
          <Route path="/tasks" component={TaskList} />
          <Route path="/users" component={UserList} />
          <Route path="/" component={ProjectList} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;