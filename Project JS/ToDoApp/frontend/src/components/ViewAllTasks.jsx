import React, { useEffect, useState } from "react";
import axios from "axios";


function ViewAllTasks() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/alltasks") 
      .then((res) => {
        setTasks(res.data);
      })
      .catch((err) => {
        console.error("Error fetching tasks:", err);
      });
  }, []);

  return (
    <div className="view-tasks-container">
      <h2 className="tasks-title">All Tasks</h2>
      {tasks.length === 0 ? (
        <p className="no-tasks">No tasks found.</p>
      ) : (
        <ul className="task-list">
          {tasks.map((task) => (
            <li key={task._id} className="task-item">
              <h3>{task.title}</h3>
              <p>{task.description}</p>
              <p>Status: <span>{task.status}</span></p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default ViewAllTasks;
