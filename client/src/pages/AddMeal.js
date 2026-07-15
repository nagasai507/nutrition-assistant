import React, { useEffect, useState } from "react";
import axios from "axios";

function AddMeal() {
  const user = JSON.parse(localStorage.getItem("user"));

  const [meal, setMeal] = useState({
    mealName: "",
    calories: "",
    protein: "",
    carbs: "",
    fat: "",
  });

  const [meals, setMeals] = useState([]);

  useEffect(() => {
    fetchMeals();
  }, []);

  const fetchMeals = async () => {
    try {
      const res = await axios.get(
        `http://localhost:5000/api/meals/${user.id}`
      );

      setMeals(res.data);
    } catch (err) {
      console.log(err);
    }
  };

  const handleChange = (e) => {
    setMeal({
      ...meal,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.post("http://localhost:5000/api/meals/add", {
        userId: user.id,
        ...meal,
      });

      alert("Meal Added Successfully!");

      setMeal({
        mealName: "",
        calories: "",
        protein: "",
        carbs: "",
        fat: "",
      });

      fetchMeals();
    } catch (err) {
      console.log(err);
      alert("Unable to save meal");
    }
  };

  const totalCalories = meals.reduce(
    (sum, meal) => sum + Number(meal.calories),
    0
  );

  return (
    <div className="container mt-5">
      <div className="card shadow p-4">

        <h2 className="text-center text-success mb-4">
          🍽️ Add Meal
        </h2>

        <form onSubmit={handleSubmit}>

          <input
            type="text"
            className="form-control mb-3"
            placeholder="Meal Name"
            name="mealName"
            value={meal.mealName}
            onChange={handleChange}
            required
          />

          <input
            type="number"
            className="form-control mb-3"
            placeholder="Calories"
            name="calories"
            value={meal.calories}
            onChange={handleChange}
            required
          />

          <input
            type="number"
            className="form-control mb-3"
            placeholder="Protein (g)"
            name="protein"
            value={meal.protein}
            onChange={handleChange}
          />

          <input
            type="number"
            className="form-control mb-3"
            placeholder="Carbs (g)"
            name="carbs"
            value={meal.carbs}
            onChange={handleChange}
          />

          <input
            type="number"
            className="form-control mb-3"
            placeholder="Fat (g)"
            name="fat"
            value={meal.fat}
            onChange={handleChange}
          />

          <button className="btn btn-success w-100">
            Save Meal
          </button>

        </form>

      </div>

      <div className="card shadow mt-5 p-4">

        <h3 className="text-center mb-3">
          📋 Meal History
        </h3>

        <table className="table table-bordered">

          <thead className="table-success">
            <tr>
              <th>Meal</th>
              <th>Calories</th>
              <th>Protein</th>
              <th>Carbs</th>
              <th>Fat</th>
            </tr>
          </thead>

          <tbody>

            {meals.map((item) => (
              <tr key={item._id}>
                <td>{item.mealName}</td>
                <td>{item.calories}</td>
                <td>{item.protein}</td>
                <td>{item.carbs}</td>
                <td>{item.fat}</td>
              </tr>
            ))}

          </tbody>

        </table>

        <h4 className="text-end text-success">
          Total Calories : {totalCalories} kcal
        </h4>

      </div>
    </div>
  );
}

export default AddMeal;