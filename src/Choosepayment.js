import {useHistory, useParams} from 'react-router-dom';
import { useState, useEffect } from "react";
import {Link} from 'react-router-dom'
const Choosepayment = () => {
    const history = useHistory();
    useEffect(() => {
        if(sessionStorage.getItem("registerStatus")){
            if(sessionStorage.getItem("registerStatus") == "1")
            {
                history.push("/transition");
            }
            else{
                if(!sessionStorage.getItem("chosenPlan")){
                    alert("please choose the plan first");
                    history.push("/usertype")
                }
            }
        }
        else{
            history.push("/");
        }
    }, [])
    return ( <div className="create">
        <h4>STEP 3 OF 3</h4>
        <h2>Set up your payment.</h2>
        <h3>Your membership starts as soon as you set up payment.</h3>
        <h2>No commitments</h2>
        <h3>Cancel online anytime</h3>
        <Link to = {`/finishregister`}>
            <h3 style={{marginTop:60}}>Credit or Debit Card</h3>
        </Link>
    </div> );
}
 
export default Choosepayment;