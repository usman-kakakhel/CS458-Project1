import { useHistory, useParams } from 'react-router-dom';
import { useState, useEffect } from "react";
const SignUpPassword = () => {
    const username = sessionStorage.getItem("registeringUser");
    const [password, setPassword] = useState("");
    const [sendMail, setSendMail] = useState(false);
    const [isPending, setIsPending] = useState(false);
    const history = useHistory();
    useEffect(() => {
        if (sessionStorage.getItem("registerStatus")) {
            if (sessionStorage.getItem("registerStatus") == "2") {
                history.push("/chooseplan");
            }
        }
        else {
            history.push("/");
        }
    }, [])
    const handleSubmit = (e) => {
        e.preventDefault();
        const user = { username, password };
        if (password.length > 60 || password.length < 4) {
            alert("Your password must contain between 4 and 60 characters!");
        }
        else {
            setIsPending(true)
            fetch('http://localhost:8000/users', {
                method: 'POST',
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(user)
            }).then(() => {
                console.log('new user added');
                setIsPending(false);
                sessionStorage.setItem("registerStatus", "2");
                history.push(`/chooseplan`);
            })
        }
    }
    return (
        <div className="create">
            <h4>STEP 2 OF 3</h4>
            <h2>Create a password to start your membership.</h2>
            <h3>Just a few more steps and you're done!</h3>
            <h3>We hate paperwork, too.</h3>
            <form onSubmit={handleSubmit}>
                <label>Email:</label>
                <input type="text"
                    disabled
                    value={username}
                />
                <label>Password:</label>
                <input type="password"
                    required
                    value={password}
                    placeholder="Password"
                    onChange={(e) => setPassword(e.target.value)}
                />
                <div style={{ display: "flex", flexDirection: "row", paddingBottom: 20 }}>
                    <input type="checkbox"
                        style={{ margin: 0, padding: 0, width: "10%" }}
                        onChange={() => { setSendMail(!sendMail) }} />
                    <label>Please do not email me Netflix special offers.</label>
                </div>
                {!isPending && <button>Continue</button>}
                {isPending && <button disabled>Registering...</button>}
            </form>
        </div>);
}

export default SignUpPassword;