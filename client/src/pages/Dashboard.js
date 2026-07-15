import React from "react";
import { Link } from "react-router-dom";

function Dashboard() {
  const user = JSON.parse(localStorage.getItem("user"));

  return (
    <div className="container mt-5">

      <div className="card shadow p-4">

        <h2 className="text-success">
          Welcome, {user?.name} 👋
        </h2>

        <p className="text-muted">
          Manage your nutrition and stay healthy!
        </p>

        <hr />

        <div className="row">

          <div className="col-md-3 mb-3">
            <Link to="/addmeal" className="btn btn-success w-100">
              ➕ Add Meal
            </Link>
          </div>

          <div className="col-md-3 mb-3">
            <Link to="/history" className="btn btn-info w-100">
              📋 Meal History
            </Link>
          </div>

          <div className="col-md-3 mb-3">
            <Link to="/bmi" className="btn btn-primary w-100">
              ⚖️ BMI Calculator
            </Link>
          </div>

          <div className="col-md-3 mb-3">
            <Link to="/tips" className="btn btn-warning w-100">
              💡 Healthy Tips
            </Link>
          </div>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;