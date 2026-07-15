# 🥗 Nutrition Assistant

A full-stack Nutrition Assistant web application developed using the **MERN Stack (MongoDB, Express.js, React.js, Node.js)**. The application helps users maintain healthy eating habits by allowing them to register, log in securely, calculate BMI, add meals, and view their meal history.

---

## 📖 Project Overview

The Nutrition Assistant is designed to help users track their daily nutrition and improve their lifestyle through a simple and user-friendly interface. It provides secure authentication, meal tracking, BMI calculation, and nutrition tips. The project demonstrates full-stack web development using the MERN stack.

---

## ✨ Features

### 👤 User Authentication
- User Registration
- User Login
- Password Encryption using bcrypt
- JWT Authentication

### 🍽️ Meal Management
- Add Meals
- Store Meals in MongoDB
- View Meal History
- Data persists after page refresh

### 📊 Health Features
- BMI Calculator
- Healthy Nutrition Tips
- Total Calories Calculation

### 🎨 User Interface
- Responsive Design
- Bootstrap Styling
- Easy Navigation
- Clean Dashboard

---

## 🛠️ Technologies Used

### Frontend
- React.js
- React Router DOM
- Axios
- Bootstrap
- CSS

### Backend
- Node.js
- Express.js

### Database
- MongoDB Atlas
- Mongoose

### Authentication
- JWT (JSON Web Token)
- bcryptjs

### Development Tools
- VS Code
- Git
- GitHub
- Thunder Client
- npm

---

## 📁 Project Structure

```
nutrition-assistant
│
├── client
│   ├── public
│   ├── src
│   │   ├── pages
│   │   │   ├── Home.js
│   │   │   ├── Register.js
│   │   │   ├── Login.js
│   │   │   ├── Dashboard.js
│   │   │   ├── AddMeal.js
│   │   │   ├── BMI.js
│   │   │   └── Tips.js
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
│
├── server
│   ├── config
│   ├── models
│   ├── routes
│   ├── server.js
│   └── package.json
│
└── README.md
```

---

## ⚙️ Installation Steps

### 1. Clone Repository

```bash
git clone https://github.com/nagasai507/nutrition-assistant.git
```

### 2. Open Project

```bash
cd nutrition-assistant
```

### 3. Install Frontend Dependencies

```bash
cd client
npm install
```

### 4. Install Backend Dependencies

```bash
cd ../server
npm install
```

### 5. Configure Environment Variables

Create a `.env` file inside the **server** folder.

```env
PORT=5000
MONGO_URI=Your_MongoDB_Connection_String
JWT_SECRET=Your_JWT_Secret
```

### 6. Start Backend

```bash
cd server
node server.js
```

### 7. Start Frontend

Open another terminal.

```bash
cd client
npm start
```

### 8. Open Browser

```
http://localhost:3000
```

---

## 📸 Screenshots

### Home Page

(Add Screenshot Here)

---

### Registration Page

(Add Screenshot Here)

---

### Login Page

(Add Screenshot Here)

---

### Dashboard

(Add Screenshot Here)

---

### Add Meal

(Add Screenshot Here)

---

### Meal History

(Add Screenshot Here)

---

### BMI Calculator

(Add Screenshot Here)

---

## 🚀 Future Enhancements

- Edit Meal
- Delete Meal
- User Profile
- Daily Water Intake Tracker
- Weight Progress Tracker
- Nutrition Charts
- AI Meal Recommendation
- Food Image Recognition
- Dark Mode
- Mobile Application
- Email Verification
- Password Reset

---

## 🎯 Learning Outcomes

This project helped in understanding:

- MERN Stack Development
- REST API Development
- MongoDB Integration
- JWT Authentication
- React State Management
- CRUD Operations
- Git & GitHub
- Client-Server Communication
- Database Design

---

## 👨‍💻 Author

**Naga Sai**

B.Tech Computer Science Engineering

GitHub:
https://github.com/nagasai507

---

## 📄 License

This project is developed for educational purposes as a B.Tech Final Year Mini Project.
