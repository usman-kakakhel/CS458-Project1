import {Link} from 'react-router-dom';
import image from "./images/Netflix_Logo.png";

const Navbar = () => {
    return(
         <nav className="navbar">
             <h1>Netflix</h1>
             <div className="links">
                 <Link to="/signin" >Sign in</Link>
             </div>
         </nav>
    );
}
    


export default Navbar;