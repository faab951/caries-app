
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="NoCaries", layout="wide")

# --- CUSTOM STYLE ---
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
    font-size: 18px;
    background-color: #fdfdfc;
    color: #1e1e1e;
}
.main h1 {
    font-size: 2.5em;
    color: #2c3e50;
    font-weight: 600;
}
.stButton>button {
    background-color: #bfa980;
    color: white;
    border-radius: 8px;
    font-size: 1.1em;
    padding: 0.5em 1.5em;
}
</style>
""", unsafe_allow_html=True)

# --- LANGUAGE TOGGLE ---
lang = st.sidebar.radio("Language / اللغة", ["English", "Arabic"])

# --- NAVIGATION ---
page = st.sidebar.selectbox("Navigate", [
    "🏠 Home", "📚 What is Caries?", "❌ Myth Busters", "🧮 Risk Calculator",
    "🪥 Oral Hygiene Guide", "📅 Prevention Plan", "💬 Case Scenarios",
    "🧠 Quiz", "❓ FAQ", "👥 About"
])

# --- SECTION FUNCTIONS ---

def home():
    if lang == "English":
        st.title("NoCaries: Cavity Prevention for Lifelong Oral Health")
        st.markdown("""Welcome to **NoCaries**, a luxury bilingual platform for modern oral health education."""")
    else:
        st.title("نوكاريس: الوقاية من التسوس لصحة فموية تدوم")
        st.markdown("مرحبًا بكم في **نوكاريس**، منصة ثنائية اللغة لتعليم صحة الفم بأسلوب عصري.")

def what_is_caries():
    st.title("What is Dental Caries?" if lang == "English" else "ما هو تسوس الأسنان؟")
    st.image("https://www.cdc.gov/oralhealth/images/cavities.jpg", use_column_width=True)
    if lang == "English":
        st.markdown("""
Dental caries is a bacterial process causing tooth decay.  
**Stages**: White spot → Enamel decay → Dentin → Pulp → Abscess
""")
    else:
        st.markdown("""
تسوس الأسنان هو عملية بكتيرية تؤدي إلى تآكل السن.  
**المراحل**: بقعة بيضاء → تسوس المينا → العاج → اللب → خراج
""")

def myth_busters():
    st.title("Myth Busters" if lang == "English" else "كشف الخرافات")
    myths = {
        "Only kids get cavities": "Anyone can.",
        "You don't need to floss": "Flossing is essential.",
        "No pain = No cavity": "Early decay is painless."
    }
    myths_ar = {
        "فقط الأطفال يصابون بالتسوس": "أي شخص يمكن أن يصاب.",
        "لا حاجة للخيط": "الخيط ضروري.",
        "عدم وجود ألم = لا يوجد تسوس": "التسوس المبكر غير مؤلم."
    }
    data = myths if lang == "English" else myths_ar
    for myth, truth in data.items():
        with st.expander(myth):
            st.write(truth)

def risk_calculator():
    st.title("Caries Risk Calculator" if lang == "English" else "حاسبة خطر التسوس")
    sugar = st.radio("Do you eat sugar daily?" if lang == "English" else "هل تتناول السكر يوميًا؟", ["Yes", "No"])
    brush = st.radio("Brush twice daily?" if lang == "English" else "هل تفرّش مرتين يوميًا؟", ["Yes", "No"])
    risk = "High" if sugar == "Yes" and brush == "No" else "Moderate" if sugar == "Yes" else "Low"
    st.success(f"Your risk is: {risk}" if lang == "English" else f"مستوى الخطر: {'مرتفع' if risk=='High' else 'متوسط' if risk=='Moderate' else 'منخفض'}")

def oral_hygiene():
    st.title("Oral Hygiene Guide" if lang == "English" else "دليل العناية الفموية")
    st.image("https://www.cdc.gov/oralhealth/images/how-to-brush-300px.jpg", use_column_width=True)
    if lang == "English":
        st.markdown("- Brush twice daily  
- Floss once daily  
- Use fluoride toothpaste")
    else:
        st.markdown("- فرّش مرتين يوميًا  
- استخدم الخيط مرة يوميًا  
- استخدم معجون يحتوي على الفلورايد")

def prevention_plan():
    st.title("Build Your Prevention Plan" if lang == "English" else "أنشئ خطة الوقاية")
    age = st.slider("Your age" if lang == "English" else "عمرك", 5, 80, 25)
    sugar = st.radio("Do you snack on sweets?" if lang == "English" else "هل تتناول الحلويات؟", ["Yes", "No"])
    brushing = st.radio("How often do you brush?" if lang == "English" else "كم مرة تفرّش؟", ["Once", "Twice", "More than Twice"])
    st.subheader("Suggested Plan" if lang == "English" else "الخطة المقترحة")
    if brushing == "Once":
        st.write("- Brush twice daily with fluoride")
    if sugar == "Yes":
        st.write("- Reduce sugar intake and rinse after snacks")
    st.write("- Visit dentist every 6 months")

def case_scenarios():
    st.title("Case Scenario" if lang == "English" else "سيناريو واقعي")
    if lang == "English":
        choice = st.radio("Ali brushes once/day and drinks soda daily. What should he do?", ["Brush more often", "Nothing", "Drink more water"])
        st.success("Correct" if choice == "Brush more often" else "That's not ideal. Try again.")
    else:
        choice = st.radio("علي يفرّش مرة واحدة يوميًا ويشرب الصودا. ماذا يجب أن يفعل؟", ["يفرّش أكثر", "لا شيء", "يشرب ماء أكثر"])
        st.success("إجابة صحيحة" if choice == "يفرّش أكثر" else "ليست الأفضل، حاول مرة أخرى.")

def quiz():
    st.title("Caries Prevention Quiz" if lang == "English" else "اختبار الوقاية من التسوس")
    score = 0
    q1 = st.radio("1. Ideal brushing frequency?", ["Once", "Twice", "After every snack"])
    if q1 == "Twice": score += 1
    q2 = st.radio("2. What causes caries?", ["Cold", "Sugar + bacteria", "Water"])
    if q2 == "Sugar + bacteria": score += 1
    if st.button("Submit"):
        st.success(f"You scored {score}/2" if lang == "English" else f"نتيجتك {score} من 2")

def faq():
    st.title("Frequently Asked Questions" if lang == "English" else "الأسئلة الشائعة")
    faqs = {
        "Can cavities heal on their own?": "No, they need treatment.",
        "How often should I visit the dentist?": "Every 6 months."
    }
    faqs_ar = {
        "هل يشفى التسوس من تلقاء نفسه؟": "لا، يحتاج إلى علاج.",
        "كم مرة أزور طبيب الأسنان؟": "كل 6 أشهر."
    }
    data = faqs if lang == "English" else faqs_ar
    for question, answer in data.items():
        with st.expander(question):
            st.write(answer)

def about():
    st.title("About NoCaries" if lang == "English" else "حول نوكاريس")
    st.markdown("This bilingual project is designed to promote oral health education and cavity prevention." if lang == "English"
                else "هذا المشروع ثنائي اللغة يهدف إلى تعزيز التوعية بصحة الفم والوقاية من التسوس.")

# --- ROUTER ---
if page == "🏠 Home": home()
elif page == "📚 What is Caries?": what_is_caries()
elif page == "❌ Myth Busters": myth_busters()
elif page == "🧮 Risk Calculator": risk_calculator()
elif page == "🪥 Oral Hygiene Guide": oral_hygiene()
elif page == "📅 Prevention Plan": prevention_plan()
elif page == "💬 Case Scenarios": case_scenarios()
elif page == "🧠 Quiz": quiz()
elif page == "❓ FAQ": faq()
elif page == "👥 About": about()
