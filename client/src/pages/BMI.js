import React, { useState } from "react";

function BMI() {
  const [height, setHeight] = useState("");
  const [weight, setWeight] = useState("");
  const [bmi, setBmi] = useState("");
  const [status, setStatus] = useState("");

  const calculateBMI = (e) => {
    e.preventDefault();

    const h = height / 100;
    const result = (weight / (h * h)).toFixed(2);

    setBmi(result);

    if (result < 18.5) {
      setStatus("Underweight");
    } else if (result < 25) {
      setStatus("Normal Weight");
    } else if (result < 30) {
      setStatus("Overweight");
    } else {
      setStatus("Obese");
    }
  };

  return (
    <div className="container mt-5">
      <div className="col-md-6 mx-auto">
        <div className="card shadow p-4">

          <h2 className="text-center text-success mb-4">
            ⚖️ BMI Calculator
          </h2>

          <form onSubmit={calculateBMI}>

            <input
              type="number"
              className="form-control mb-3"
              placeholder="Height (cm)"
              value={height}
              onChange={(e) => setHeight(e.target.value)}
              required
            />

            <input
              type="number"
              className="form-control mb-3"
              placeholder="Weight (kg)"
              value={weight}
              onChange={(e) => setWeight(e.target.value)}
              required
            />

            <button className="btn btn-primary w-100">
              Calculate BMI
            </button>

          </form>

          {bmi && (
            <div className="alert alert-success mt-4 text-center">
              <h4>Your BMI: {bmi}</h4>
              <h5>{status}</h5>
            </div>
          )}

        </div>
      </div>
    </div>
  );
}

export default BMI;