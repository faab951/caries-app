
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="NoCaries", layout="wide")

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            background-color: #fffaf0;
            color: #333333;
            font-size: 18px;
        }
        h1, h2, h3 {
            color: #2c3e50;
            font-weight: 600;
        }
        .section {
            background-color: #f7f0e9;
            padding: 1.2em;
            border-radius: 10px;
            margin-bottom: 2em;
        }
        .stButton>button {
            background-color: #bfa980;
            color: white;
            border-radius: 8px;
            padding: 0.6em 1.2em;
            font-size: 1em;
        }
    </style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
page = st.sidebar.selectbox("Navigate", [
    "Home", "What is Caries?", "Myth Busters", "Risk Calculator",
    "Oral Hygiene Guide", "Prevention Plan", "Case Scenarios", "Quiz", "FAQ", "About"
])

# --- PAGE FUNCTIONS ---

def home():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("NoCaries: Your Guide to Cavity Prevention")
    st.image("https://www.cdc.gov/oralhealth/images/dental-caries.jpg", use_container_width=True)
    st.markdown("Explore interactive tools to understand dental caries, evaluate your risk, and build a custom prevention plan.")
    st.markdown("</div>", unsafe_allow_html=True)

def what_is_caries():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("What is Dental Caries?")
    st.markdown("Click on each stage to learn more:")
    stages = {
        "White Spot": ("file-EbJD1iPDuayJXUjPRNHnnC", "Early demineralization appears as a white spot."),
        "Enamel Decay": ("file-8mtFP7xw56cWPVPNvXmhdT", "Enamel surface starts breaking down."),
        "Dentin Involvement": ("file-KXnJ47pgR2XyTczQS51xkf", "Decay reaches softer inner layer (dentin)."),
        "Pulp Exposure": ("file-Ku83XVRifiK2AMxSqB4NAh", "Infection reaches the pulp, causing pain."),
        "Abscess": ("file-U4ECuNVseBUmyQCQEVmwnW", "Severe decay leads to abscess and infection.")
    }
    choice = st.selectbox("Select a stage:", [""] + list(stages.keys()))
    if choice:
        image_id, description = stages[choice]
        st.image(f"/mnt/data/{image_id}", use_container_width=True)
        st.write(description)
    st.markdown("</div>", unsafe_allow_html=True)

def myth_busters():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Myth Busters")
    myths = {
        "Only sugar causes cavities.": "Sugar feeds bacteria, but all fermentable carbs contribute to decay.",
        "Brushing harder cleans better.": "Gentle, proper brushing is more effective and safer for gums.",
        "If it doesn't hurt, it's not a cavity.": "Decay can exist without pain until advanced stages.",
        "Fluoride is dangerous.": "Fluoride is safe and essential for strengthening enamel.",
        "Mouthwash replaces brushing.": "Mouthwash is an aid, not a substitute for brushing and flossing."
    }
    for myth, fact in myths.items():
        with st.expander(myth):
            st.write(f"✅ **Fact:** {fact}")
    st.markdown("</div>", unsafe_allow_html=True)

def risk_calculator():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Caries Risk Calculator")
    sugar = st.selectbox("How often do you eat sugary snacks?", ["", "Rarely", "Sometimes", "Often"])
    brush = st.selectbox("How often do you brush your teeth?", ["", "Once daily", "Twice daily", "More than twice"])
    floss = st.selectbox("Do you floss?", ["", "Never", "Occasionally", "Daily"])
    if sugar and brush and floss:
        score = 0
        if sugar == "Often": score += 2
        elif sugar == "Sometimes": score += 1
        if brush == "Once daily": score += 1
        elif brush == "": score += 2
        if floss == "Never": score += 2
        elif floss == "Occasionally": score += 1
        if score <= 2:
            st.success("🟢 Risk Level: Low – Keep up the good work!")
        elif score <= 4:
            st.warning("🟠 Risk Level: Moderate – Some habits need improvement.")
        else:
            st.error("🔴 Risk Level: High – Review your oral hygiene routine.")
    st.markdown("</div>", unsafe_allow_html=True)

def oral_hygiene():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Oral Hygiene Guide")
    tips = [
        ("Brushing Technique", "Use a soft-bristled toothbrush at a 45° angle for 2 minutes.", "file-KXnJ47pgR2XyTczQS51xkf"),
        ("Flossing", "Floss between each tooth daily to remove plaque.", "file-U4ECuNVseBUmyQCQEVmwnW"),
        ("Mouthwash", "Use fluoride mouthwash once a day, especially at night.", "file-JgQawVuupBc3tXaYqybTiU")
    ]
    for title, text, img_id in tips:
        st.image(f"/mnt/data/{img_id}", caption=title, use_container_width=True)
        st.markdown(f"**{title}:** {text}")
    st.markdown("</div>", unsafe_allow_html=True)

def prevention_plan():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Prevention Plan")
    sugar = st.selectbox("Do you frequently snack on sugary foods?", ["", "Yes", "No"])
    brush = st.selectbox("How many times do you brush?", ["", "Once", "Twice", "More than twice"])
    floss = st.selectbox("Do you floss?", ["", "Yes", "No"])
    st.subheader("Your Recommended Routine:")
    if sugar == "Yes":
        st.write("- Cut down on sugar intake between meals.")
    if brush != "Twice" and brush != "More than twice":
        st.write("- Increase brushing to at least twice daily with fluoride toothpaste.")
    if floss == "No":
        st.write("- Start flossing daily to remove plaque between teeth.")
    st.write("- Visit your dentist every 6 months.")
    st.markdown("</div>", unsafe_allow_html=True)

def case_scenarios():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Case Scenarios")
    cases = [
        ("Ali brushes once daily and drinks soda before bed. What should he change?", "Brush more often and avoid nighttime soda"),
        ("Sara notices bleeding when flossing for the first time. What should she do?", "Continue gently flossing daily"),
        ("Ahmed has dry mouth and sips coffee all day. Advice?", "Drink more water and limit acidic drinks"),
        ("Lina sees a black dot on her molar but feels no pain. Action?", "Visit dentist for evaluation"),
        ("Omar brushes hard with a stiff brush and has gum recession. Best advice?", "Use soft brush and gentle technique")
    ]
    for i, (question, correct) in enumerate(cases):
        st.write(f"**{i+1}. {question}**")
        choice = st.text_input("Your answer:", key=f"case{i}")
        if choice:
            st.write(f"✅ Correct Answer: {correct}")
    st.markdown("</div>", unsafe_allow_html=True)

def quiz():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Caries Prevention Quiz")
    questions = [
        ("How long should you brush your teeth?", ["1 min", "2 mins", "5 mins"], "2 mins"),
        ("How often should you floss?", ["Weekly", "Occasionally", "Daily"], "Daily"),
        ("What does fluoride do?", ["Strengthens enamel", "Whitens teeth", "None"], "Strengthens enamel"),
        ("Best brushing tool?", ["Soft brush", "Hard brush", "Finger"], "Soft brush"),
        ("Can cavities heal without treatment?", ["Yes", "No"], "No"),
        ("When should you visit a dentist?", ["Only if in pain", "Every 6 months", "Every 2 years"], "Every 6 months")
    ]
    score = 0
    for i, (q, opts, ans) in enumerate(questions):
        choice = st.radio(q, opts, key=f"quiz{i}")
        if choice == ans:
            score += 1
    if st.button("Submit Quiz"):
        st.success(f"You scored {score} out of {len(questions)}.")
    st.markdown("</div>", unsafe_allow_html=True)

def faq():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("FAQ")
    faqs = {
        "Can early cavities be reversed?": "Yes, through fluoride and improved oral hygiene.",
        "Should I use mouthwash?": "Yes, especially a fluoride-containing rinse at night.",
        "What is the best toothbrush?": "Soft-bristled manual or electric brush.",
        "Can I brush immediately after eating?": "Wait 30 minutes if you've had acidic foods.",
        "Is flossing really necessary?": "Yes, brushing alone doesn't clean between teeth.",
        "Why do my gums bleed when I floss?": "It's a sign you need to floss more, not stop.",
        "How often should I visit the dentist?": "Every 6 months for check-ups and cleanings.",
        "Do white spots mean decay?": "They can be early signs of demineralization.",
        "Do cavities always hurt?": "No, many are painless until advanced.",
        "Is sugar-free gum good?": "Yes, it can stimulate saliva and reduce risk."
    }
    for q, a in faqs.items():
        with st.expander(q):
            st.write(a)
    st.markdown("</div>", unsafe_allow_html=True)

def about():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("About NoCaries")
    st.markdown("""
**NoCaries** is a student-developed educational tool designed to promote caries prevention and patient empowerment through visual, interactive, and personalized learning content.  
This app is built for classroom presentations and public health awareness initiatives.
""")
    st.markdown("</div>", unsafe_allow_html=True)

# --- ROUTING ---
if page == "Home": home()
elif page == "What is Caries?": what_is_caries()
elif page == "Myth Busters": myth_busters()
elif page == "Risk Calculator": risk_calculator()
elif page == "Oral Hygiene Guide": oral_hygiene()
elif page == "Prevention Plan": prevention_plan()
elif page == "Case Scenarios": case_scenarios()
elif page == "Quiz": quiz()
elif page == "FAQ": faq()
elif page == "About": about()
