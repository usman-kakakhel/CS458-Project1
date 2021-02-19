import {useHistory, useParams} from 'react-router-dom';
import { useState, useEffect } from "react";
import {Link} from 'react-router-dom'

const Finishregister = () => {
    const username = sessionStorage.getItem("registeringUser");
    const usertype = sessionStorage.getItem("chosenPlan");
    const [firstname, setfirstname] = useState("");
    const [lastname, setlastname] = useState("");
    const [cardnumber, setCardnumber] = useState();
    const [expirationDate, setExpirationDate] = useState();
    const [cvvcode, setcvvcode] = useState();
    const history = useHistory();
    const [isPending, setIsPending] = useState(false);
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
    const Register = (e) =>{
        e.preventDefault();
        var stcardnumber = cardnumber.toString();
        var stEXdate = expirationDate.toString();
        var stCVVcode = cvvcode.toString();
        const user = {username, usertype, firstname, lastname, stcardnumber, stEXdate, stCVVcode};
        setIsPending(true)
        fetch('http://localhost:8000/details', {
            method: 'POST',
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(user)
        }).then(()=>{
            history.push("/")
        })
    }
    return ( <div className="create">
        <h4>STEP 3 OF 3</h4>
        <h2>Set up your credit or debit card.</h2>
        <form onSubmit={Register}>
        <input type="text"
        required
        value={firstname}
        placeholder="First name"
        onChange={(e)=>{setfirstname(e.target.value)}}
        />
        <input type="text"
        required
        value={lastname}
        placeholder="Last name"
        onChange={(e)=>{setlastname(e.target.value)}}
        />
        <input type="number"
        required
        value={cardnumber}
        placeholder="Card number"
        onChange={(e)=>{setCardnumber(e.target.value)}}
        />
        <input type="date"
        required
        value={expirationDate}
        placeholder="Expiration date"
        onChange={(e)=>{setExpirationDate(e.target.value)}}
        />
        <input type="number"
        required
        value={cvvcode}
        placeholder="Security code"
        onChange={(e)=>{setcvvcode(e.target.value)}}
        />
        <h4>Current plan is {usertype}:</h4>
        <Link to = {`/usertype/${username}`}>
            <h3>Change plan</h3>
        </Link>
        <h4>By checking the checkbox below, you agree to our Terms of Use, Privacy Statement, and that you are over 18. Netflix will automatically continue your membership and charge the monthly membership fee to your payment method until you cancel. You may cancel at any time to avoid future charges.</h4>
        <div>
            <input type="checkbox"
            label="I agree"/>
        </div>
        {!isPending && <button>Start Membership</button>}
        </form>
    </div> );
}
 
export default Finishregister;