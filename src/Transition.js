import {useHistory, useParams} from 'react-router-dom';
import { useState, useEffect } from "react";
const Transition = () => {
    const history = useHistory();
    useEffect(() => {
        if(sessionStorage.getItem("registerStatus")){
            if(sessionStorage.getItem("registerStatus") == "2")
            {
                history.push("/chooseplan");
            }
        }
        else{
            history.push("/");
        }
    }, [])
    return ( <div className="create">
        <h4>STEP 1 OF 3</h4>
        <h2>Finish setting up your account</h2>
        <h3>Netflix is personalized for you. Create a password to watch Netflix on any device at any time</h3>
        <button onClick={()=>{history.push(`/register`);}}>Continue</button>
    </div> );
}
 
export default Transition;