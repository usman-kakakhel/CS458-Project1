import {useHistory, useParams} from 'react-router-dom';
import { useState, useEffect } from "react";
const Profile = () => {
    const history = useHistory();
    const [user, setUser] = useState("");
    const logoutHandler = ()=>{
        localStorage.clear();
        sessionStorage.clear();
        history.push("/signin");
    }
    useEffect(() => {
        if(localStorage.getItem("rememberMe") ==="true"){
            setUser(localStorage.getItem("user"));
        }
        else if(sessionStorage.getItem("user")){
            setUser(sessionStorage.getItem("user"));
        }
        else{
            history.push("signin");
        }
    }, [])
    return ( <div className="create">
        <h2>Home page</h2>
        <h4>user is {user}</h4>
        <button onClick={logoutHandler}>Logout</button>
    </div> );
}
 
export default Profile;