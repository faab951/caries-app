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
    st.title("Welcome to the Caries Prevention Digital Tool")
    st.write(
        "Welcome! This app aims to increase patient education and awareness about dental caries prevention. "
        "By using this interactive tool, patients can learn about oral health in an engaging and accessible way."
    )
    st.write(
        "Use the sidebar to explore educational content, risk calculators, brushing guides, and even chat with a virtual assistant!"
    )

elif choice == "What is Dental Caries?":
    st.header("What is Dental Caries?")
    st.write(
        "Dental caries, commonly known as cavities, is a disease where tooth structure is damaged by acids produced "
        "by bacteria in the mouth. The acids dissolve the minerals in the enamel, leading to holes or structural breakdown."
    )
    st.subheader("Stages of Dental Caries")
    st.write(
        "1. **Demineralization**: White spots appear as minerals are lost.\n"
        "2. **Enamel Decay**: Surface breaks and cavities form.\n"
        "3. **Dentin Decay**: Bacteria reach deeper layers of the tooth.\n"
        "4. **Pulp Damage**: Infection and inflammation of the tooth nerve.\n"
        "5. **Abscess Formation**: Spread of infection causing severe pain and swelling."
    )

elif choice == "Causes of Caries":
    st.header("Causes of Dental Caries")
    st.write(
        "**Dental caries is a multi-factorial disease** that results from a combination of factors:"
    )
    st.markdown("""
    - **Bacteria**: Especially _Streptococcus mutans_ and _Lactobacilli_.
    - **Sugary Diet**: Sugar fuels acid production by bacteria.
    - **Poor Oral Hygiene**: Plaque buildup remains undisturbed.
    - **Reduced Saliva Flow**: Saliva helps neutralize acids.
    - **Deep Pits and Fissures**: Difficult to clean areas in molars.
    """)

elif choice == "How to Prevent Caries":
    st.header("How to Prevent Dental Caries")
    st.write(
        "**Prevention is better than cure!** Follow these steps to keep your teeth healthy:"
    )
    st.markdown("""
    - Brush twice daily for two minutes using fluoride toothpaste.
    - Floss daily to clean between teeth.
    - Use fluoride treatments or mouth rinses if recommended.
    - Reduce intake of sugary and acidic food/drinks.
    - Drink plenty of water, especially fluoridated water.
    - Visit the dentist every 6 months for professional cleaning and early detection.
    - Consider dental sealants for children to protect molars.
    """)

elif choice == "Brushing and Flossing Techniques":
    st.header("Brushing and Flossing Techniques")
    st.subheader("Brushing Technique (Bass Method)")
    st.write(
        "Place the toothbrush at a 45-degree angle to the gums. Move the brush back and forth gently in short strokes. "
        "Brush the outer surfaces, the inner surfaces, and the chewing surfaces of the teeth. "
        "For the inside surfaces of the front teeth, tilt the brush vertically and make several up-and-down strokes."
    )
    st.subheader("Flossing Technique")
    st.write(
        "Break off about 18 inches of floss and wind most of it around each middle finger, leaving about an inch to work with. "
        "Gently slide it between the teeth, curve the floss into a C-shape against the side of the tooth, and rub it up and down."
    )

elif choice == "Dietary Advice for Oral Health":
    st.header("Dietary Advice for Oral Health")
    st.write(
        "Your diet plays a major role in your oral health. Making the right food choices helps prevent cavities and gum disease."
    )
    st.subheader("Recommended Foods")
    st.markdown("""
    - Fresh fruits and vegetables
    - Dairy products like cheese and yogurt
    - Whole grains
    - Water (especially fluoridated water)
    """)
    st.subheader("Foods to Limit")
    st.markdown("""
    - Candy, cakes, and pastries
    - Sugary beverages (sodas, energy drinks)
    - Acidic fruits and juices (consumed in excess)
    - Sticky foods like caramel and dried fruits
    """)

elif choice == "Myths About Dental Caries":
    st.header("Myths vs Facts About Dental Caries")
    myths = {
        "If my teeth don’t hurt, I don’t have cavities":
            "Fact: Many cavities are painless until they are severe.",
        "Only children get cavities":
            "Fact: Adults are also at high risk for caries.",
        "Sugar is the only cause of cavities":
            "Fact: Acid-producing bacteria, poor hygiene, and dry mouth are also critical factors.",
        "Brushing alone is enough to prevent cavities":
            "Fact: Flossing, diet, and regular dental visits are equally important."
    }
    myth_choice = st.selectbox("Select a myth to reveal the truth:", list(myths.keys()))
    st.success(myths[myth_choice])

elif choice == "Caries Risk Calculator":
    st.header("Caries Risk Calculator")
    st.write(
        "Answer a few questions to estimate your risk of developing dental caries:"
    )
    sugar = st.slider("How many sugary snacks or drinks do you consume daily?", 0, 10, 2)
    brushing = st.slider("How many times do you brush per day?", 0, 4, 2)
    flossing = st.slider("How many times do you floss per week?", 0, 14, 3)
    fluoride = st.checkbox("Do you use fluoride toothpaste?")
    dry_mouth = st.checkbox("Do you suffer from dry mouth frequently?")
    
    score = (sugar * 2) - (brushing * 2) - (flossing // 2) - (3 if fluoride else 0) + (3 if dry_mouth else 0)
    if score <= 0:
        risk = "Low Risk"
    elif score <= 5:
        risk = "Moderate Risk"
    else:
        risk = "High Risk"

    st.success(f"Your estimated caries risk: **{risk}** (Score: {score})")

elif choice == "Frequently Asked Questions":
    st.header("Frequently Asked Questions")
    faqs = {
        "How often should I get a dental check-up?":
            "Twice per year is recommended, but more frequent visits may be necessary if you have specific conditions.",
        "What toothpaste should I use?":
            "Use a fluoride toothpaste. Ask your dentist if a prescription-strength fluoride paste is needed.",
        "Can cavities heal by themselves?":
            "Early-stage mineral loss (white spots) can sometimes be reversed. Cavities that have formed require professional treatment.",
        "How does fluoride help teeth?":
            "Fluoride remineralizes enamel, making it more resistant to acid attacks."
    }
    for question, answer in faqs.items():
        with st.expander(question):
            st.write(answer)

elif choice == "Chatbot":
    st.header("Dental Care Chatbot")
    bot_mode = st.radio("Choose Chatbot Mode", ["Simple Chatbot", "OpenAI GPT Chatbot"])
    user_input = st.text_input("Ask your dental question:")

    if bot_mode == "Simple Chatbot":
        responses = {
            "what is caries":
                "Dental caries is decay of the teeth caused by bacterial acids breaking down the enamel.",
            "how to prevent caries":
                "Brush and floss daily, use fluoride, and reduce sugar intake.",
            "causes of caries":
                "Caries is caused by bacteria, sugar intake, poor oral hygiene, and dry mouth."
        }
        if user_input:
            key = user_input.lower().strip()
            answer = responses.get(
                key, "Sorry, I don't know the answer to that. Try asking about caries prevention or causes!"
            )
            st.info(answer)

    else:
        api_key = st.text_input("Enter your OpenAI API key:", type="password")
        if not api_key:
            st.warning("Please enter your OpenAI API key to use the GPT chatbot.")
        elif user_input:
            try:
                import openai
                openai.api_key = api_key
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": user_input}]
                )
                st.success(response.choices[0].message.content)
            except ModuleNotFoundError:
                st.error("OpenAI module not installed. Run: pip install openai")
            except Exception as e:
                st.error(f"An error occurred: {e}")
