import streamlit as st
import openai

# Requirements: pip install streamlit openai

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
        "characterized by demineralization of the tooth surface due to acid-producing bacteria."
    )
    st.write("Untreated caries can lead to pain, infection, and tooth loss.")

elif choice == "Causes of Caries":
    st.header("Causes of Dental Caries")
    st.write("- **Bacteria**: Streptococcus mutans and other acid-producing bacteria.")
    st.write("- **Diet**: Frequent consumption of sugary and acidic foods and drinks.")
    st.write("- **Poor Oral Hygiene**: Inadequate brushing and flossing.")
    st.write("- **Lack of Fluoride**: Fluoride helps to remineralize tooth enamel.")
    st.write("- **Dry Mouth**: Reduced saliva flow decreases natural remineralization.")

elif choice == "How to Prevent Caries":
    st.header("How to Prevent Dental Caries")
    st.write("1. Brush twice daily with fluoride toothpaste.")
    st.write("2. Floss or use interdental cleaners daily.")
    st.write("3. Reduce intake of sugary and acidic foods and drinks.")
    st.write("4. Visit your dentist regularly for check-ups and cleanings.")
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
    st.write("**Do:**")
    st.write("- Eat plenty of vegetables, fruits, and dairy products.")
    st.write("- Drink water throughout the day.")
    st.write("**Limit:**")
    st.write("- Sugary snacks and beverages.")
    st.write("- Acidic foods like citrus fruits and soda.")
    st.write("- Frequent snacking between meals.")

elif choice == "Myths About Dental Caries":
    st.header("Myths vs Facts About Dental Caries")
    myths = {
        "Sugar-free soda is safe for teeth":
            "Fact: Sugar-free sodas are acidic and can still erode enamel.",
        "Brushing harder cleans better":
            "Fact: Brushing too hard can damage enamel and gums.",
        "Only kids get cavities":
            "Fact: Adults are also susceptible to cavities throughout life.",
        "If I have no pain, I have no cavities":
            "Fact: Cavities can exist without pain until advanced stages."
    }
    myth_choice = st.selectbox("Select a myth:", list(myths.keys()))
    st.write(myths[myth_choice])

elif choice == "Caries Risk Calculator":
    st.header("Caries Risk Calculator")
    st.write("Answer the following to estimate your caries risk:")
    sugar = st.slider("Sugary snacks/drinks per day?", 0, 10, 3)
    brushing = st.slider("Brushings per day?", 0, 4, 2)
    fluoride = st.checkbox("Use fluoride toothpaste?")
    score = sugar * 2 - brushing * 2 - (2 if fluoride else 0)
    if score < 0:
        risk = "Low"
    elif score <= 5:
        risk = "Moderate"
    else:
        risk = "High"
    st.write(f"Your estimated caries risk is: **{risk}** (Score: {score})")

elif choice == "Frequently Asked Questions":
    st.header("Frequently Asked Questions")
    faqs = {
        "How often should I visit the dentist?":
            "At least twice a year for check-ups and cleanings.",
        "Is fluoride safe?":
            "Yes, when used correctly, fluoride strengthens enamel and helps prevent decay.",
        "Can I reverse early cavities?":
            "Early lesions can remineralize with good oral hygiene and fluoride.",
        "What toothbrush should I use?":
            "A soft-bristled brush with a small head is recommended."
    }
    for question, answer in faqs.items():
        with st.expander(question):
            st.write(answer)

elif choice == "Chatbot":
    st.header("Dental Care Chatbot")
    bot_mode = st.radio("Choose chatbot mode:", [
        "Simple Chatbot",
        "OpenAI GPT Chatbot"
    ])
    user_input = st.text_input("Your question:")
    if bot_mode == "Simple Chatbot":
        responses = {
            "what is caries":
                "Dental caries is tooth decay caused by bacterial acid demineralizing the enamel.",
            "how to prevent caries":
                "Brush twice a day, floss daily, reduce sugar intake, and use fluoride.",
            "what causes caries":
                "Frequent sugar, poor oral hygiene, and acid-producing bacteria."
        }
        if user_input:
            key = user_input.lower()
            answer = responses.get(
                key,
                "Sorry, I don't know the answer. Try another question."
            )
            st.write(answer)

    else:
        api_key = st.text_input("Enter your OpenAI API key:", type="password")
        if not api_key:
            st.warning("Please enter your OpenAI API key to use this chatbot.")
        elif user_input:
            openai.api_key = api_key
            try:
                completion = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_input}]
                )
                reply = completion.choices[0].message.content
                st.write(reply)
            except Exception as e:
                st.error(f"Error: {e}")
