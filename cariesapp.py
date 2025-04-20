
import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="NoCaries", layout="wide")

# --- CUSTOM STYLE ---
st.markdown("""<style>
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
    background-color: #fffaf0;
    color: #333333;
    font-size: 18px;
}
h1, h2 {
    color: #2c3e50;
    font-weight: 600;
}
.section {
    background-color: #f7f0e9;
    padding: 1em;
    border-radius: 10px;
    margin-bottom: 1.5em;
}
.stButton>button {
    background-color: #bfa980;
    color: white;
    border-radius: 8px;
    padding: 0.6em 1.2em;
    font-size: 1em;
}
""", unsafe_allow_html=True)

# --- LANGUAGE TOGGLE ---
lang = st.sidebar.radio("Language / اللغة", ["English", "Arabic"])

# --- NAVIGATION ---
pages = ["Home", "What is Caries?", "Myth Busters", "Risk Calculator",
         "Oral Hygiene Guide", "Prevention Plan", "Case Scenarios",
         "Quiz", "FAQ", "About"]
page = st.sidebar.selectbox("Navigate", pages)

# --- SECTION FUNCTIONS ---

def home():
    title = "NoCaries: Your Guide to Cavity Prevention" if lang=="English" else "نوكاريس: دليلك للوقاية من التسوس"
    welcome = ("Explore interactive tools to learn about dental caries, assess your risk, and build a personalized prevention plan."
               if lang=="English" else
               "استكشف أدوات تفاعلية لتتعرف على تسوس الأسنان، قيّم خطر الإصابة، وأنشئ خطة وقاية مخصصة.")
    st.markdown(f"<div class='section'><h1>{title}</h1><p>{welcome}</p></div>", unsafe_allow_html=True)

def what_is_caries():
    header = "What is Dental Caries?" if lang=="English" else "ما هو تسوس الأسنان؟"
    st.markdown(f"<div class='section'><h2>{header}</h2></div>", unsafe_allow_html=True)
    stages_en = {
        "White Spot": ("https://i.imgur.com/1hH4m5r.png", "Early demineralization appears as a white spot."),
        "Enamel Decay": ("https://i.imgur.com/9Pz8ZgM.png", "Enamel surface breaks down into tiny pits."),
        "Dentin Involvement": ("https://i.imgur.com/7y5ZK2O.png", "Decay reaches softer dentin, progression speeds."),
        "Pulp Exposure": ("https://i.imgur.com/4bXj6fQ.png", "Infection reaches pulp, causing pain."),
        "Abscess": ("https://i.imgur.com/DqW8K4u.png", "Pus formation around root; needs urgent care.")
    }
    stages_ar = {
        "بقعة بيضاء": ("https://i.imgur.com/1hH4m5r.png", "بداية إزالة المعادن تظهر على شكل بقعة بيضاء."),
        "تسوس المينا": ("https://i.imgur.com/9Pz8ZgM.png", "ينهار سطح المينا ويظهر حفر صغيرة."),
        "وصول إلى العاج": ("https://i.imgur.com/7y5ZK2O.png", "يصل التسوس إلى العاج الأكثر ليونة."),
        "تعرض اللب": ("https://i.imgur.com/4bXj6fQ.png", "يصل التسوس إلى اللب مسببًا الألم."),
        "خراج": ("https://i.imgur.com/DqW8K4u.png", "تكوّن صديد حول الجذر؛ يتطلب علاجًا عاجلًا.")
    }
    data = stages_en if lang=="English" else stages_ar
    choice = st.selectbox("Select a stage:" if lang=="English" else "اختر مرحلة:", [""] + list(data.keys()))
    if choice:
        img, desc = data[choice]
        st.image(img, use_container_width=True)
        st.write(desc)

def myth_busters():
    header = "Myth Busters" if lang=="English" else "كشف الخرافات"
    st.markdown(f"<div class='section'><h2>{header}</h2></div>", unsafe_allow_html=True)
    myths = [
        ("Only sweets cause cavities", "While sugar contributes, any fermentable carbs feed bacteria."),
        ("Brush harder to remove plaque", "Gentle brushing with proper technique is superior."),
        ("Natural toothpaste suffices", "Fluoride toothpaste is clinically proven to strengthen enamel.")
    ]
    myths_ar = [
        ("فقط الحلويات تسبب التسوس", "بينما يساهم السكر، أي كربوهيدرات قابلة للتخمر تغذي البكتيريا."),
        ("التفريش بقوة يزيل البلاك", "التفريش اللطيف مع التقنية الصحيحة أفضل."),
        ("المعجون الطبيعي كافٍ", "معجون الفلورايد مثبت سريريًا في تقوية المينا.")
    ]
    data = myths if lang=="English" else myths_ar
    for myth, truth in data:
        with st.expander(myth):
            st.write(truth)

def risk_calculator():
    header = "Caries Risk Calculator" if lang=="English" else "حاسبة خطر التسوس"
    st.markdown(f"<div class='section'><h2>{header}</h2></div>", unsafe_allow_html=True)
    sugar = st.selectbox("Sugary snacks frequency:" if lang=="English" else "تكرار تناول السكريات:", ["", "Never", "Occasionally", "Daily"])
    brushing = st.selectbox("Brushing frequency:" if lang=="English" else "تكرار التفريش:", ["", "Once daily", "Twice daily", "More"])
    flossing = st.selectbox("Flossing:" if lang=="English" else "استخدام الخيط:", ["", "Never", "Sometimes", "Daily"])
    if sugar and brushing and flossing:
        score = ["Never","Occasionally","Daily"].index(sugar) + ["Once daily","Twice daily","More"].index(brushing) + ["Never","Sometimes","Daily"].index(flossing)
        if score <= 2:
            level, reason = ("Low", "Good habits lower risk.") if lang=="English" else ("منخفض", "عادات جيدة تقلل الخطر.")
        elif score <= 4:
            level, reason = ("Moderate", "Some improvements needed.") if lang=="English" else ("متوسط", "يحتاج إلى بعض التحسين.")
        else:
            level, reason = ("High", "Significant changes advised.") if lang=="English" else ("مرتفع", "ينصح بإجراء تغييرات كبيرة.")
        st.success(f"Risk Level: {level}\n{reason}")

def oral_hygiene_guide():
    header = "Oral Hygiene Guide" if lang=="English" else "دليل العناية الفموية"
    st.markdown(f"<div class='section'><h2>{header}</h2></div>", unsafe_allow_html=True)
    tips_en = [
        ("Brushing Technique", "Use a soft brush at 45° angle for 2 minutes.", "https://i.imgur.com/7y5ZK2O.png"),
        ("Flossing", "Curve floss in C-shape around each tooth daily.", "https://i.imgur.com/tKX87Jb.png"),
        ("Tongue Cleaning", "Gently scrape tongue to remove bacteria.", "https://i.imgur.com/DqW8K4u.png"),
        ("Mouthwash", "Use fluoride rinse once daily.", "https://i.imgur.com/9Pz8ZgM.png")
    ]
    tips_ar = [
        ("تقنية التفريش", "استخدم فرشاة ناعمة بزاوية 45° لمدة دقيقتين.", "https://i.imgur.com/7y5ZK2O.png"),
        ("استخدام الخيط", "لف الخيط على شكل C حول كل سن يوميًا.", "https://i.imgur.com/tKX87Jb.png"),
        ("تنظيف اللسان", "اكشط اللسان برفق لإزالة البكتيريا.", "https://i.imgur.com/DqW8K4u.png"),
        ("المضمضة", "استخدم غسول فلورايد مرة يوميًا.", "https://i.imgur.com/9Pz8ZgM.png")
    ]
    tips = tips_en if lang=="English" else tips_ar
    cols = st.columns(2)
    for i, (title, desc, img) in enumerate(tips):
        with cols[i%2]:
            st.image(img, use_container_width=True)
            st.markdown(f"**{title}**\n{desc}")

def prevention_plan():
    header = "Prevention Plan Builder" if lang=="English" else "منشئ خطة الوقاية"
    st.markdown(f"<div class='section'><h2>{header}</h2></div>", unsafe_allow_html=True)
    age = st.slider("Age" if lang=="English" else "العمر", 5, 80, 30)
    goal = st.selectbox("Your goal:" if lang=="English" else "هدفك:", 
                        ["Improve hygiene","Maintain health","Reduce cavities"] 
                        if lang=="English" else ["تحسين التنظيف","الحفاظ على الصحة","تقليل التسوس"])
    st.subheader("Daily Routine" if lang=="English" else "روتين يومي")
    st.write("- Morning: Brush 2 mins + rinse")
    st.write("- Midday: Floss + healthy snack")
    st.write("- Night: Brush + mouthwash")

def case_scenarios():
    header = "Case Scenarios" if lang=="English" else "سيناريوهات واقعية"
    st.markdown(f"<div class='section'><h2>{header}</h2></div>", unsafe_allow_html=True)
    data_en = [
        ("Sensitive to cold?","Cavity","Enamel crack","Receding gum","Cavity"),
        ("Dark spots on molars?","Fluoride","Ignore","Soda rinse","Fluoride"),
        ("Child refuses brushing?","Fun timer","Force","None","Fun timer"),
        ("Dry mouth often?","Water","Sugar","Ignore","Water"),
        ("Bleeding gums after floss?","Gentle floss","Stop floss","Brush harder","Gentle floss")
    ]
    data_ar = [
        ("حساسية للبرد؟","تسوس","تشقق المينا","تراجع اللثة","تسوس"),
        ("بقع داكنة على الأضراس؟","فلورايد","تجاهل","مضمضة صودا","فلورايد"),
        ("الطفل يرفض التفريش؟","مؤقت مرح","إجبار","لا شيء","مؤقت مرح"),
        ("جفاف الفم؟","ماء","سكر","تجاهل","ماء"),
        ("نزيف بعد الخيط؟","خيط بلطف","توقف","افرك بقوة","خيط بلطف")
    ]
    data = data_en if lang=="English" else data_ar
    for i, item in enumerate(data):
        q, opt1, opt2, opt3, ans = item
        choice = st.selectbox(q, ["", opt1, opt2, opt3], key=f"case{i}")
        if choice:
            st.write("✅ Correct" if choice==ans else f"❌ Answer: {ans}")

def quiz():
    header = "Quiz" if lang=="English" else "اختبار"
    st.markdown(f"<div class='section'><h2>{header}</h2></div>", unsafe_allow_html=True)
    qlist_en = [
        ("Ideal brushing time?",["1 min","2 mins","30 sec"],"2 mins"),
        ("Floss once?",["Weekly","Daily","Never"],"Daily"),
        ("Sugar causes?",["Yes","No"],"Yes"),
        ("Toothbrush type?",["Soft","Hard","Metal"],"Soft"),
        ("Use mouthwash?",["Yes","No"],"Yes"),
        ("Sealants help?",["Yes","No"],"Yes")
    ]
    qlist_ar = [
        ("مدة التفريش؟",["1 دقيقة","2 دقائق","30 ث"],"2 دقائق"),
        ("استخدام الخيط؟",["أسبوعيًا","يوميًا","أبدًا"],"يوميًا"),
        ("هل يسبب السكر؟",["نعم","لا"],"نعم"),
        ("نوع الفرشاة؟",["ناعمة","صلبة","معدنية"],"ناعمة"),
        ("استخدام المضمضة؟",["نعم","لا"],"نعم"),
        ("هل تساعد الختمات؟",["نعم","لا"],"نعم")
    ]
    qlist = qlist_en if lang=="English" else qlist_ar
    score = 0
    for idx, (q, opts, ans) in enumerate(qlist):
        choice = st.selectbox(q, [""]+opts, key=f"quiz{idx}")
        if choice and choice==ans:
            score += 1
    if st.button("Submit"):
        st.success(f"Your score: {score} / {len(qlist)}" if lang=="English" else f"النتيجة: {score} من {len(qlist)}")

def faq():
    header = "FAQ" if lang=="English" else "الأسئلة الشائعة"
    st.markdown(f"<div class='section'><h2>{header}</h2></div>", unsafe_allow_html=True)
    faqs_en = {
        "Can early cavities reverse?":"With fluoride and care, early lesions can remineralize.",
        "Should I avoid all sugar?":"Limit frequency; moderation is key.",
        "Best toothbrush?":"Soft bristles protect enamel and gums.",
        "Are sealants effective?":"Yes, especially for molars in children.",
        "Is mouthwash necessary?":"Helpful, but not a substitute for brushing.",
        "Dentist visits?":"Every 6 months recommended.",
        "Dry mouth risk?":"Increases decay; stay hydrated.",
        "Sugar-free gum?":"Chewing can stimulate saliva.",
        "Bleeding gums?":"Seek dental advice if persistent.",
        "Children brushing?":"Supervise until age 8."
    }
    faqs_ar = {
        "هل يشفى التسوس المبكر؟":"يمكن إعادة تمعدن البقع المبكرة بالفلورايد والعناية.",
        "هل أتجنب كل السكر؟":"قلل التكرار؛ الاعتدال مهم.",
        "أفضل فرشاة؟":"النعومة تحمي المينا واللثة.",
        "هل الختمات فعالة؟":"نعم، خاصة للأطفال.",
        "هل المضمضة ضرورية؟":"مفيدة وليست بديلاً للتفريش.",
        "زيارة الطبيب؟":"يوصى كل 6 أشهر.",
        "جفاف الفم؟":"يزيد التسوس؛ اشرب الماء.",
        "العلكة بدون سكر؟":"تحفيز اللعاب مفيد.",
        "نزيف اللثة؟":"راجع طبيب الأسنان إذا استمر.",
        "تفريش الأطفال؟":"اشرف حتى سن 8."
    }
    data = faqs_en if lang=="English" else faqs_ar
    for q, ans in data.items():
        with st.expander(q):
            st.write(ans)

def about():
    header = "About" if lang=="English" else "حول"
    st.markdown(f"<div class='section'><h2>{header}</h2></div>", unsafe_allow_html=True)
    if lang=="English":
        st.markdown('''**NoCaries** developed by dental students:
- Student A: Community Outreach
- Student B: Clinical Content
- Student C: UX & Design
- Student D: Data & Interactivity
        ''')
    else:
        st.markdown('''**نوكاريس** تم تطويره بواسطة طلاب طب الأسنان:
- الطالب أ: التوعية المجتمعية
- الطالب ب: المحتوى السريري
- الطالب ج: تجربة المستخدم والتصميم
- الطالب د: البيانات والتفاعلية
        ''')

# --- ROUTING ---
if page=="Home": home()
elif page=="What is Caries?": what_is_caries()
elif page=="Myth Busters": myth_busters()
elif page=="Risk Calculator": risk_calculator()
elif page=="Oral Hygiene Guide": oral_hygiene_guide()
elif page=="Prevention Plan": prevention_plan()
elif page=="Case Scenarios": case_scenarios()
elif page=="Quiz": quiz()
elif page=="FAQ": faq()
elif page=="About": about()
