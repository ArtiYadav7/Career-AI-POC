import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json



load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")



st.set_page_config(
    page_title="AI Career Transformation POC",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Career Transformation POC")

st.write(
    "Generate identity transformation cards and motivational narration using AI."
)



test_users = [

    {
        "icp_type": "high_wage",
        "name": "Neha Kulkarni",
        "current_role": "Final year IT student",
        "target_role": "Cloud Engineer",
        "urgency_months": 6,
        "skills": ["Python basics", "Linux", "Networking"],
        "language": "en",

        "vision_profile": {
            "current_life": "Preparing for placements without practical cloud experience",
            "main_blocker": "No real-world cloud projects",
            "vision_12mo": "Working in a cloud team at a tech company",
            "top_motivation": "Want financial independence and career growth"
        }
    },

    {
        "icp_type": "low_wage",
        "name": "Mahesh Pawar",
        "current_role": "Warehouse helper",
        "target_role": "Computer operator",
        "urgency_months": 4,
        "skills": ["Basic smartphone usage", "Basic typing"],
        "language": "hi",

        "vision_profile": {
            "current_life": "Long physical work hours with unstable income",
            "main_blocker": "Limited computer knowledge",
            "vision_12mo": "Stable office-based computer job",
            "top_motivation": "Better future for family"
        }
    }
]



st.subheader("User Input")

input_mode = st.radio(
    "Choose Input Mode",
    ["Test User", "Manual Entry"]
)



if input_mode == "Test User":

    selected_name = st.selectbox(
        "Select Test User",
        [user["name"] for user in test_users]
    )

    selected_user = next(
        user for user in test_users
        if user["name"] == selected_name
    )



else:

    icp_type = st.selectbox(
        "ICP Type",
        ["high_wage", "low_wage"]
    )

    name = st.text_input("Name")

    current_role = st.text_input("Current Role")

    target_role = st.text_input("Target Role")

    urgency_months = st.number_input(
        "Urgency (Months)",
        min_value=1,
        max_value=24,
        value=6
    )

    skills = st.text_input(
        "Skills (comma separated)"
    )

    language = st.selectbox(
        "Language",
        ["en", "hi"]
    )

    current_life = st.text_area(
        "Current Situation"
    )

    main_blocker = st.text_area(
        "Main Blocker"
    )

    vision_12mo = st.text_area(
        "12 Month Vision"
    )

    top_motivation = st.text_area(
        "Top Motivation"
    )

    selected_user = {
        "icp_type": icp_type,
        "name": name,
        "current_role": current_role,
        "target_role": target_role,
        "urgency_months": urgency_months,
        "skills": [skill.strip() for skill in skills.split(",")],
        "language": language,

        "vision_profile": {
            "current_life": current_life,
            "main_blocker": main_blocker,
            "vision_12mo": vision_12mo,
            "top_motivation": top_motivation
        }
    }



def generate_career_output(user_data):

    prompt = f"""
    You are an AI career transformation assistant.

    Generate:
    1. Four identity cards
    2. One voice narration script

    IMPORTANT RULES:
    - Output ONLY valid JSON
    - No markdown
    - No explanations
    - Narration MUST be between 60-70 words
    - Keep narration concise,simple, grounded and voiceover-style
    - Tone should feel emotional, realistic, and motivational
    - Avoid overly dramatic phrases or cinematic language
    - Clearly mention current situation (education/background and present career or emotional state)
    - Honestly mention current skill or career gap using simple, supportive, non-harsh language
    - Language must match user preference
    - Use simple, everyday English; avoid metaphors or cinematic phrases
    - For Hindi users, generate simple natural Hindi
    - Must end with a clear, single actionable next step (what to do now)
    - Descriptions should be 25-40 words
    - DO NOT add extra fields
    - ONLY use the exact JSON schema provided

    Use exact timeline values:
    - today
    - 3 months
    - 6 months
    - 12 months

    IMPORTANT:
    - proof_point should ONLY exist for:
      - today
      - 3 months

    - proof_point must be null for:
      - 6 months
      - 12 months

    - proof_point field must always be present (never omit the key)

    Required JSON structure:

    {{
      "identity_cards": [
        {{
          "timeline": "today",
          "title": "",
          "description": "",
          "proof_point": ""
        }},
        {{
          "timeline": "3 months",
          "title": "",
          "description": "",
          "proof_point": ""
        }},
        {{
          "timeline": "6 months",
          "title": "",
          "description": "",
          "proof_point": null
        }},
        {{
          "timeline": "12 months",
          "title": "",
          "description": "",
          "proof_point": null
        }}
      ],
      "narration_script": ""
    }}

    User Data:
    {json.dumps(user_data, ensure_ascii=False)}
    """

    try:

       response = model.generate_content(prompt)

       parsed_output = json.loads(response.text)

       return parsed_output

    except Exception as e:

      return {
        "error": str(e)
    }



if st.button("Generate Career Transformation"):

    with st.spinner("Generating AI Output..."):

        try:

            result = generate_career_output(selected_user)
            if "error" in result:
                st.error(f"API Error: {result['error']}")
            else:
                st.success("Generation Successful ✅")


            

            st.subheader("Identity Cards")

            for card in result["identity_cards"]:

                with st.container(border=True):

                    st.markdown(f"### {card['timeline']}")
                    st.markdown(f"**{card['title']}**")
                    st.write(card["description"])

                    if card["proof_point"] is not None:

                        st.info(
                            f"Proof Point: {card['proof_point']}"
                        )

            
            
            

            st.subheader("Narration Script")

            st.write(result["narration_script"])

            # =========================
            # SHOW RAW JSON
            # =========================

            with st.expander("View Raw JSON Output"):

                st.json(result)

        except Exception as e:

            st.error(f"Error: {str(e)}")