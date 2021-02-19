import { useHistory, useParams } from 'react-router-dom';
import { useState, useEffect } from "react";
import { Link } from 'react-router-dom'

const SignIn = () => {
    const history = useHistory();
    const [password, setPassword] = useState("");
    const [username, setusername] = useState("");
    const [isPending, setIsPending] = useState(false);
    const [data, setData] = useState(null);
    const [details, setDetails] = useState(null);
    const [rememberMe, setRememberMe] = useState(false);
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
            fetch("http://localhost:8000/users")
                .then(res => {
                    if (!res.ok) {
                        throw Error('could not fetch the data');
                    }
                    return res.json();
                })
                .then(data => {
                    setData(data);
                    setIsPending(false);
                })
                .then(
                    fetch("http://localhost:8000/details")
                        .then(res => {
                            if (!res.ok) {
                                throw Error('could not fetch the user details');
                            }
                            return res.json();
                        })
                        .then(data => {
                            setDetails(data);
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
        e.preventDefault();
        if (!validateEmail(username)) {
            alert("Enter valid email");
        }
        else if (password.length > 60 || password.length < 4) {
            alert("Your password must contain between 4 and 60 characters!");
        }
        else {
            var validEmail = false;
            var validPassword = false;
            var fullyRegistered = false;
            data.map((user) => {
                if (user.username == username) {
                    validEmail = true;
                    if (user.password == password) {
                        validPassword = true;
                    }
                }
            })
            details.map((user) => {
                if (user.username == username) {
                    fullyRegistered = true
                }
            })
            if (validEmail && validPassword) {
                if (fullyRegistered) {
                    localStorage.setItem("rememberMe", rememberMe);
                    localStorage.setItem("user", rememberMe ? username : "");
                    if (!rememberMe) {
                        sessionStorage.setItem("user", username);
                    }
                    history.push("/profile")
                }
                else {
                    alert("This user is registered without account details. Please complete them.");
                    sessionStorage.setItem("registeringUser", username);
                    sessionStorage.setItem("registerStatus", "2");
                    history.push("/chooseplan");
                }
            }
            else {
                if (!validEmail) {
                    alert("No such user!");
                }
                else {
                    alert("Password is wrong!");
                }
            }
        }
    }
    return (
        <div className="create">
            <form onSubmit={handleSubmit}>
                <label>Email:</label>
                <input type="email"
                    required
                    value={username}
                    placeholder="Email"
                    onChange={(e) => { setusername(e.target.value) }}
                />
                <label>Password:</label>
                <input type="password"
                    required
                    value={password}
                    placeholder="Password"
                    onChange={(e) => setPassword(e.target.value)}
                />
                <button>Sign in</button>
                <div style={{ display: "flex", flexDirection: "row" }}>
                    <label style={{ padding: 0, margin: 0 }}>Remember me?</label>
                    <input type="checkbox"
                        style={{ padding: 0, marginTop: 5, width: "10%" }}
                        onChange={(e) => {
                            setRememberMe(e.target.checked)
                        }
                        } />
                </div>
                <Link to="">Need Help?</Link>
                <br />
                <Link to="/">Sign up now</Link>
            </form>
        </div>);
}

export default SignIn;