# Security-Risk-Analyzer

This tool scans Python code for OWASP Top 10 vulnerabilities using OpenAI's language models. It helps developers catch common security risks like SQL injection, XSS, hardcoded credentials, and more.

Features:
- Upload a Python file and get a detailed security analysis.
- Supports model fallback: tries GPT-4 first, then GPT-3.5 if unavailable.
- Highlights specific issues with recommendations.

Tech Stack:
- Python
- Streamlit for the interface
- OpenAI API for analysis
- dotenv for API key management

How to Use:
1. Clone the repository
2. Create a .env file and add your OpenAI API key:
   OPENAI_API_KEY=your_api_key_here
3. Install dependencies using pip:
   pip install -r requirements.txt
4. Run the app:
   streamlit run main.py

Notes:
- Requires an active OpenAI API key with access to GPT-3.5 or GPT-4.

