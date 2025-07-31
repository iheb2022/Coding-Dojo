import { useNavigate } from "react-router-dom";


function Navbar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <nav className="main-navbar">
      <div className="navbar-left">
        <h1 className="brand">📝 ToDoApp</h1>
      </div>
      <div className="navbar-right">
        <a href="/dashboard" className="link">Dashboard</a>
        <button onClick={handleLogout} className="logout-button">Logout</button>
      </div>
    </nav>
  );
}

export default Navbar;
