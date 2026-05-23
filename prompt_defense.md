# Prompt Defense Document

# Project: AI Career Transformation Assistant

# Objective

The goal of this project was to build an AI-powered system that generates:

Four identity transformation cards
One motivational narration script

based on a user’s career vision profile.

The system needed to support:

High wage ICP users
Low wage ICP users
English and Hindi outputs
Structured JSON responses
Emotionally supportive but realistic career transformation narratives

# Why This System Prompt?

The final system prompt was designed to solve four major requirements:

## 1. Structured JSON Output

The assignment required strict JSON formatting for downstream usage and validation.

So the prompt explicitly included:

exact schema
required keys
exact timeline values
null handling rules
prohibition of extra fields

This reduced inconsistent outputs from the LLM.

## 2. Controlled Emotional Tone

Initial generations were overly dramatic and cinematic.

Examples of issues:

exaggerated storytelling
unrealistic transformations
motivational language that felt artificial

To solve this, the prompt added instructions such as:

“Keep narration concise, grounded and voiceover-style”
“Avoid cinematic phrases”
“Use simple everyday language”
“Use supportive, non-harsh language”

This produced more realistic internship-level outputs.

## 3. Multilingual Support

The system needed to support both:

English users
Hindi users

Earlier attempts produced:

mixed Hindi-English text
unnatural Hindi translations

The prompt was improved with:

“Language must match user preference”
“For Hindi users, generate simple natural Hindi”

This improved consistency significantly.

## 4. Consistent Narration Length

Narration scripts initially became too long or too short.

To maintain consistency:

narration word limits were enforced
concise voiceover-style narration was specified

Final constraint:

narration must be between 60–70 words

# What Was Tried Initially?

The first version of the prompt was simpler and only asked the model to:

generate identity cards
generate narration

without strict formatting instructions.

Problems observed:

inconsistent JSON
missing fields
extra fields
invalid timelines
long narrations
dramatic storytelling
inconsistent proof points

# What Broke During Development?
## 1. JSON Parsing Errors

The model sometimes returned:

markdown
explanations
malformed JSON

Fix:

Added “Output ONLY valid JSON”
Added exact schema inside prompt
## 2. Proof Point Inconsistency

The model generated proof points for all timelines.

Requirement:

proof_point only for:
today
3 months

Fix:
Explicitly instructed:

proof_point must be null for 6 and 12 months
## 3. Narration Quality Issues

Earlier narrations:

sounded overly cinematic
used unrealistic transformations

Fix:
Added:

grounded tone
realistic language
simple supportive phrasing
## 4. API Rate Limits

Gemini free-tier quotas caused:

request exhaustion
interrupted testing

Fixes:

batch testing
retrying with another API key
storing outputs in all_test_outputs.json

# Final Result

The final system successfully supports:

multilingual generation
structured JSON outputs
schema validation
Streamlit-based POC demo
10 varied test cases
emotional yet realistic AI-generated career narratives

The project demonstrates practical use of:

prompt engineering
LLM integration
structured generation
frontend prototyping
validation workflows
multilingual AI experiences