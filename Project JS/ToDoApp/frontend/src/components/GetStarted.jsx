import { useNavigate } from "react-router-dom";


function GetStarted() {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate("/register");
  };

  return (
    <div className="get-started-wrapper">
      <div className="get-started-card">
        <h1>Welcome to ToDo App</h1>
        <p>Organize your tasks and boost your productivity.</p>
        <button onClick={handleClick}>Get Started</button>
      </div>
    </div>
  );
}

export default GetStarted;
