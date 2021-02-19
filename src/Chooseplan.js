import {useHistory, useParams} from 'react-router-dom';
import { useState, useEffect } from "react";
const ChoosePlan = () => {
    const username = sessionStorage.getItem("registeringUser");
    const history = useHistory();
    useEffect(() => {
        if(sessionStorage.getItem("registerStatus")){
            if(sessionStorage.getItem("registerStatus") == "1")
            {
                history.push("/transition");
            }
        }
        else{
            history.push("/");
        }
    }, [])
    return ( <div className="create">
        <h4>STEP 2 OF 3</h4>
        <h2>Choose your plan.</h2>
        <h3>No commitments, cancel anytime.</h3>
        <h3>Everything on Netflix for one low price</h3>
        <h3>Unlimited viewing on all your devices</h3>
        <button onClick={()=>{
            history.push(`/usertype`);
        }}>See the Plans</button>
    </div> );
}
 
export default ChoosePlan;