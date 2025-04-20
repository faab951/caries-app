import streamlit as st

st.set_page_config(page_title="NoCaries | Prevent Tooth Decay", layout="centered")

# Custom Style
st.markdown("""
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
        }
        .main h1 {
            font-size: 2.4em;
            color: #2a9d8f;
        }
        .stButton>button {
            background-color: #2a9d8f;
            color: white;
            border-radius: 10px;
            font-size: 1em;
            padding: 0.5em 1.5em;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("NoCaries Navigation")
selection = st.sidebar.radio("Explore", ["🏠 Home", "❓ What is Caries?", "🧠 Quiz", "💡 Personalized Advice", "👥 About NoCaries"])

if selection == "🏠 Home":
    st.title("NoCaries: A Smarter Way to Prevent Cavities")

    st.markdown("### What would you like to learn today?")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🛡️ Why Prevent?"):
            st.info("Preventing caries means protecting enamel before damage begins.")
    with col2:
        if st.button("🪥 How to Brush"):
            st.success("Use a soft-bristled brush for 2 minutes, twice a day.")
    with col3:
        if st.button("🍭 Sugar Danger"):
            st.warning("Sugar feeds acid-producing bacteria — limit snacking!")

elif selection == "❓ What is Caries?":
    st.title("What is Dental Caries?")
    with st.expander("Step 1: Bacteria in the Mouth"):
        st.write("Your mouth naturally has bacteria. Some are harmful.")
    with st.expander("Step 2: Sugar Enters"):
        st.write("Bacteria consume sugar and produce acids.")
    with st.expander("Step 3: Acid Attacks Enamel"):
        st.write("Acid dissolves enamel, leading to soft spots (incipient caries).")
    with st.expander("Step 4: Cavity Forms"):
        st.write("The hole expands deeper into the dentin, forming a cavity.")

elif selection == "🧠 Quiz":
    st.title("Caries Prevention Quiz")
    score = 0

    if st.radio("1️⃣ How long should you brush?", ["30 secs", "1 min", "2 mins"]) == "2 mins":
        score += 1
    if st.radio("2️⃣ What's the best flossing habit?", ["Weekly", "Daily", "When food stuck"]) == "Daily":
        score += 1
    if st.radio("3️⃣ What causes caries?", ["Toothpaste", "Cold drinks", "Sugar & bacteria"]) == "Sugar & bacteria":
        score += 1
    if st.radio("4️⃣ Is fluoride helpful?", ["Yes", "No", "Only for kids"]) == "Yes":
        score += 1

    if st.button("See My Score"):
        st.success(f"✅ You scored {score}/4")
        if score == 4:
            st.balloons()
            st.info("Excellent! You're a NoCaries pro.")
        elif score >= 2:
            st.warning("Good effort! Review the tips above.")
        else:
            st.error("Let’s revisit some prevention basics!")

elif selection == "💡 Personalized Advice":
    st.title("Get Your Dental Prevention Plan")
    age = st.selectbox("How old are you?", ["Under 12", "12–18", "19–60", "60+"])
    brushing = st.radio("How often do you brush daily?", ["Once", "Twice", "More than twice"])
    sugar = st.radio("Do you consume sugary snacks daily?", ["Yes", "No"])

    st.subheader("🪞 Your Tips:")
    if brushing == "Once":
        st.write("- Brush **twice a day** with fluoride toothpaste.")
    if sugar == "Yes":
        st.write("- Limit sugar intake and rinse after snacks.")
    if age == "Under 12":
        st.write("- Use kids’ toothpaste with supervision.")
    if age == "60+":
        st.write("- Visit your dentist regularly to manage dry mouth or wear.")

elif selection == "👥 About NoCaries":
    st.title("About NoCaries")
    st.markdown("""
    **NoCaries** is a student-led initiative to educate and empower people about cavity prevention using interactive, digital tools.

    **Team Members:**  
    - Student A  
    - Student B  
    - Student C  
    - Student D

    Developed as part of our Caries Prevention Awareness Project.
    """)
