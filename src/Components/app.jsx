function App() {
  const [user, setUser] = React.useState({});

  React.useEffect(() => {
    const user_in_storage = localStorage.getItem("user");
    if (user_in_storage) {
      setUser(JSON.parse(user_in_storage));
    }
  }, []);

  // function logOut() {
  //     setUser({});
  //     localStorage.clear();
  //     return(alert('logged out'))
  // }

  return (
    <div>hi there</div>

    // <Router>
    //   <Navbar>
    //     <Nav>
    //       {user.id ? "" : <Nav.Link href="/SignIn"> Sign In </Nav.Link>}
    //       {user.id ? "" : <Nav.Link href="/SignUp"> Sign Up </Nav.Link>}
    //     </Nav>
    //   </Navbar>
    //   <Switch>
    //     <Route path="/SignUp">
    //       <SignUp />
    //     </Route>
    //     <Route path="/SignIn">
    //       <SignIn />
    //     </Route>
    //     <Route path="/">
    //       <Homepage user={user} />
    //     </Route>
    //   </Switch>
    // </Router>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
// return(
// <Router>
//     <Navbar bg="light" expand="lg" className="navbar-color navbar-background-color">
//         <Navbar.Brand className="nav-link navbar-color navbar-brand:hover navbar-brand:focus" href="/">
//         <div className="navbar-brand">
//         </div>
//         </Navbar.Brand>
//         <Navbar.Toggle aria-controls="basic-navbar-nav"/>
//         <Navbar.Collapse id="basic-navbar-nav">
//         <Nav className="mr-auto">
//             {user.id ? '' : <Nav.Link href="/login"> Login </Nav.Link>}
//             {user.id ? '' : <Nav.Link href="/new_user"> Create Account</Nav.Link>}
//             <Nav.Link href="/recipes"> Recipes </Nav.Link>
//             {user.id ? <Nav.Link href="/create_mealplan"> Create a Mealplan </Nav.Link> : ''}
//             {user.id ? <Nav.Link href="/mealplans"> View My Mealplans </Nav.Link> : ''}
//         </Nav>
//         <Nav.Item className="ml-auto">
//             {user.id ? <Button href="/" onClick={logOut} variant="outline-secondary"> Log Out </Button> : ''}
//         </Nav.Item>
//         </Navbar.Collapse>
//     </Navbar>

//         <Switch>
//             <Route path="/login">
//                 <LogIn user={user} setUser={setUser} />
//             </Route>
//             <Route path="/recipes">
//                 <Recipes />
//             </Route>
//             <Route path="/create_mealplan">
//                 <CreateMealPlan user={user}/>
//             </Route>
//             <Route path="/mealplan/:mealplan_id">
//                 <Mealplan />
//             </Route>
//             <Route path="/mealplans">
//                 <Mealplans user={user}/>
//             </Route>
//             <Route path="/new_user">
//                 <CreateUser user={user} setUser={setUser}/>
//             </Route>
//             <Route path="/">
//                 <Homepage user={user}/>
//             </Route>
//         </Switch>
//     </Router>
// )
// }
