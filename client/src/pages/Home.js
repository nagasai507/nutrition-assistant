import React from "react";
import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="container text-center mt-5">

      <h1 className="text-success mb-3">
        🥗 Nutrition Assistant
      </h1>

      <h2 className="mb-3">
        Eat Healthy, Stay Healthy
      </h2>

      <p className="lead">
        Track your meals, calories and BMI easily.
      </p>

      <div className="mt-4">

        <Link
          to="/login"
          className="btn btn-success me-3"
        >
          Login
        </Link>

        <Link
          to="/register"
          className="btn btn-outline-success"
        >
          Register
        </Link>

      </div>

    </div>
  );
}

export default Home;