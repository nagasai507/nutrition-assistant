import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import AddMeal from "./pages/AddMeal";
import BMI from "./pages/BMI";
import Tips from "./pages/Tips";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/addmeal" element={<AddMeal />} />
        <Route path="/bmi" element={<BMI />} />
        <Route path="/tips" element={<Tips />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;