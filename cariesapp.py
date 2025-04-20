import streamlit as st

st.set_page_config(page_title="CariesFree: Prevent Cavities", layout="centered")

st.sidebar.title("CariesFree Navigation")
selection = st.sidebar.radio("Go to", ["Home", "What is Caries?", "Prevention Quiz", "Personalized Advice", "About Us"])

if selection == "Home":
    st.title("CariesFree: Protect Your Smile")
    st.image("https://www.cdc.gov/oralhealth/images/cavities.jpg", caption="Tooth decay is preventable!", use_column_width=True)
    st.markdown("""
    ### Welcome!
    Cavities (caries) are the most common preventable dental condition. Our goal is to help you protect your smile with simple, effective tips.
    - Brush twice daily
    - Floss once a day
    - Visit your dentist regularly
    """)

elif selection == "What is Caries?":
    st.title("What is Dental Caries?")
    st.markdown("""
    Dental caries, commonly known as cavities, are areas of tooth decay caused by:
    - Bacteria in the mouth
    - Frequent snacking or sugary drinks
    - Inadequate brushing and flossing

    ### How it Happens:
    1. Sugar feeds bacteria.
    2. Bacteria produce acid.
    3. Acid breaks down tooth enamel.
    """)
    st.image("https://www.verywellhealth.com/thmb/mrTCGLv-N4KL5-dN-hStAI4sKPY=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-533586003-587a2fba3df78c17b64a19dc.jpg", caption="Stages of tooth decay", use_column_width=True)

elif selection == "Prevention Quiz":
    st.title("Caries Prevention Quiz")
    score = 0
    q1 = st.radio("How long should you brush your teeth?", ["30 seconds", "1 minute", "2 minutes"])
    if q1 == "2 minutes":
        score += 1

    q2 = st.radio("How often should you floss?", ["Once a week", "Once a day", "Only when food gets stuck"])
    if q2 == "Once a day":
        score += 1

    q3 = st.radio("What causes caries?", ["Cold weather", "Sugar and bacteria", "Toothpaste"])
    if q3 == "Sugar and bacteria":
        score += 1

    q4 = st.radio("Is fluoride helpful?", ["Yes", "No", "Only for adults"])
    if q4 == "Yes":
        score += 1

    if st.button("Submit Quiz"):
        st.success(f"You scored {score}/4!")
        if score == 4:
            st.balloons()
            st.info("Excellent! You really know how to protect your teeth.")
        elif score >= 2:
            st.warning("Not bad! Keep brushing up on your knowledge.")
        else:
            st.error("Oops! Time to review caries prevention tips.")

elif selection == "Personalized Advice":
    st.title("Personalized Oral Health Advice")
    age_group = st.selectbox("Select your age group", ["Under 12", "12–18", "19–60", "60+"])
    brushing_freq = st.radio("How often do you brush per day?", ["Once", "Twice", "More than twice"])
    sugar_intake = st.radio("Do you consume sugary snacks/drinks daily?", ["Yes", "No"])

    st.subheader("Your Advice:")
    if brushing_freq == "Once":
        st.write("- Brush at least **twice a day** to protect your teeth.")
    if sugar_intake == "Yes":
        st.write("- Try to **reduce sugary snacks/drinks** and rinse your mouth after.")
    if age_group == "Under 12":
        st.write("- Make brushing fun with a **timer** or a **toothbrushing song**.")
    if age_group == "60+":
        st.write("- Schedule **regular checkups** and ask about dry mouth solutions.")

elif selection == "About Us":
    st.title("About Our Team")
    st.markdown("""
    We are a group of dental students passionate about oral health education.

    This tool was developed as part of our patient education project to make caries prevention accessible and engaging.

    **Team Members:**
    - Abdullah Al-Razhi
    - Mohammed Al-Sharif
    - Sadakah Basyouni
    - Mohammed Al-Shammrani
    - Maan Al-Ghamdi

    Thank you for visiting CariesFree!
    """)
