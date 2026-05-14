# app.py

import streamlit as st
from pipeline import run_research_pipeline
import time

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Multi Agent Research System",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CUSTOM CSS ---------------- #
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.title {
    font-size: 42px;
    font-weight: bold;
    color: #4CAF50;
    text-align: center;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    color: #B0B0B0;
    font-size: 18px;
    margin-bottom: 40px;
}

.section {
    padding: 20px;
    border-radius: 15px;
    background-color: #161B22;
    margin-bottom: 20px;
    border: 1px solid #30363D;
}

.agent-title {
    color: #58A6FF;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}

.report-box {
    background-color: #1C2128;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #30363D;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown(
    '<div class="title">🤖 Multi Agent Research System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI Powered Research • Search • Scrape • Write • Critic</div>',
    unsafe_allow_html=True
)

# ---------------- INPUT ---------------- #
topic = st.text_input(
    "🔍 Enter Research Topic",
    placeholder="Example: Future of Artificial Intelligence"
)

run_button = st.button("🚀 Start Research")

# ---------------- MAIN LOGIC ---------------- #
if run_button:

    if not topic.strip():
        st.warning("Please enter a research topic.")
        st.stop()

    with st.spinner("Agents are working on your research..."):

        try:
            # Run pipeline
            result = run_research_pipeline(topic)

            # ---------------- SEARCH RESULTS ---------------- #
            st.markdown('<div class="section">', unsafe_allow_html=True)
            st.markdown(
                '<div class="agent-title">🔎 Search Agent Results</div>',
                unsafe_allow_html=True
            )

            st.write(result.get("search_results", "No search results found"))
            st.markdown('</div>', unsafe_allow_html=True)

            time.sleep(1)

            # ---------------- SCRAPED CONTENT ---------------- #
            st.markdown('<div class="section">', unsafe_allow_html=True)
            st.markdown(
                '<div class="agent-title">📄 Reader Agent Scraped Content</div>',
                unsafe_allow_html=True
            )

            st.write(result.get("scraped_content", "No scraped content found"))
            st.markdown('</div>', unsafe_allow_html=True)

            time.sleep(1)

            # ---------------- FINAL REPORT ---------------- #
            st.markdown('<div class="section">', unsafe_allow_html=True)
            st.markdown(
                '<div class="agent-title">📝 Final Research Report</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="report-box">{result.get("report", "No report generated")}</div>',
                unsafe_allow_html=True
            )

            st.markdown('</div>', unsafe_allow_html=True)

            time.sleep(1)

            # ---------------- CRITIC FEEDBACK ---------------- #
            st.markdown('<div class="section">', unsafe_allow_html=True)
            st.markdown(
                '<div class="agent-title">🧠 Critic Feedback</div>',
                unsafe_allow_html=True
            )

            st.write(result.get("feedback", "No feedback generated"))
            st.markdown('</div>', unsafe_allow_html=True)

            # ---------------- DOWNLOAD REPORT ---------------- #
            st.download_button(
                label="📥 Download Report",
                data=str(result.get("report", "")),
                file_name=f"{topic}_research_report.txt",
                mime="text/plain"
            )

            st.success("Research Completed Successfully ✅")

        except Exception as e:
            st.error(f"Error: {e}")