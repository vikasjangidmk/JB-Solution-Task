
import streamlit as st
import os
from dotenv import load_dotenv
from crew import research_crew
from memory.memory_store import MemoryStore

load_dotenv()

st.set_page_config(page_title="Autonomous Research Agent", page_icon="🔎")

st.title("🔎 Autonomous Research Agent")
st.caption("Planner • Tools • Memory • Report Generation")

topic = st.text_input("Enter a research topic", value="Top React Native libraries in 2025")
col1, col2 = st.columns(2)
with col1:
    if st.button("Run Research"):
        with st.spinner("Thinking, searching, analyzing..."):
            result = research_crew.kickoff(inputs={"topic": topic})
        st.success("Done!")
        st.subheader("Final Report")
        st.write(result)

with col2:
    st.markdown("### 📒 Memory Lookup")
    q = st.text_input("Query memory", value="React Native libraries")
    if st.button("Search Memory"):
        ms = MemoryStore()
        hits = ms.query(q, k=5)
        for h in hits:
            st.write(f"- {h['text']}")
    
st.divider()
st.markdown("### 🪵 Logs")
log_files = sorted([f for f in os.listdir("logs") if f.endswith(".log")], reverse=True) if os.path.isdir("logs") else []
if log_files:
    pick = st.selectbox("Select a log file", log_files)
    st.code(open(os.path.join("logs", pick),'r',encoding='utf-8').read())
else:
    st.info("No logs yet. Run a job to populate logs.")
