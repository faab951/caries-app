
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="NoCaries", layout="wide")

# --- CUSTOM STYLING ---
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
    st.write("Welcome to NoCaries. Use this tool to explore dental caries, calculate your risk, and improve your oral health through evidence-based practices.")
    st.markdown("</div>", unsafe_allow_html=True)

def what_is_caries():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("What is Dental Caries?")
    stages = {
        "White Spot": ("https://www.dentalcare.com/-/media/project/dental-care/resources/en-us/images/white-spot.jpg", "Early sign of mineral loss on enamel."),
        "Enamel Decay": ("https://www.dentalcare.com/-/media/project/dental-care/resources/en-us/images/enamel-decay.jpg", "Breakdown of enamel, cavity starts."),
        "Dentin Involvement": ("https://www.dentalcare.com/-/media/project/dental-care/resources/en-us/images/dentin.jpg", "Decay spreads quickly through dentin."),
        "Pulp Exposure": ("https://www.dentalcare.com/-/media/project/dental-care/resources/en-us/images/pulp.jpg", "Pain and infection occur."),
        "Abscess": ("https://www.dentalcare.com/-/media/project/dental-care/resources/en-us/images/abscess.jpg", "Severe infection under tooth.")
    }
    stage = st.selectbox("Select a caries stage to learn more:", [""] + list(stages.keys()))
    if stage:
        img, desc = stages[stage]
        st.image(img, use_container_width=True)
        st.write(desc)
    st.markdown("</div>", unsafe_allow_html=True)

def myth_busters():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Myth Busters")
    myths = {
        "Sugar is the only cause of cavities.": "False. All fermentable carbs can contribute to caries, especially with poor oral hygiene.",
        "If it doesn't hurt, it's not a cavity.": "False. Many cavities are painless until they are severe.",
        "Fluoride is harmful.": "False. Fluoride is safe and helps prevent tooth decay.",
        "Mouthwash replaces brushing.": "False. It can help but cannot replace brushing and flossing.",
        "Only kids get cavities.": "False. Adults are also at risk, especially with receding gums and dry mouth."
    }
    for myth, fact in myths.items():
        with st.expander(myth):
            st.write(f"🦷 {fact}")
    st.markdown("</div>", unsafe_allow_html=True)

def risk_calculator():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Caries Risk Calculator")
    sugar = st.radio("How often do you consume sugary snacks?", ["Select", "Rarely", "Sometimes", "Frequently"])
    brushing = st.radio("How often do you brush your teeth?", ["Select", "Once daily", "Twice daily", "More than twice"])
    flossing = st.radio("Do you floss daily?", ["Select", "Yes", "No"])

    if "Select" not in [sugar, brushing, flossing]:
        score = 0
        if sugar == "Frequently": score += 2
        elif sugar == "Sometimes": score += 1
        if brushing == "Once daily": score += 1
        elif brushing == "More than twice": score -= 1
        if flossing == "No": score += 1
        if score <= 1:
            st.success("✅ Low Risk – Excellent oral care habits!")
        elif score <= 3:
            st.warning("⚠️ Moderate Risk – There’s room to improve.")
        else:
            st.error("🚨 High Risk – Take action to prevent decay.")
    st.markdown("</div>", unsafe_allow_html=True)

def oral_hygiene_guide():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Oral Hygiene Guide")
    tips = {
        "Brush Twice Daily": "Use fluoride toothpaste and brush for 2 minutes.",
        "Floss Daily": "Remove plaque between teeth where a brush can’t reach.",
        "Limit Sugar": "Reduce frequency of sugary foods and drinks.",
        "Mouthwash": "Use alcohol-free fluoride mouthwash at night.",
        "Hydration": "Drink water regularly, especially if you have dry mouth."
    }
    for title, desc in tips.items():
        st.markdown(f"**{title}**: {desc}")
    st.markdown("</div>", unsafe_allow_html=True)

def prevention_plan():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Your Daily Prevention Plan")
    time = st.selectbox("What time of day are you focusing on?", ["Morning", "Midday", "Night"])
    if time == "Morning":
        st.write("- Brush with fluoride toothpaste
- Avoid sugary breakfast
- Drink water")
    elif time == "Midday":
        st.write("- Rinse after meals
- Chew sugar-free gum
- Floss if possible")
    elif time == "Night":
        st.write("- Brush thoroughly before bed
- Use fluoride mouthwash
- Avoid snacks after brushing")
    st.markdown("</div>", unsafe_allow_html=True)

def case_scenarios():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Case Scenarios")
    cases = [
        ("Ali brushes once a day and drinks soda at night.", "He should brush twice daily and reduce soda."),
        ("Sara bleeds when flossing for the first time.", "Continue gentle flossing daily."),
        ("Tom has dry mouth and snacks frequently.", "Drink more water and reduce snacking."),
        ("Leena sees a white spot on her tooth.", "Visit a dentist—it may be early caries."),
        ("Ahmed brushes hard and has gum recession.", "Use a soft brush and brush gently.")
    ]
    for i, (case, advice) in enumerate(cases):
        st.subheader(f"Case {i+1}")
        st.write(case)
        st.info(f"Suggested action: {advice}")
    st.markdown("</div>", unsafe_allow_html=True)

def quiz():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Caries Prevention Quiz")
    questions = [
        ("How often should you brush your teeth?", ["Once", "Twice", "Only at night"], "Twice"),
        ("What does fluoride do?", ["Cleans teeth", "Strengthens enamel", "Whitening"], "Strengthens enamel"),
        ("Should you floss?", ["Yes", "No"], "Yes"),
        ("How often should you visit the dentist?", ["Every 6 months", "Once a year", "Only when in pain"], "Every 6 months"),
        ("Can mouthwash replace brushing?", ["Yes", "No"], "No")
    ]
    score = 0
    for i, (q, options, correct) in enumerate(questions):
        ans = st.radio(q, options, key=i)
        if ans == correct:
            score += 1
    if st.button("Submit Quiz"):
        st.success(f"Your score: {score} / {len(questions)}")
    st.markdown("</div>", unsafe_allow_html=True)

def faq():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Frequently Asked Questions")
    faqs = {
        "Do cavities always cause pain?": "No, many are painless until advanced.",
        "Can fluoride reverse early decay?": "Yes, it can remineralize early lesions.",
        "How often should I change my toothbrush?": "Every 3 months or after illness.",
        "Can cavities heal on their own?": "No, professional treatment is needed.",
        "Is bleeding after flossing normal?": "It’s common at first—keep flossing daily."
    }
    for q, a in faqs.items():
        with st.expander(q):
            st.write(a)
    st.markdown("</div>", unsafe_allow_html=True)

def about():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("About NoCaries")
    st.write("This app was built by dental students to provide interactive, evidence-based education on dental caries prevention for patient awareness and classroom engagement.")
    st.markdown("</div>", unsafe_allow_html=True)

# --- ROUTING ---
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
