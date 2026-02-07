
import { NavLink, Link } from "react-router";

function Home() {
  return (
    <nav>
      {/* NavLink makes it easy to show active states */}
      <NavLink
        to="/"
        className={({ isActive }) =>
          isActive ? "active" : ""
        }
      >
        Home
      </NavLink>
      <br></br>
      <Link to="/places/"><h1>Places to go</h1></Link>
    </nav>
  );
}

export default Home
