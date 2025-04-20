
import streamlit as st

st.set_page_config(page_title="NoCaries", layout="wide")

# Sidebar Navigation
st.sidebar.title("NoCaries App")
selection = st.sidebar.radio("Go to", [
    "Home", 
    "Brushing & Flossing Guide", 
    "Caries Risk Calculator", 
    "Oral Health Prevention Plan", 
    "Myth Busters", 
    "Quiz"
])

# Homepage
if selection == "Home":
    st.title("Welcome to NoCaries")
    st.markdown("### Caries Prevention Through Education")
    st.write(
        "Dental caries, also known as tooth decay, is one of the most common chronic diseases. "
        "It occurs when bacteria in the mouth produce acids that erode tooth enamel. "
        "This app will guide you through effective prevention strategies, interactive tools, and resources to protect your oral health."
    )

# Brushing & Flossing Guide
elif selection == "Brushing & Flossing Guide":
    st.header("Visual Guide to Brushing and Flossing")
    st.image("https://www.cdc.gov/oralhealth/images/brushing-teeth.jpg", caption="Proper Brushing Technique", use_column_width=True)
    st.image("https://www.cdc.gov/oralhealth/images/flossing.jpg", caption="Correct Flossing Method", use_column_width=True)

# Caries Risk Calculator
elif selection == "Caries Risk Calculator":
    st.header("Caries Risk Calculator")
    age = st.slider("What is your age?", 5, 80, 25)
    sugar_intake = st.radio("Do you consume sugary snacks/drinks daily?", ["Yes", "No"])
    brush_freq = st.radio("How many times do you brush per day?", ["0", "1", "2 or more"])
    floss = st.radio("Do you floss daily?", ["Yes", "No"])

    risk_score = 0
    risk_score += 1 if sugar_intake == "Yes" else 0
    risk_score += 1 if brush_freq == "0" else 0
    risk_score += 1 if floss == "No" else 0

    if risk_score == 0:
        st.success("Low risk of caries. Keep up the great habits!")
    elif risk_score == 1:
        st.warning("Moderate risk. Consider improving one area.")
    else:
        st.error("High risk of caries. Improve your oral hygiene and dietary habits.")

# Prevention Plan
elif selection == "Oral Health Prevention Plan":
    st.header("Your Personalized Prevention Plan")
    st.markdown("""
    - Brush twice daily with fluoride toothpaste.
    - Floss at least once a day.
    - Reduce sugar intake.
    - Visit the dentist twice a year.
    - Drink plenty of water.
    """)

# Myth Busters
elif selection == "Myth Busters":
    st.header("Oral Health Myth Busters")
    myths = {
        "You only need to see a dentist if your teeth hurt": "False. Regular check-ups prevent problems before they become painful.",
        "Sugar is the only cause of cavities": "False. Poor hygiene, lack of fluoride, and dry mouth also contribute.",
        "Brushing harder cleans better": "False. Brushing too hard can damage gums and enamel."
    }
    for myth, truth in myths.items():
        st.subheader(f"🧠 Myth: {myth}")
        st.markdown(f"✅ Truth: {truth}")

# Quiz
elif selection == "Quiz":
    st.header("Caries Prevention Quiz")
    q1 = st.radio("How often should you brush your teeth?", ["Once a day", "Twice a day", "After every meal"])
    q2 = st.radio("What ingredient helps prevent caries?", ["Salt", "Fluoride", "Baking soda"])
    q3 = st.radio("Which of these is NOT a cause of tooth decay?", ["Bacteria", "Flossing", "Sugary drinks"])

    score = 0
    score += 1 if q1 == "Twice a day" else 0
    score += 1 if q2 == "Fluoride" else 0
    score += 1 if q3 == "Flossing" else 0

    if st.button("Submit Answers"):
        st.success(f"You scored {score}/3!")
