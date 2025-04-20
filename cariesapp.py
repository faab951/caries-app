
def caries_risk_calculator():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Caries Risk Calculator")
    st.write("Answer the questions below to assess your risk of developing dental caries.")
    sugar = st.radio("How often do you consume sugary snacks or drinks?", ["Rarely", "Sometimes", "Frequently"])
    brushing = st.radio("How often do you brush your teeth?", ["Once a day", "Twice a day", "More than twice a day"])
    flossing = st.radio("Do you floss daily?", ["Yes", "No"])
    dry_mouth = st.radio("Do you experience dry mouth frequently?", ["Yes", "No"])

    score = 0
    if sugar == "Sometimes": score += 1
    elif sugar == "Frequently": score += 2
    if brushing == "Once a day": score += 1
    elif brushing == "More than twice a day": score -= 1
    if flossing == "No": score += 1
    if dry_mouth == "Yes": score += 1

    if st.button("Calculate My Risk"):
        if score <= 1:
            st.success("🟢 Low Risk – Keep up the good habits!")
        elif score == 2:
            st.warning("🟡 Moderate Risk – You can improve a few areas.")
        else:
            st.error("🔴 High Risk – Take action to reduce your risk.")
    st.markdown("</div>", unsafe_allow_html=True)

def oral_hygiene_guide():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Oral Hygiene Guide")
    tips = {
        "Brush Twice Daily": ("https://cdn.pixabay.com/photo/2020/09/25/13/21/toothbrush-5601924_1280.jpg", 
            "Use fluoride toothpaste and brush for two minutes each morning and night."),
        "Floss Once Daily": ("https://cdn.pixabay.com/photo/2016/03/05/19/02/dental-floss-1238342_1280.jpg", 
            "Flossing removes plaque and food particles from between your teeth."),
        "Use Mouthwash": ("https://cdn.pixabay.com/photo/2021/08/17/13/06/mouthwash-6552301_1280.jpg", 
            "Use alcohol-free mouthwash to reduce bacteria and freshen breath."),
        "Limit Sugar Intake": ("https://cdn.pixabay.com/photo/2016/04/13/07/18/sugar-1324237_1280.jpg", 
            "Reduce snacking on sugary foods and drinks, especially between meals."),
        "Stay Hydrated": ("https://cdn.pixabay.com/photo/2017/06/10/06/06/bottle-2384733_1280.jpg", 
            "Drinking water helps wash away food and bacteria and stimulates saliva.")
    }
    for tip, (img, desc) in tips.items():
        st.image(img, caption=tip, use_container_width=True)
        st.write(f"**{tip}**: {desc}")
    st.markdown("</div>", unsafe_allow_html=True)

def prevention_plan():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Prevention Plan Builder")
    brushing = st.selectbox("How often do you brush?", ["Once", "Twice", "More than twice"])
    sugar = st.selectbox("How often do you eat sweets or drink soda?", ["Rarely", "Sometimes", "Frequently"])
    water = st.selectbox("Do you drink water after meals?", ["Yes", "No"])
    
    st.subheader("Your Personalized Routine:")
    if brushing == "Once": st.write("- Increase brushing to twice daily.")
    else: st.write("- Great brushing frequency!")
    if sugar == "Frequently": st.write("- Reduce sugary snacks and drinks.")
    if water == "No": st.write("- Try rinsing your mouth with water after meals.")
    st.markdown("</div>", unsafe_allow_html=True)

def case_scenarios():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Case Scenarios")
    cases = [
        ("Leena notices a white spot on her tooth that wasn't there before.", 
         ["Ignore it", "Start brushing more", "Visit a dentist"], "Visit a dentist"),
        ("Ahmed brushes three times a day with a hard brush and has gum recession.", 
         ["Brush more", "Use a soft brush and be gentle", "Floss harder"], "Use a soft brush and be gentle"),
        ("Sara’s gums bleed when she flosses for the first time.", 
         ["Stop flossing", "Keep flossing daily gently", "Brush more instead"], "Keep flossing daily gently"),
        ("Tom has constant dry mouth and snacks often.", 
         ["Drink soda", "Chew sugar-free gum and drink water", "Ignore it"], "Chew sugar-free gum and drink water"),
        ("Ali brushes once daily and drinks soda before bed.", 
         ["Continue routine", "Drink water after soda", "Brush twice daily and avoid soda at night"], "Brush twice daily and avoid soda at night")
    ]
    for i, (q, options, answer) in enumerate(cases):
        st.subheader(f"Case {i+1}")
        choice = st.radio(q, options, key=f"case{i}")
        if st.button(f"Submit Answer {i+1}"):
            if choice == answer:
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Incorrect. The correct answer is: {answer}")
    st.markdown("</div>", unsafe_allow_html=True)

def quiz():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("Quiz")
    questions = [
        ("How long should you brush your teeth?", ["1 min", "2 mins", "5 mins"], "2 mins"),
        ("What helps strengthen enamel?", ["Fluoride", "Salt", "Baking soda"], "Fluoride"),
        ("Is flossing necessary?", ["Yes", "No"], "Yes"),
        ("What food causes most decay?", ["Vegetables", "Candy", "Cheese"], "Candy"),
        ("When should you visit a dentist?", ["When in pain", "Every 6 months", "Every 5 years"], "Every 6 months")
    ]
    score = 0
    for i, (q, opts, correct) in enumerate(questions):
        ans = st.radio(q, opts, key=f"quiz{i}")
        if ans == correct:
            score += 1
    if st.button("Submit Quiz"):
        st.success(f"Your score: {score} / {len(questions)}")
    st.markdown("</div>", unsafe_allow_html=True)

def faq():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("FAQs")
    questions = {
        "What is a cavity?": "A cavity is a hole in your tooth caused by tooth decay.",
        "Can cavities heal on their own?": "No. Once a cavity forms, it needs treatment.",
        "Is bleeding when flossing normal?": "It is common when starting. Keep flossing gently.",
        "How often should I change my toothbrush?": "Every 3 months or after sickness.",
        "Is it okay to skip brushing at night?": "No. Night brushing is essential.",
        "Does fluoride cause harm?": "No, fluoride is safe and prevents decay.",
        "Should kids use mouthwash?": "Only under supervision and if age-appropriate.",
        "Can diet affect oral health?": "Yes. Sugar increases risk. Fiber and calcium help.",
        "What toothbrush is best?": "A soft-bristled brush is ideal for most people.",
        "How often should I visit the dentist?": "Every 6 months or as recommended."
    }
    for q, a in questions.items():
        with st.expander(q):
            st.write(a)
    st.markdown("</div>", unsafe_allow_html=True)

def about():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.title("About NoCaries")
    st.write("""
        NoCaries was developed by dental students passionate about preventive care. 
        This tool empowers patients and learners to better understand dental caries through interactive education.
        Built using Streamlit with verified sources and public images.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# --- ROUTING ---
if page == "Home": home()
elif page == "What is Caries?": what_is_caries()
elif page == "Myth Busters": myth_busters()
elif page == "Caries Risk Calculator": caries_risk_calculator()
elif page == "Oral Hygiene Guide": oral_hygiene_guide()
elif page == "Prevention Plan": prevention_plan()
elif page == "Case Scenarios": case_scenarios()
elif page == "Quiz": quiz()
elif page == "FAQ": faq()
elif page == "About": about()
