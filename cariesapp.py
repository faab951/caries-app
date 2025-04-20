
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
h1 {
    font-size: 2.2em;
    margin-bottom: 0.5em;
}
h2 {
    font-size: 1.6em;
    margin-bottom: 0.5em;
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
    st.image("https://cdn.pixabay.com/photo/2016/03/05/19/02/toothbrush-1238340_1280.jpg", use_container_width=True)
    st.write("Explore dental caries, calculate your risk, and build healthy habits with this interactive educational tool.")
    st.markdown("</div>", unsafe_allow_html=True)

def what_is_caries():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("What is Dental Caries?")
    stages = {
        "White Spot": ("https://upload.wikimedia.org/wikipedia/commons/7/74/White_spot_lesions_on_teeth.jpg", "Early sign of enamel demineralization."),
        "Enamel Decay": ("https://upload.wikimedia.org/wikipedia/commons/1/12/Enamel_Caries.jpg", "Decay begins on enamel surface."),
        "Dentin Involvement": ("https://upload.wikimedia.org/wikipedia/commons/b/bb/Dental_caries_dentin.jpg", "Decay reaches dentin, progressing faster."),
        "Pulp Exposure": ("https://upload.wikimedia.org/wikipedia/commons/0/0b/Pulpitis.jpg", "Painful inflammation from pulp involvement."),
        "Abscess": ("https://upload.wikimedia.org/wikipedia/commons/f/f6/Tooth_abscess.jpg", "Infection at root tip or surrounding tissue.")
    }
    stage = st.selectbox("Select a stage to explore:", [""] + list(stages.keys()))
    if stage:
        img, desc = stages[stage]
        st.image(img, use_container_width=True)
        st.write(desc)
    st.markdown("</div>", unsafe_allow_html=True)

def myth_busters():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Myth Busters")
    myths = {
        "Sugar is the only cause of cavities.": "False. All fermentable carbs can lead to decay.",
        "If it doesn't hurt, it's not a cavity.": "False. Cavities may be painless until advanced.",
        "Fluoride is harmful.": "False. Fluoride strengthens enamel safely.",
        "Mouthwash replaces brushing.": "False. It's only a supplement.",
        "Only children get cavities.": "False. Adults are also at risk."
    }
    for myth, fact in myths.items():
        with st.expander(myth):
            st.write(f"✅ {fact}")
    st.markdown("</div>", unsafe_allow_html=True)

def risk_calculator():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Caries Risk Calculator")
    sugar = st.radio("How often do you eat sugary snacks?", ["Select", "Rarely", "Sometimes", "Frequently"])
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
            st.success("✅ Low Risk – Great job!")
        elif score <= 3:
            st.warning("⚠️ Moderate Risk – Consider improving some habits.")
        else:
            st.error("🚨 High Risk – You need to change your routine.")
    st.markdown("</div>", unsafe_allow_html=True)

def oral_hygiene_guide():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Oral Hygiene Guide")
    tips = {
        "Brush Twice Daily": "Use fluoride toothpaste with a soft-bristled brush.",
        "Floss Daily": "Clean between your teeth once per day.",
        "Use Mouthwash": "Rinse with alcohol-free fluoride mouthwash at night.",
        "Limit Sugar": "Avoid frequent sugary snacks and drinks.",
        "Stay Hydrated": "Drink plenty of water throughout the day."
    }
    for tip, detail in tips.items():
        st.markdown(f"**{tip}**: {detail}")
    st.markdown("</div>", unsafe_allow_html=True)

def prevention_plan():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Your Personalized Prevention Plan")
    time = st.radio("Choose a time of day:", ["Morning", "Midday", "Night"])
    st.subheader(f"Recommended actions for {time}")
    if time == "Morning":
        st.write("- Brush with fluoride toothpaste")
        st.write("- Drink water and avoid sugary breakfast")
    elif time == "Midday":
        st.write("- Rinse your mouth after meals")
        st.write("- Chew sugar-free gum")
    elif time == "Night":
        st.write("- Brush before bed")
        st.write("- Use fluoride mouthwash")
        st.write("- No eating after brushing")
    st.markdown("</div>", unsafe_allow_html=True)

def case_scenarios():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Case Scenarios")
    scenarios = [
        ("Ali brushes once daily and drinks soda before bed.", "He should brush twice daily and avoid sugary drinks at night."),
        ("Sara’s gums bleed when flossing for the first time.", "This is common. She should continue gentle flossing daily."),
        ("Tom has dry mouth and snacks frequently.", "He should drink more water and limit snacking."),
        ("Leena sees a white spot on her tooth.", "It may be early decay. She should see her dentist."),
        ("Ahmed brushes hard and has gum recession.", "He should switch to a soft-bristled brush and use gentle technique.")
    ]
    for i, (case, advice) in enumerate(scenarios):
        st.subheader(f"Case {i+1}")
        st.write(case)
        st.info(f"Advice: {advice}")
    st.markdown("</div>", unsafe_allow_html=True)

def quiz():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Quiz")
    questions = [
        ("How often should you brush your teeth?", ["Once", "Twice", "Only at night"], "Twice"),
        ("What does fluoride do?", ["Cleans teeth", "Strengthens enamel", "Whitening"], "Strengthens enamel"),
        ("Should you floss?", ["Yes", "No"], "Yes"),
        ("How often to visit a dentist?", ["Every 6 months", "Once a year", "Only with pain"], "Every 6 months"),
        ("Does mouthwash replace brushing?", ["Yes", "No"], "No")
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
    st.title("Frequently Asked Questions")
    faqs = {
        "Do cavities always hurt?": "No, most don't hurt until they are advanced.",
        "Can fluoride reverse early decay?": "Yes, if caught early enough.",
        "How often should I change my toothbrush?": "Every 3 months.",
        "Can cavities heal on their own?": "No. They need to be treated.",
        "Is bleeding after flossing bad?": "It’s common at first. Keep flossing daily."
    }
    for q, a in faqs.items():
        with st.expander(q):
            st.write(a)
    st.markdown("</div>", unsafe_allow_html=True)

def about():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("About NoCaries")
    st.write("NoCaries is a student-led interactive oral health app designed to help patients and the public understand, assess, and prevent dental caries.")
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
