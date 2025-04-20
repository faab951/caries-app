
import streamlit as st

# --- Language Toggle ---
lang = st.sidebar.radio("Language / اللغة", ["English", "Arabic"])

# --- Page Config ---
st.set_page_config(page_title="NoCaries", layout="wide")

# --- Custom CSS for luxury style ---
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
    .stRadio > div {
        background-color: #f0f0f0;
        padding: 0.5em;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- Page Navigation ---
page = st.sidebar.selectbox("Navigate", [
    "🏠 Home",
    "📚 What is Caries?",
    "❌ Myth Busters",
    "🧮 Risk Calculator",
    "🪥 Oral Hygiene Guide",
    "📅 Build My Prevention Plan",
    "💬 Case Scenarios",
    "🧠 Quiz",
    "❓ FAQ",
    "👥 About"
])

# --- Language content blocks ---
def english_home():
    st.title("NoCaries: Cavity Prevention for Lifelong Oral Health")
    st.markdown("""
    Welcome to **NoCaries**, a digital oral health platform designed to educate and empower patients and families on cavity prevention through interaction, visuals, and customized learning tools.
    """)
    st.subheader("Explore the sections using the sidebar:")
    st.markdown("- Learn what causes dental caries and how it progresses")
    st.markdown("- Bust myths and misconceptions")
    st.markdown("- Calculate your personal caries risk")
    st.markdown("- Learn effective brushing and flossing techniques")
    st.markdown("- Generate your own prevention plan")
    st.markdown("- Solve real-life cases and test your knowledge")
    st.markdown("- Get answers to frequently asked questions")

def arabic_home():
    st.title("نوكاريس: الوقاية من التسوس لصحة فموية تدوم")
    st.markdown("""
    مرحبًا بكم في **نوكاريس**، منصة صحية رقمية تهدف إلى تثقيف وتمكين المرضى والعائلات حول الوقاية من التسوس من خلال التفاعل، والصور التوضيحية، وأدوات التعلم المخصصة.
    """)
    st.subheader("استكشف الأقسام من خلال الشريط الجانبي:")
    st.markdown("- تعرف على أسباب التسوس وكيفية تطوره")
    st.markdown("- كشف الخرافات والتصورات الخاطئة")
    st.markdown("- احسب خطر إصابتك بالتسوس")
    st.markdown("- تعلم تقنيات التفريش والتنظيف بالخيط")
    st.markdown("- أنشئ خطة وقاية شخصية")
    st.markdown("- حل حالات واقعية واختبر معلوماتك")
    st.markdown("- احصل على إجابات لأسئلة شائعة")

# Placeholder pages
def page_placeholder(title_en, title_ar):
    st.title(title_en if lang == "English" else title_ar)
    st.info("🚧 This section is under development and will include full content, visuals, and interactivity.")

# --- Page Router ---
if page == "🏠 Home":
    english_home() if lang == "English" else arabic_home()
elif page == "📚 What is Caries?":
    page_placeholder("What is Dental Caries?", "ما هو تسوس الأسنان؟")
elif page == "❌ Myth Busters":
    page_placeholder("Caries Myth Busters", "كشف خرافات التسوس")
elif page == "🧮 Risk Calculator":
    page_placeholder("Caries Risk Calculator", "حاسبة خطر التسوس")
elif page == "🪥 Oral Hygiene Guide":
    page_placeholder("Oral Hygiene Instructions", "دليل العناية اليومية")
elif page == "📅 Build My Prevention Plan":
    page_placeholder("Build My Oral Health Plan", "أنشئ خطة العناية الفموية")
elif page == "💬 Case Scenarios":
    page_placeholder("Clinical Case Scenarios", "سيناريوهات سريرية")
elif page == "🧠 Quiz":
    page_placeholder("Caries Prevention Quiz", "اختبار الوقاية من التسوس")
elif page == "❓ FAQ":
    page_placeholder("Frequently Asked Questions", "الأسئلة الشائعة")
elif page == "👥 About":
    st.title("About NoCaries" if lang == "English" else "حول نوكاريس")
    st.markdown("""
    **NoCaries** is a student-led project created to raise awareness and provide interactive, accessible education on cavity prevention.

    Developed as part of a university patient education initiative.

    **Team Members:**  
    - Abdullah Al-Razhi  
    - Mohammed Al-Sharif  
    - Sadakah Basyouni  
    - Mohammed Al-Shammrani
    - Maan Al-Ghamdi
    """)
