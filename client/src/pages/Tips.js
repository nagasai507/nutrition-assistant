import React from "react";

function Tips() {
  const tips = [
    "🥗 Eat at least 5 servings of fruits and vegetables every day.",
    "💧 Drink 2–3 liters of water daily.",
    "🍗 Include protein in every meal.",
    "🚶 Exercise for at least 30 minutes every day.",
    "😴 Sleep for 7–8 hours every night.",
    "🍔 Avoid junk food and sugary drinks.",
    "🥜 Eat healthy snacks like nuts and fruits.",
    "🥛 Drink milk or consume calcium-rich foods.",
    "🍽️ Don't skip breakfast.",
    "😊 Maintain a balanced lifestyle and reduce stress."
  ];

  return (
    <div className="container mt-5">
      <div className="card shadow p-4">

        <h2 className="text-center text-success mb-4">
          💡 Healthy Tips
        </h2>

        <div className="list-group">

          {tips.map((tip, index) => (
            <div
              key={index}
              className="list-group-item mb-2"
            >
              {tip}
            </div>
          ))}

        </div>

      </div>
    </div>
  );
}

export default Tips;