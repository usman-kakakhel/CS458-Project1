import {useHistory, useParams} from 'react-router-dom';
import { useState, useEffect } from "react";

const Usertype = () => {
    const [plan, setPlan] = useState("Premium");
    const [isPending, setIsPending] = useState(false);
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
    const handleSubmit = () =>{
        sessionStorage.setItem("chosenPlan", plan)
        history.push(`/choosepayment`);
    }
    return ( <div className="create">
        <h4>STEP 2 OF 3</h4>    
        <h2>Choose the plan that is right for you</h2>
        <h4>Downgrade or upgrade at any time</h4>
        <h3>Basic:</h3>
        <h4>Monthly price: 17.99 TL, Video quality: Good, Resolution: 480p, Screens you can watch on at the same time: 1</h4>
        <h3>Standard:</h3>
        <h4>Monthly price: 29.99 TL, Video quality: Better, Resolution: 1080p, Screens you can watch on at the same time: 2</h4>
        <h3>Premium:</h3>
        <h4>Monthly price: 41.99 TL, Video quality: Best, Resolution: 4K+HDR, Screens you can watch on at the same time: 4</h4>
        <label>Choose the plan:</label>
        <select 
        value={plan}
        onChange={(e)=>setPlan(e.target.value)}>
            <option value="Basic">Basic</option>
            <option value="Standard">Standard</option>
            <option value="Premium">Premium</option>   
        </select>
        {!isPending && <button onClick={handleSubmit}>Continue</button>}

    </div> );
}
 
export default Usertype;