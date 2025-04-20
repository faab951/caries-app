
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="NoCaries", layout="wide")

# --- STYLING ---
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
    background-color: #fffaf0;
    color: #333;
}
h1, h2 {
    color: #2c3e50;
}
.section {
    background-color: #f5efe6;
    padding: 1.5em;
    border-radius: 10px;
    margin-bottom: 2em;
}
.stButton>button {
    background-color: #bfa980;
    color: white;
    font-size: 1em;
    border-radius: 8px;
    padding: 0.5em 1em;
}
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
page = st.sidebar.selectbox("Navigate", [
    "Home", "What is Caries?", "Myth Busters", "Risk Calculator",
    "Oral Hygiene Guide", "Prevention Plan", "Case Scenarios",
    "Quiz", "FAQ", "About"
])

# --- PAGE FUNCTIONS ---
def home():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("NoCaries: Your Guide to Cavity Prevention")
    st.image("https://www.cdc.gov/oralhealth/images/dental-caries.jpg", use_container_width=True)
    st.write("Welcome to NoCaries. Explore dental caries, calculate your risk, and learn how to maintain a healthy smile.")
    st.markdown("</div>", unsafe_allow_html=True)

def what_is_caries():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("What is Dental Caries?")
    stages = {
        "White Spot": ("https://www.dentalcare.com/-/media/project/dental-care/resources/en-us/images/white-spot.jpg", "Early sign of mineral loss."),
        "Enamel Decay": ("https://www.dentalcare.com/-/media/project/dental-care/resources/en-us/images/enamel-decay.jpg", "Cavity begins in enamel."),
        "Dentin Involvement": ("https://www.dentalcare.com/-/media/project/dental-care/resources/en-us/images/dentin.jpg", "Decay spreads faster through dentin."),
        "Pulp Exposure": ("https://www.dentalcare.com/-/media/project/dental-care/resources/en-us/images/pulp.jpg", "Painful pulp involvement."),
        "Abscess": ("https://www.dentalcare.com/-/media/project/dental-care/resources/en-us/images/abscess.jpg", "Serious infection forms.")
    }
    stage = st.selectbox("Select a stage:", [""] + list(stages.keys()))
    if stage:
        img, desc = stages[stage]
        st.image(img, use_container_width=True)
        st.write(desc)
    st.markdown("</div>", unsafe_allow_html=True)

def myth_busters():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Myth Busters")
    myths = {
        "Sugar is the only cause of cavities.": "False. All fermentable carbohydrates can contribute.",
        "If it doesn't hurt, it's not a cavity.": "False. Pain comes later in decay.",
        "Fluoride is harmful.": "False. Fluoride is safe and strengthens enamel.",
        "Mouthwash replaces brushing.": "False. It’s an addition, not a replacement.",
        "Only kids get cavities.": "False. Adults are also at risk."
    }
    for myth, fact in myths.items():
        with st.expander(myth):
            st.write(f"✅ {fact}")
    st.markdown("</div>", unsafe_allow_html=True)

def risk_calculator():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Caries Risk Calculator")
    sugar = st.radio("How often do you consume sugary snacks?", ["Select", "Rarely", "Sometimes", "Frequently"])
    brushing = st.radio("How often do you brush?", ["Select", "Once daily", "Twice daily", "More than twice"])
    flossing = st.radio("Do you floss daily?", ["Select", "Yes", "No"])

    if "Select" not in [sugar, brushing, flossing]:
        score = 0
        if sugar == "Frequently": score += 2
        elif sugar == "Sometimes": score += 1
        if brushing == "Once daily": score += 1
        elif brushing == "More than twice": score -= 1
        if flossing == "No": score += 1
        if score <= 1:
            st.success("✅ Low Risk – Excellent hygiene habits!")
        elif score <= 3:
            st.warning("⚠️ Moderate Risk – There’s room to improve.")
        else:
            st.error("🚨 High Risk – Take steps to prevent decay.")
    st.markdown("</div>", unsafe_allow_html=True)

def oral_hygiene_guide():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Oral Hygiene Guide")
    tips = {
        "Brush Twice Daily": "Use fluoride toothpaste and a soft-bristled brush.",
        "Floss Daily": "Reach the areas between your teeth where your brush can't.",
        "Use Mouthwash": "Fluoride mouthwash can help prevent decay.",
        "Limit Sugar": "Eat fewer sugary foods and drinks, especially between meals.",
        "Drink Water": "Stay hydrated and rinse after meals."
    }
    for tip, detail in tips.items():
        st.markdown(f"**{tip}**: {detail}")
    st.markdown("</div>", unsafe_allow_html=True)

def prevention_plan():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Prevention Plan Builder")
    time = st.radio("Select a time of day:", ["Morning", "Midday", "Night"])
    if time == "Morning":
        st.write("- Brush teeth with fluoride toothpaste")
        st.write("- Avoid sugary breakfast")
        st.write("- Drink water to start the day")
    elif time == "Midday":
        st.write("- Rinse mouth after meals")
        st.write("- Chew sugar-free gum")
        st.write("- Floss if possible")
    elif time == "Night":
        st.write("- Brush thoroughly before bed")
        st.write("- Use fluoride mouthwash")
        st.write("- Avoid snacking after brushing")
    st.markdown("</div>", unsafe_allow_html=True)

def case_scenarios():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Case Scenarios")
    cases = [
        ("Ali brushes once and drinks soda before bed.", "Brush twice daily and stop soda at night."),
        ("Sara’s gums bleed when flossing for the first time.", "Continue flossing gently daily."),
        ("Tom has dry mouth and snacks often.", "Drink water more often and reduce snacking."),
        ("Leena sees a white spot on her tooth.", "Visit the dentist—it may be early caries."),
        ("Ahmed brushes hard with a stiff brush.", "Use a soft brush and gentle strokes.")
    ]
    for i, (case, advice) in enumerate(cases):
        st.subheader(f"Case {i+1}")
        st.write(case)
        st.info(f"Suggested advice: {advice}")
    st.markdown("</div>", unsafe_allow_html=True)

def quiz():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Quiz")
    questions = [
        ("How often should you brush your teeth?", ["Once", "Twice", "Only at night"], "Twice"),
        ("What does fluoride do?", ["Cleans teeth", "Strengthens enamel", "Whitening"], "Strengthens enamel"),
        ("Should you floss?", ["Yes", "No"], "Yes"),
        ("How often should you visit the dentist?", ["Every 6 months", "Once a year", "Only when in pain"], "Every 6 months"),
        ("Can mouthwash replace brushing?", ["Yes", "No"], "No")
    ]
    score = 0
    for i, (q, opts, ans) in enumerate(questions):
        response = st.radio(q, opts, key=f"quiz{i}")
        if response == ans:
            score += 1
    if st.button("Submit Quiz"):
        st.success(f"Your score: {score} / {len(questions)}")
    st.markdown("</div>", unsafe_allow_html=True)

def faq():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("FAQs")
    faqs = {
        "Do cavities always hurt?": "No, many are painless until advanced.",
        "Can fluoride reverse early decay?": "Yes, it can remineralize enamel.",
        "How often to change toothbrush?": "Every 3 months or after illness.",
        "Can cavities heal on their own?": "No, they need dental treatment.",
        "Is bleeding after flossing bad?": "No, it’s common early on—keep flossing."
    }
    for q, a in faqs.items():
        with st.expander(q):
            st.write(a)
    st.markdown("</div>", unsafe_allow_html=True)

def about():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("About NoCaries")
    st.write("This app was developed by dental students to raise awareness on cavity prevention through interactive learning tools.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- ROUTER ---
if page == "Home": home()
elif page == "What is Caries?": what_is_caries()
elif page == "Myth Busters": myth_busters()
elif page == "Risk Calculator": risk_calculator()
elif page == "Oral Hygiene Guide": oral_hygiene_guide()
elif page == "Prevention Plan": prevention_plan()
elif page == "Case Scenarios": case_scenarios()
elif page == "Quiz": quiz()
elif page == "FAQ": faq()
elif page == "About": about()
