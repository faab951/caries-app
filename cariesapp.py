import streamlit as st

st.set_page_config(page_title="Caries Prevention App", layout="wide")

# Sidebar navigation
sections = [
    "Home",
    "What is Dental Caries?",
    "Causes of Caries",
    "How to Prevent Caries",
    "Brushing and Flossing Techniques",
    "Dietary Advice for Oral Health",
    "Myths About Dental Caries",
    "Caries Risk Calculator",
    "Frequently Asked Questions",
    "Chatbot"
]
choice = st.sidebar.radio("Navigate to", sections)

if choice == "Home":
    st.title("Welcome to the Caries Prevention Project")
    st.write(
        "This app is designed to educate patients about dental caries prevention "
        "and promote oral health awareness using interactive digital tools."
    )
    st.write("Use the sidebar to explore different sections and tools.")

elif choice == "What is Dental Caries?":
    st.header("What is Dental Caries?")
    st.write(
        "Dental caries, also known as tooth decay or cavities, is a chronic disease "
        "caused by bacterial acid attacking the enamel."
    )
    st.write("Untreated caries can lead to pain, infection, and tooth loss.")

elif choice == "Causes of Caries":
    st.header("Causes of Dental Caries")
    st.write("- **Bacteria**: Streptococcus mutans and others produce acid.")
    st.write("- **Diet**: High sugar and acid intake.")
    st.write("- **Poor Oral Hygiene**: Infrequent brushing and flossing.")
    st.write("- **Lack of Fluoride**: Fluoride strengthens enamel.")
    st.write("- **Dry Mouth**: Less saliva reduces natural protection.")

elif choice == "How to Prevent Caries":
    st.header("How to Prevent Dental Caries")
    st.write("1. Brush twice daily with fluoride toothpaste.")
    st.write("2. Floss or clean between your teeth daily.")
    st.write("3. Limit sugary and acidic food/drinks.")
    st.write("4. Visit your dentist regularly.")
    st.write("5. Use fluoride mouth rinses if recommended.")

elif choice == "Brushing and Flossing Techniques":
    st.header("Brushing and Flossing Techniques")
    st.subheader("Brushing")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/a/a7/Toothbrushing_1.jpg",
        caption="Proper Brushing Technique",
        use_column_width=True
    )
    st.write(
        "Use a soft-bristled toothbrush. Hold at a 45° angle and use gentle circular motions."
    )
    st.subheader("Flossing")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/2/2f/Flossing_1.jpg",
        caption="Proper Flossing Technique",
        use_column_width=True
    )
    st.write(
        "Use about 18 inches of floss, wrap it around your fingers, and gently slide between teeth."
    )

elif choice == "Dietary Advice for Oral Health":
    st.header("Dietary Advice for Oral Health")
    st.write("**Good Choices:**")
    st.write("- Vegetables, fruits, dairy products.")
    st.write("- Drink water instead of soda.")
    st.write("**Limit:**")
    st.write("- Sugary snacks and acidic foods.")
    st.write("- Frequent snacking between meals.")

elif choice == "Myths About Dental Caries":
    st.header("Myths vs Facts About Dental Caries")
    myths = {
        "Sugar-free soda is safe for teeth":
            "Fact: Even sugar-free sodas are acidic and can erode enamel.",
        "Brushing harder cleans better":
            "Fact: Brushing too hard can damage enamel and gums.",
        "Only kids get cavities":
            "Fact: Adults are also at risk for cavities.",
        "If I have no pain, I have no cavities":
            "Fact: Early cavities can be painless but still harmful."
    }
    myth_choice = st.selectbox("Select a myth:", list(myths.keys()))
    st.write(myths[myth_choice])

elif choice == "Caries Risk Calculator":
    st.header("Caries Risk Calculator")
    st.write("Estimate your caries risk:")
    sugar = st.slider("Sugary snacks/drinks per day?", 0, 10, 2)
    brushing = st.slider("Times brushing per day?", 0, 4, 2)
    fluoride = st.checkbox("Using fluoride toothpaste?")
    score = sugar * 2 - brushing * 2 - (2 if fluoride else 0)
    if score < 0:
        risk = "Low"
    elif score <= 5:
        risk = "Moderate"
    else:
        risk = "High"
    st.success(f"Your estimated caries risk is: **{risk}** (Score: {score})")

elif choice == "Frequently Asked Questions":
    st.header("Frequently Asked Questions")
    faqs = {
        "How often should I visit the dentist?":
            "Twice a year for check-ups and cleanings.",
        "Is fluoride safe?":
            "Yes. Fluoride is safe and protects teeth.",
        "Can cavities reverse?":
            "Early stages can remineralize with proper care.",
        "Which toothbrush is best?":
            "Soft-bristled toothbrush with a small head."
    }
    for question, answer in faqs.items():
        with st.expander(question):
            st.write(answer)

elif choice == "Chatbot":
    st.header("Dental Care Chatbot")
    bot_mode = st.radio("Choose chatbot mode:", ["Simple Chatbot", "OpenAI GPT Chatbot"])
    user_input = st.text_input("Ask me a question:")

    if bot_mode == "Simple Chatbot":
        responses = {
            "what is caries": "Dental caries is tooth decay caused by bacterial acid attacking enamel.",
            "how to prevent caries": "Brush twice daily, floss daily, limit sugars, and use fluoride.",
            "what causes caries": "Frequent sugar intake, bacteria, and poor oral hygiene."
        }
        if user_input:
            key = user_input.lower()
            answer = responses.get(key, "Sorry, I don't know that. Try asking another question.")
            st.write(answer)

    else:
        api_key = st.text_input("Enter your OpenAI API key:", type="password")
        if not api_key:
            st.warning("You need to enter your OpenAI API key to use GPT chatbot.")
        elif user_input:
            try:
                import openai
                openai.api_key = api_key
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_input}]
                )
                st.write(response.choices[0].message.content)
            except ModuleNotFoundError:
                st.error("OpenAI module is not installed. Please run: pip install openai")
            except Exception as e:
                st.error(f"An error occurred: {e}")
