const express = require("express");
const cors = require("cors");
const dotenv = require("dotenv");

const connectDB = require("./config/db");
const authRoutes = require("./routes/authRoutes");
const mealRoutes = require("./routes/mealRoutes");
dotenv.config();

connectDB();

const app = express();

app.use(cors());
app.use(express.json());
console.log("✅ Registering auth routes...");

app.use("/api/auth", authRoutes);
app.use("/api/meals", mealRoutes);

app.get("/", (req, res) => {
  res.send("Nutrition Assistant Backend is Running 🚀");
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`🚀 Server running on http://localhost:${PORT}`);
});