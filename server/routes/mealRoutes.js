const express = require("express");
const Meal = require("../models/Meal");

const router = express.Router();

// Add Meal
router.post("/add", async (req, res) => {
  try {
    const { userId, mealName, calories, protein, carbs, fat } = req.body;

    if (!userId || !mealName || !calories) {
      return res.status(400).json({
        message: "Please fill all required fields",
      });
    }

    const meal = await Meal.create({
      userId,
      mealName,
      calories,
      protein,
      carbs,
      fat,
    });

    res.status(201).json({
      message: "Meal Added Successfully",
      meal,
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({
      message: "Server Error",
    });
  }
});

// Get Meals
router.get("/:userId", async (req, res) => {
  try {
    const meals = await Meal.find({
      userId: req.params.userId,
    }).sort({ createdAt: -1 });

    res.json(meals);
  } catch (error) {
    console.error(error);
    res.status(500).json({
      message: "Server Error",
    });
  }
});

// Delete Meal
router.delete("/:mealId", async (req, res) => {
  try {
    await Meal.findByIdAndDelete(req.params.mealId);

    res.json({
      message: "Meal Deleted Successfully",
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({
      message: "Server Error",
    });
  }
});

module.exports = router;