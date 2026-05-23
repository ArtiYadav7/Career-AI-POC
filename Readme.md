# Career Transformation AI POC (Voice Narrator + Possible-Self Vision )

## Overview

This project is a Proof of Concept (POC) for an AI-powered career transformation assistant.

The system takes structured user profile data as input and generates:

- 4 personalized identity transformation cards
- 1 motivational narration script

The generated outputs are personalized based on:
- current role
- target role
- career blockers
- urgency
- skills
- language preference

The project supports:
- High Wage ICP users
- Low Wage ICP users
- English narration
- Hindi narration

---

# Features

- AI-generated identity transformation cards
- AI-generated narration scripts
- English + Hindi multilingual support
- Structured JSON output generation
- Schema validation
- Batch testing on 10 varied ICP users
- Prompt engineering based generation
- Gemini API integration
- Streamlit-based interactive frontend
- Manual user input support
- Predefined test user support
- API exception handling
---

# Tech Stack

- Python
- Jupyter Notebook
- Google Gemini API
- python-dotenv
- JSON
- VS Code
- Streamlit

---

# Project Structure

Career_Ai_POC/
│
├── app.py
├── notebook.ipynb
├── README.md
├── PROMPT_DEFENSE.md
├── requirements.txt
├── all_test_outputs.json
├── .gitignore
└── .env

---

# How to Run

## 1. Clone Repository

```bash
git clone <your_repo_link>
cd Career_Ai_POC
```
---
## 2. Create Virtual Environment

```bash
python -m venv venv
```
### Activate Environment

### Windows PowerShell

```bash
.\venv\Scripts\Activate.ps1
```
---
## 3. Install Dependencies
```bash
pip install -r requirements.txt
```
---
## 4. Add Gemini API Key
Create a `.env` file:

```env
GOOGLE_API_KEY=your_api_key_here
```
---
## 5. Run Streamlit App

```bash
streamlit run app.py
```
---
## 6. Optional Notebook Execution

Open:
notebook.ipynb

Run all cells sequentially for notebook-based testing.


# Input Format

Example Input:

{
  "icp_type": "high_wage",
  "name": "Neha Kulkarni",
  "current_role": "Engineering student",
  "target_role": "Cloud Engineer",
  "urgency_months": 6,
  "skills": ["Python basics", "Linux basics"],
  "language": "en",

  "vision_profile": {
    "current_life": "Preparing for placements without internship experience",
    "main_blocker": "No hands-on cloud projects",
    "vision_12mo": "Working in a cloud engineering role at a tech company",
    "top_motivation": "Want a successful tech career and financial independence"
  }
}
# Output Format

Example Output:

{
  "identity_cards": [
    {
      "timeline": "today",
      "title": "Aspiring Engineer",
      "description": "Preparing for placements and learning cloud fundamentals.",
      "proof_point": "Learning Python and Linux basics."
    }
  ],

  "narration_script": "Neha is taking her first steps toward a successful cloud engineering career by building practical skills and confidence."
}
# Validation

The project includes schema validation to ensure:

correct JSON structure
correct timelines
required fields exist
successful narration generation
Testing

The system was tested on:

5 High Wage ICP users
5 Low Wage ICP users

# Testing included:

English outputs
Hindi outputs
varied professions
varied motivations
schema validation
Challenges Faced
Gemini API free-tier rate limits
JSON parsing issues
Prompt formatting problems
Maintaining narration length constraints
Making outputs realistic instead of overly dramatic


# Test Outputs

All generated test outputs are stored in:

all_test_outputs.json

# Included Deliverables

- Streamlit POC application
- 10 varied test cases
- all_test_outputs.json
- Prompt defense documentation
- README documentation
- Structured JSON generation
- Multilingual output support

# Challenges Faced

- Gemini API free-tier rate limits
- JSON parsing and formatting issues
- Maintaining strict schema consistency
- Controlling narration length and tone
- Avoiding overly dramatic AI-generated outputs
- Environment variable and API key conflicts
- Streamlit dependency installation issues

# Learnings

- Prompt engineering for structured JSON outputs
- Gemini API integration
- Schema validation workflows
- Multilingual AI generation
- Streamlit frontend integration
- API rate limit handling
- Exception handling in AI applications
- Batch testing AI-generated outputs
- Markdown documentation and GitHub project structuring


# Future Improvements

- Add text-to-speech voice generation
- Add retry and fallback handling for API failures
- Store outputs in database
- Add LangChain workflow orchestration
- Deploy as cloud web application
- Add user authentication and history

# Status

POC Successfully Completed


# Author
Arti Yadav

