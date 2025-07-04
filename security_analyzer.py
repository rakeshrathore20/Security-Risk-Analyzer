
import streamlit as st
from analyzer_core import analyze_code
from openai import OpenAI
import os
from openai import OpenAI

client = OpenAI(api_key="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")


# Page
st.set_page_config(
    page_title="AI Security Risk Analyzer",
    layout="wide",
    page_icon="🛡️"
)

#theme
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #e1e4e8;
    font-family: 'Segoe UI', sans-serif;
}
h1, h2, h3 {
    color: #58a6ff;
}
.stButton>button {
    background-color: #238636;
    color: white;
    font-weight: 600;
    border: none;
    padding: 10px 20px;
    border-radius: 6px;
}
.stFileUploader, .stTextArea, .stTextInput {
    background-color: #161b22 !important;
    color: white;
    border-radius: 5px;
}
.report-style {
    background-color: #161b22;
    padding: 1.2rem;
    border-radius: 10px;
    border: 1px solid #30363d;
    font-family: Consolas, monospace;
    color: #e6edf3;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

#Title
st.title("Security Risk Analyzer")
st.markdown("Upload your source code to scan for **vulnerabilities** ")


file = st.file_uploader(" Upload your code file", type=["py", "js", "php", "java", "html"])

#  Analysis code
if st.button("🔍 Run Vulnerability Analysis"):
    if not file:
        st.error("Please upload a file to analyze.")
    else:
        with st.spinner("Analyzing your code..."):
            code = file.read().decode("utf-8")
            result = analyze_code(client, code)
            st.markdown("###  Vulnerability Report")
            st.markdown(f"<div class='report-style'>{result}</div>", unsafe_allow_html=True)
            st.success("Scan completed.")
