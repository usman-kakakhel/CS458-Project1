import Navbar from './Navbar';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom'
import NotFound from './NotFound';
import SignUpUsername from "./SignUpUsername";
import SignUpPassword from './SignUpPassword';
import Transition from './Transition';
import ChoosePlan from './Chooseplan';
import UserType from './UserType';
import Choosepayment from './Choosepayment';
import Finishregister from "./Finishregister";
import SignIn from './signin';
import Profile from "./Profile";
function App() {
  return (
    <Router>
      <div className="App">
        <div className="content">
          <Switch>
            <Route exact path="/">
              {<Navbar/>}
              <SignUpUsername/>
            </Route>
            {/*<Route exact path="/signup">
              <SignUpUsername/>
            </Route>*/}
            <Route path="/signin">
              <SignIn/>
            </Route>
            <Route path="/profile">
              <Profile/>
            </Route>
            <Route path="/register">
              <SignUpPassword/>
            </Route>
            <Route path="/transition">
              <Transition/>
            </Route>
            <Route path="/chooseplan">
              <ChoosePlan/>
            </Route>
            <Route path="/usertype">
              <UserType/>
            </Route>
            <Route path="/choosepayment">
              <Choosepayment/>
            </Route>
            <Route path="/finishregister">
              <Finishregister/>
            </Route>
            <Route path="*">
              <NotFound/>
            </Route>
          </Switch>
        </div>
      </div>
    </Router>
  );
}

export default App;
