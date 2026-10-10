
import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Nutrition Assistant",
    page_icon="🥗",
    layout="wide"
)

# ---------- SESSION STATE ----------
if "meals" not in st.session_state:
    st.session_state.meals = []

if "water" not in st.session_state:
    st.session_state.water = 0

if "calorie_goal" not in st.session_state:
    st.session_state.calorie_goal = 2000

if "protein_goal" not in st.session_state:
    st.session_state.protein_goal = 100


# ---------- FOOD DATABASE ----------
FOODS = {
    "Boiled Egg": {"calories": 78, "protein": 6, "carbs": 1, "fat": 5},
    "Idli (2 pieces)": {"calories": 120, "protein": 4, "carbs": 26, "fat": 1},
    "Dosa": {"calories": 168, "protein": 4, "carbs": 25, "fat": 6},
    "Rice (1 cup cooked)": {"calories": 205, "protein": 4, "carbs": 45, "fat": 0},
    "Dal (1 cup)": {"calories": 180, "protein": 12, "carbs": 30, "fat": 3},
    "Chicken (100 g cooked)": {"calories": 165, "protein": 31, "carbs": 0, "fat": 4},
    "Banana": {"calories": 105, "protein": 1, "carbs": 27, "fat": 0},
    "Apple": {"calories": 95, "protein": 0, "carbs": 25, "fat": 0},
    "Milk (250 ml)": {"calories": 150, "protein": 8, "carbs": 12, "fat": 8},
    "Curd (100 g)": {"calories": 61, "protein": 4, "carbs": 5, "fat": 3},
    "Chapati": {"calories": 120, "protein": 3, "carbs": 20, "fat": 3},
    "Peanuts (30 g)": {"calories": 170, "protein": 7, "carbs": 5, "fat": 15},
}

MEAL_TYPES = ["Breakfast", "Lunch", "Dinner", "Snack"]


def daily_totals():
    today = date.today().isoformat()
    entries = [
        meal for meal in st.session_state.meals
        if meal["date"] == today
    ]

    totals = {
        "calories": 0,
        "protein": 0,
        "carbs": 0,
        "fat": 0,
    }

    for meal in entries:
        for nutrient in totals:
            totals[nutrient] += meal[nutrient]

    return entries, totals


# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("🥗 NutriTrack")
    st.caption("Your personal nutrition companion")
    st.divider()

    st.subheader("Daily Goals")

    st.session_state.calorie_goal = st.number_input(
        "Calorie goal (kcal)",
        min_value=500,
        max_value=6000,
        value=int(st.session_state.calorie_goal),
        step=100,
    )

    st.session_state.protein_goal = st.number_input(
        "Protein goal (g)",
        min_value=10,
        max_value=400,
        value=int(st.session_state.protein_goal),
        step=5,
    )

    st.divider()
    st.subheader("💧 Water Tracker")

    st.write(f"Glasses today: {st.session_state.water}/8")

    water_col1, water_col2 = st.columns(2)

    with water_col1:
        if st.button("＋ Add glass", use_container_width=True):
            st.session_state.water = min(
                8, st.session_state.water + 1
            )
            st.rerun()

    with water_col2:
        if st.button("Reset", use_container_width=True):
            st.session_state.water = 0
            st.rerun()

    st.progress(st.session_state.water / 8)

    st.caption("One glass is approximately 250 ml.")


# ---------- HEADER ----------
st.title("🥗 Nutrition Assistant")
st.write(
    "Plan balanced meals, monitor your nutrition, "
    "and build healthier daily habits."
)

st.caption(f"Today: {date.today().strftime('%d %B %Y')}")

entries, totals = daily_totals()

remaining = max(
    0, st.session_state.calorie_goal - totals["calories"]
)

# ---------- NAVIGATION ----------
dashboard, food_log, planner, food_guide = st.tabs([
    "🏠 Dashboard",
    "🍽️ Food Log",
    "📅 Meal Planner",
    "🥑 Food Guide",
])


# ---------- DASHBOARD ----------
with dashboard:
    st.subheader("Today's Overview")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Calories consumed",
        f'{totals["calories"]:,} kcal',
        f'{totals["calories"] - st.session_state.calorie_goal:+,} kcal'
        if totals["calories"] > st.session_state.calorie_goal
        else None,
    )

    c2.metric("Calories remaining", f"{remaining:,} kcal")
    c3.metric("Protein", f'{totals["protein"]} g')
    c4.metric("Meals logged", len(entries))

    st.divider()

    st.subheader("🔥 Daily Calorie Progress")

    st.progress(min(
        1.0,
        totals["calories"] / st.session_state.calorie_goal
    ))

    st.write(
        f'{totals["calories"]:,} of '
        f'{st.session_state.calorie_goal:,} kcal'
    )

    if totals["calories"] > st.session_state.calorie_goal:
        st.warning("You've exceeded your calorie goal for today.")
    elif totals["calories"] > 0:
        st.success("Keep tracking your meals throughout the day!")
    else:
        st.info("Start by adding your first meal in the Food Log tab.")

    st.divider()

    left, right = st.columns(2)

    with left:
        st.subheader("🥩 Macronutrients")

        st.write(f'**Protein:** {totals["protein"]} g')
        st.progress(min(
            1.0,
            totals["protein"] / st.session_state.protein_goal
        ))

        st.write(f'**Carbohydrates:** {totals["carbs"]} g')
        st.write(f'**Fat:** {totals["fat"]} g')

    with right:
        st.subheader("🍴 Recent Meals")

        if entries:
            for meal in reversed(entries[-5:]):
                st.write(
                    f'**{meal["name"]}** · {meal["meal_type"]}'
                )
                st.caption(
                    f'{meal["calories"]} kcal · '
                    f'{meal["protein"]} g protein'
                )
        else:
            st.write("No meals logged yet.")

    st.divider()

    st.subheader("💡 Daily Tip")
    st.info(
        "Include a variety of vegetables, fruits, whole grains, "
        "protein-rich foods, and adequate water in your daily diet."
    )


# ---------- FOOD LOG ----------
with food_log:
    st.subheader("🍽️ Add a Meal")
    st.write("Choose a food, set the quantity, and record your meal.")

    with st.form("meal_form", clear_on_submit=True):
        selected_food = st.selectbox(
            "Select food",
            list(FOODS.keys())
        )

        meal_type = st.selectbox("Meal type", MEAL_TYPES)

        quantity = st.number_input(
            "Number of servings",
            min_value=0.25,
            max_value=20.0,
            value=1.0,
            step=0.25,
        )

        nutrition = FOODS[selected_food]

        st.caption(
            f'Per serving: {nutrition["calories"]} kcal · '
            f'{nutrition["protein"]} g protein · '
            f'{nutrition["carbs"]} g carbs · '
            f'{nutrition["fat"]} g fat'
        )

        submitted = st.form_submit_button(
            "➕ Add to Food Log",
            use_container_width=True,
        )

        if submitted:
            meal = {
                "date": date.today().isoformat(),
                "name": selected_food,
                "meal_type": meal_type,
                "calories": round(nutrition["calories"] * quantity),
                "protein": round(nutrition["protein"] * quantity, 1),
                "carbs": round(nutrition["carbs"] * quantity, 1),
                "fat": round(nutrition["fat"] * quantity, 1),
            }

            st.session_state.meals.append(meal)
            st.success(f"{selected_food} added successfully!")
            st.rerun()

    st.divider()

    st.subheader("📋 Today's Food Log")

    current_entries, current_totals = daily_totals()

    if current_entries:
        for index, meal in enumerate(current_entries):
            with st.container(border=True):
                col1, col2 = st.columns([4, 1])

                with col1:
                    st.write(f'**{meal["name"]}**')
                    st.caption(
                        f'{meal["meal_type"]} · '
                        f'{meal["calories"]} kcal · '
                        f'{meal["protein"]} g protein · '
                        f'{meal["carbs"]} g carbs · '
                        f'{meal["fat"]} g fat'
                    )

                with col2:
                    if st.button(
                        "🗑️",
                        key=f"delete_{index}",
                        help="Delete this entry",
                    ):
                        st.session_state.meals.remove(meal)
                        st.rerun()
    else:
        st.info("Your food log is empty. Add your first meal above.")


# ---------- MEAL PLANNER ----------
with planner:
    st.subheader("📅 Simple Daily Meal Planner")

    st.write(
        "Use these sample ideas to plan your day. "
        "Actual nutrition varies with ingredients and preparation."
    )

    suggestions = {
        "Breakfast": [
            "Idli with sambar",
            "Eggs with whole-grain toast",
            "Dosa with sambar",
        ],
        "Lunch": [
            "Rice, dal, vegetables and curd",
            "Chapati with dal and vegetables",
            "Rice with chicken and vegetables",
        ],
        "Dinner": [
            "Chapati with vegetables and dal",
            "Rice with vegetables and protein",
            "Egg curry with chapati",
        ],
        "Snacks": [
            "Fruit",
            "Curd",
            "A small serving of peanuts",
        ],
    }

    for category, foods in suggestions.items():
        with st.expander(f"🍴 {category}", expanded=True):
            for food in foods:
                st.write(f"• {food}")

    st.divider()

    st.subheader("🎯 Plan Around Your Goal")

    st.write(f"Your current daily calorie goal is **{st.session_state.calorie_goal} kcal**.")

    st.caption(
        "Your individual energy needs depend on factors such as age, "
        "height, weight, activity, and health. Treat this goal as "
        "a setting to review, not a medical recommendation."
    )


# ---------- FOOD GUIDE ----------
with food_guide:
    st.subheader("🥑 Nutrition Reference")

    st.write("Approximate nutrition per serving:")

    for food_name, values in FOODS.items():
        with st.container(border=True):
            col1, col2 = st.columns([2, 3])

            with col1:
                st.write(f"**{food_name}**")

            with col2:
                st.write(
                    f'{values["calories"]} kcal · '
                    f'Protein {values["protein"]} g · '
                    f'Carbs {values["carbs"]} g · '
                    f'Fat {values["fat"]} g'
                )

    st.caption(
        "Values are estimates, not laboratory measurements. "
        "Serving size, recipes, brands, and cooking methods can change them."
    )


# ---------- FOOTER ----------
st.divider()

st.caption(
    "Nutrition Assistant · Built with Streamlit and Python"
)
st.caption(
    "This app provides general nutrition information, "
    "not a substitute for professional medical advice."
)
