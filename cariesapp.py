
import streamlit as st
st.set_page_config(page_title="NoCaries", layout="wide")  # Only set ONCE

# --- STYLING ---
st.markdown("""
<style>
body {
    background-color: #fdfcf9;
    font-family: 'Segoe UI', sans-serif;
    color: #333;
}
h1, h2 {
    color: #2c3e50;
}
.section {
    background-color: #f2ebe3;
    padding: 2em;
    border-radius: 12px;
    margin-bottom: 2em;
}
.stButton>button {
    background-color: #bba47c;
    color: white;
    font-size: 1em;
    padding: 0.5em 1.2em;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
page = st.sidebar.radio("Go to", [
    "Home", "What is Caries?", "Myth Busters", "Caries Risk Calculator",
    "Oral Hygiene Guide", "Prevention Plan", "Case Scenarios", "Quiz", "FAQ", "About"
])

# --- PAGE FUNCTIONS ---
if page == "Home":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Welcome to NoCaries")
    st.image("https://cdn.pixabay.com/photo/2017/04/10/22/29/dental-care-2223462_1280.jpg", use_container_width=True)
    st.write("""
    **NoCaries** is your go-to app for understanding, preventing, and managing dental caries.
    Explore interactive tools, learn with visuals, and assess your caries risk with just a few clicks.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "What is Caries?":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("What is Dental Caries?")
    stage = st.selectbox("Select a stage to learn more", ["", "White Spot", "Enamel Decay", "Dentin Decay", "Pulp Involvement", "Abscess"])
    info = {
        "White Spot": ("https://upload.wikimedia.org/wikipedia/commons/7/74/White_spot_lesions_on_teeth.jpg", "Early demineralization of enamel – reversible with fluoride."),
        "Enamel Decay": ("https://upload.wikimedia.org/wikipedia/commons/1/12/Enamel_Caries.jpg", "Decay breaks through enamel causing permanent damage."),
        "Dentin Decay": ("https://upload.wikimedia.org/wikipedia/commons/b/bb/Dental_caries_dentin.jpg", "Decay spreads faster once it reaches dentin."),
        "Pulp Involvement": ("https://upload.wikimedia.org/wikipedia/commons/0/0b/Pulpitis.jpg", "Pain begins when bacteria reach the pulp."),
        "Abscess": ("https://upload.wikimedia.org/wikipedia/commons/f/f6/Tooth_abscess.jpg", "Infection leads to swelling and severe pain.")
    }
    if stage in info:
        st.image(info[stage][0], use_container_width=True)
        st.write(info[stage][1])
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Myth Busters":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Myth Busters")
    myths = {
        "Sugar is the only cause of cavities.": "False – Any fermentable carbohydrate can cause decay.",
        "If it doesn’t hurt, it’s not a cavity.": "False – Early caries are painless.",
        "Fluoride is toxic.": "False – It's safe and protective in correct doses.",
        "Mouthwash replaces brushing.": "False – It’s only an add-on, not a replacement.",
        "Adults don’t get cavities.": "False – They do, especially with gum issues."
    }
    for myth, truth in myths.items():
        with st.expander(myth):
            st.write(truth)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Caries Risk Calculator":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Caries Risk Calculator")
    sugar = st.radio("Do you eat sugary snacks daily?", ["Yes", "No"])
    brush = st.radio("Do you brush twice a day?", ["Yes", "No"])
    floss = st.radio("Do you floss daily?", ["Yes", "No"])
    dry = st.radio("Do you experience dry mouth?", ["Yes", "No"])
    score = sum([sugar == "Yes", brush == "No", floss == "No", dry == "Yes"])
    if st.button("Calculate Risk"):
        if score <= 1:
            st.success("Low risk. Keep up the good work!")
        elif score == 2:
            st.warning("Moderate risk. Improve one or two habits.")
        else:
            st.error("High risk. You need a prevention plan.")
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Oral Hygiene Guide":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Oral Hygiene Tips")
    tips = {
        "Brush Twice": "Use fluoride toothpaste and soft brush twice daily.",
        "Floss Daily": "Cleans between teeth where brush can't reach.",
        "Mouthwash": "Use alcohol-free fluoride rinse at night.",
        "Limit Sugar": "Avoid frequent snacks and sugary drinks.",
        "Drink Water": "Helps flush food and acids between meals."
    }
    for t, d in tips.items():
        st.subheader(t)
        st.write(d)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Prevention Plan":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Build Your Prevention Plan")
    brush = st.selectbox("How often do you brush?", ["Once", "Twice", "More than twice"])
    sugar = st.selectbox("Sugar intake", ["Low", "Medium", "High"])
    water = st.selectbox("Do you drink water after meals?", ["Yes", "No"])
    if st.button("Generate Plan"):
        st.write("**Morning:** Brush + rinse with water.")
        if sugar != "Low":
            st.write("**Midday:** Rinse with water after meals.")
        st.write("**Night:** Brush, floss, and use mouthwash.")
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Case Scenarios":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Case Scenarios")
    case = st.selectbox("Choose a case", ["Ali - Soda at night", "Sara - Gums bleed", "Tom - Dry mouth", "Leena - White spot"])
    if "Ali" in case:
        st.write("Recommendation: Stop soda at night. Brush before bed.")
    elif "Sara" in case:
        st.write("Keep flossing daily. Bleeding is temporary.")
    elif "Tom" in case:
        st.write("Stay hydrated and limit snacks.")
    elif "Leena" in case:
        st.write("White spots need early fluoride intervention.")
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Quiz":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Caries Quiz")
    q1 = st.radio("Best time to brush?", ["Morning", "After meals", "Before bed"], key="q1")
    q2 = st.radio("What strengthens enamel?", ["Water", "Fluoride", "Milk"], key="q2")
    if st.button("Submit Quiz"):
        correct = (q1 == "Before bed") + (q2 == "Fluoride")
        st.write(f"Score: {correct}/2")
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "FAQ":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Frequently Asked Questions")
    faqs = {
        "Can cavities heal?": "No, only the very early stage can be reversed.",
        "How often to see a dentist?": "Every 6 months for checkups.",
        "Is mouthwash required?": "Helpful but not mandatory.",
        "Can adults get caries?": "Yes, especially with gum problems.",
        "Why does sugar cause decay?": "It feeds bacteria that make acid."
    }
    for q, a in faqs.items():
        with st.expander(q):
            st.write(a)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "About":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("About This Project")
    st.write("""
    This app was created to promote awareness and prevention of dental caries using interactive technology.
    Designed and developed by dental students using Streamlit.
    """)
    st.markdown("</div>", unsafe_allow_html=True)
