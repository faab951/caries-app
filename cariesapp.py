
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
        st.markdown("""
Welcome to **NoCaries**, a luxury bilingual platform for modern oral health education.  
Use the sidebar to navigate through interactive tools designed to help you understand and prevent dental caries effectively.
""")
    else:
        st.title("نوكاريس: الوقاية من التسوس لصحة فموية تدوم")
        st.markdown("""
مرحبًا بكم في **نوكاريس**، منصة ثنائية اللغة للتثقيف الصحي الفموي بأسلوب راقٍ.  
استخدم القائمة الجانبية لاستكشاف أدوات تفاعلية تساعدك على فهم تسوس الأسنان والوقاية منه.
""")

def what_is_caries():
    st.title("What is Dental Caries?" if lang == "English" else "ما هو تسوس الأسنان؟")
    st.image("https://www.cdc.gov/oralhealth/images/cavities.jpg", use_column_width=True)
    content_en = """**Dental caries** is a bacterial process that causes destruction of the tooth's hard tissues by acid produced from sugar.  
**Stages:**  
- White spot lesion  
- Enamel breakdown  
- Dentin involvement  
- Pulp exposure  
- Abscess or tooth loss"""
    content_ar = """**تسوس الأسنان** هو عملية بكتيرية تؤدي إلى تآكل الأنسجة الصلبة للسن نتيجة الأحماض الناتجة عن السكريات.  
**المراحل:**  
- بقعة بيضاء  
- تآكل المينا  
- إصابة العاج  
- تعرض اللب  
- خراج أو فقدان السن"""
    st.markdown(content_en if lang == "English" else content_ar)

def myth_busters():
    st.title("Myth Busters" if lang == "English" else "كشف الخرافات")
    myths = {
        "Only kids get cavities": "Anyone with teeth can get cavities.",
        "Flossing isn’t necessary if you brush": "Brushing only cleans 60% of surfaces.",
        "If it doesn't hurt, it’s not a cavity": "Cavities often don't hurt until they're advanced."
    }
    myths_ar = {
        "فقط الأطفال يصابون بالتسوس": "أي شخص لديه أسنان يمكن أن يصاب بالتسوس.",
        "لا حاجة لاستخدام الخيط إذا قمت بالتفريش": "التفريش ينظف فقط 60٪ من الأسطح.",
        "إذا لم يكن هناك ألم، فلا يوجد تسوس": "التسوس لا يسبب ألمًا حتى يصبح متقدمًا."
    }
    data = myths if lang == "English" else myths_ar
    for myth, truth in data.items():
        with st.expander(myth):
            st.write(truth)

def risk_calculator():
    st.title("Caries Risk Calculator" if lang == "English" else "حاسبة خطر التسوس")
    sugar = st.radio("Do you eat sugary snacks daily?" if lang == "English" else "هل تتناول الحلويات يوميًا؟", ["Yes", "No"])
    brushing = st.radio("Do you brush twice a day?" if lang == "English" else "هل تفرّش مرتين يوميًا؟", ["Yes", "No"])
    flossing = st.radio("Do you floss daily?" if lang == "English" else "هل تستخدم الخيط يوميًا؟", ["Yes", "No"])
    risk = "Low"
    if sugar == "Yes" and brushing == "No":
        risk = "High"
    elif sugar == "Yes" or brushing == "No":
        risk = "Moderate"
    label = {"Low": "منخفض", "Moderate": "متوسط", "High": "مرتفع"}
    st.success(f"Your risk level is: {risk}" if lang == "English" else f"مستوى الخطر لديك: {label[risk]}")

def oral_hygiene():
    st.title("Oral Hygiene Guide" if lang == "English" else "دليل العناية الفموية")
    st.image("https://www.cdc.gov/oralhealth/images/how-to-brush-300px.jpg", use_column_width=True)
    content_en = """- Brush twice daily with fluoride toothpaste  
- Floss once daily  
- Replace your toothbrush every 3 months  
- Clean your tongue and gums  
- Avoid rinsing immediately after brushing"""
    content_ar = """- فرّش مرتين يوميًا بمعجون يحتوي على الفلورايد  
- استخدم الخيط مرة يوميًا  
- استبدل فرشاتك كل 3 أشهر  
- نظف لسانك ولثتك  
- لا تشطف فمك مباشرة بعد التفريش"""
    st.markdown(content_en if lang == "English" else content_ar)

def prevention_plan():
    st.title("Your Prevention Plan" if lang == "English" else "خطة الوقاية الخاصة بك")
    age = st.slider("Select your age" if lang == "English" else "اختر عمرك", 5, 80, 25)
    brushing = st.radio("Brushing frequency?" if lang == "English" else "عدد مرات التفريش؟", ["Once", "Twice", "More than Twice"])
    sugar = st.radio("Do you snack on sugary foods?" if lang == "English" else "هل تتناول وجبات خفيفة سكرية؟", ["Yes", "No"])
    st.subheader("Your Plan" if lang == "English" else "خطة العناية")
    st.write("- Brush 2x daily with fluoride")
    if sugar == "Yes":
        st.write("- Reduce sugary snacks and rinse mouth after eating")
    if brushing == "Once":
        st.write("- Increase brushing to at least twice daily")

def case_scenarios():
    st.title("Case Scenario" if lang == "English" else "سيناريو واقعي")
    if lang == "English":
        q = st.radio("Ali is 16, brushes once a day, drinks soda at night. What should he do?", ["Nothing", "Drink water", "Brush twice + reduce soda"])
        st.success("Correct choice!" if q == "Brush twice + reduce soda" else "Think again.")
    else:
        q = st.radio("علي عمره ١٦ سنة، يفرّش مرة ويشرب صودا مساءً. ماذا عليه أن يفعل؟", ["لا شيء", "يشرب ماء", "يفرّش مرتين ويقلل الصودا"])
        st.success("إجابة صحيحة!" if q == "يفرّش مرتين ويقلل الصودا" else "أعد التفكير.")

def quiz():
    st.title("Caries Prevention Quiz" if lang == "English" else "اختبار الوقاية من التسوس")
    score = 0
    if st.radio("1. How often should you brush?", ["Once", "Twice", "After snacks"]) == "Twice":
        score += 1
    if st.radio("2. Is fluoride helpful?", ["Yes", "No"]) == "Yes":
        score += 1
    if st.radio("3. Can sugar cause cavities?", ["Yes", "No"]) == "Yes":
        score += 1
    if st.button("Submit"):
        st.success(f"Your score: {score}/3" if lang == "English" else f"نتيجتك: {score} من 3")

def faq():
    st.title("Frequently Asked Questions" if lang == "English" else "الأسئلة الشائعة")
    faqs = {
        "Do cavities heal on their own?": "No, they need dental treatment.",
        "How often should I visit the dentist?": "Every 6 months."
    }
    faqs_ar = {
        "هل يشفى التسوس من تلقاء نفسه؟": "لا، يجب علاجه من قبل طبيب الأسنان.",
        "كم مرة أزور طبيب الأسنان؟": "كل ٦ أشهر."
    }
    for q, a in (faqs if lang == "English" else faqs_ar).items():
        with st.expander(q):
            st.write(a)

def about():
    st.title("About NoCaries" if lang == "English" else "حول نوكاريس")
    st.markdown("Developed by a team of dental students to promote patient awareness and caries prevention." if lang == "English"
                else "تم تطويره بواسطة فريق من طلاب طب الأسنان لتعزيز الوعي الوقائي للمرضى.")

# --- ROUTING ---
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
