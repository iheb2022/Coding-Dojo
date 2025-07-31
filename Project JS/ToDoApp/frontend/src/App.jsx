import {Routes, Route} from "react-router-dom";
import Footer from "./components/Footer";
import Register from "./components/Register";
import Login from "./components/Login";
import Dashboard from "./components/Dashboard";
import Create from "./components/Create";
import Progress from "./components/Progress";
import Completed from "./components/Completed";
import Tostart from "./components/Tostart";
import GetStarted from "./components/GetStarted";
import ViewAllTasks from "./components/ViewAllTasks";
import "./App.css";

function App() {
  return (
    <div className="app-container">
      <div className="content-container">
        <Routes>
          <Route path="/" element={<GetStarted />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/create" element={<Create />} />
          <Route path="/progress" element={<Progress />} />
          <Route path="/completed" element={<Completed />} />
          <Route path="/tostart" element={<Tostart />} />
          <Route path="/alltasks" element={<ViewAllTasks />} />

        </Routes>
      </div>
      <Footer />
    </div>
  );
}

export default App;

