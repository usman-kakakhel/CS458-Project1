import { useHistory, useParams } from 'react-router-dom';
import { useState, useEffect } from "react";

const SignUpUsername = () => {
    const [username, setUsername] = useState("");
    const [isPending, setIsPending] = useState(false);
    const history = useHistory();
    const [userData, setUserData] = useState(null);
    const [userDetails, setUserDetails] = useState(null);
    function validateEmail(email) {
        const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }
    useEffect(() => {
        if (localStorage.getItem("rememberMe") === "true") {
            history.push("/profile");
        }
        else if (sessionStorage.getItem("user")) {
            history.push("/profile");
        }
        else {
            sessionStorage.removeItem("registeringUser");
            sessionStorage.removeItem("chosenPlan");
            sessionStorage.removeItem("registerStatus");
            fetch("http://localhost:8000/users")
                .then(res => {
                    if (!res.ok) {
                        throw Error('could not fetch the user data');
                    }
                    return res.json();
                })
                .then(data => {
                    setUserData(data);
                    setIsPending(false);
                    console.log("fetched data");
                }).
                then(
                    fetch("http://localhost:8000/details")
                        .then(res => {
                            if (!res.ok) {
                                throw Error('could not fetch the user details');
                            }
                            return res.json();
                        })
                        .then(data => {
                            setUserDetails(data);
                            setIsPending(false);
                            console.log("fetched details")
                        })
                        .catch(err => {
                            if (err.name === 'AbortError') {
                                console.log('fetch aborted at user details')
                            }
                            else {
                                setIsPending(false);
                            }
                        })
                )
        }
    }, [])
    const handleSubmit = (e) => {
        if (!validateEmail(username)) {
            alert("Please enter a valid email!");
        }
        else {
            console.log("we are here");
            e.preventDefault();
            setIsPending(true)
            var userIsRegistered = false;
            var userhasDetails = false;
            userData.map((data) => {
                if (data.username == username) {
                    userIsRegistered = true;
                    userDetails.map((detail) => {
                        if (detail.username == username) {
                            userhasDetails = true;
                        }
                    })
                }
            })
            if (userIsRegistered == false && userhasDetails == false) {
                sessionStorage.setItem("registeringUser", username);
                sessionStorage.setItem("registerStatus", "1");
                history.push("/transition");
            }
            else if (userIsRegistered == true && userhasDetails == false) {
                alert("This user is registered without account details. Please complete them.");
                sessionStorage.setItem("registeringUser", username);
                sessionStorage.setItem("registerStatus", "2");
                history.push("/chooseplan");
            }
            else if (userIsRegistered == true && userhasDetails == true) {
                alert("This user is fully registered. You can sign in.");
                history.push("/signin");
            }
            setIsPending(false);
        }
    }
    return (
        <div className="create">
            <h2>Sign Up:</h2>
            <form onSubmit={handleSubmit}>
                <label>Email:</label>
                <input type="email"
                    required
                    value={username}
                    placeholder="Email"
                    onChange={(e) => setUsername(e.target.value)}
                />
                {!isPending && <button>Getting started</button>}
                {isPending && <button disabled>Processing...</button>}
            </form>
        </div>
    );
}

export default SignUpUsername;