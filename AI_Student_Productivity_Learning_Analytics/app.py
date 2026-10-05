import streamlit as st
from utils.database import init_db

init_db()

st.set_page_config(
    page_title="AI Student Productivity & Learning Analytics",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 AI-Powered Student Productivity & Learning Analytics System")
st.write("Analyze academic performance, productivity, learning patterns, and generate personalized study insights.")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Students", "25")
c2.metric("Avg Attendance", "84%")
c3.metric("Avg Study Hours", "4.2 hrs")
c4.metric("Avg Performance", "76%")

st.subheader("🚀 Project Modules")
st.markdown("""
- 📊 **Dashboard** – Overall academic and productivity analytics
- 📚 **Academic Analytics** – Subject-wise marks, attendance and assignments
- ⏱️ **Productivity Analytics** – Study hours, tasks and productivity trends
- 🤖 **Performance Prediction** – Machine-learning based performance prediction
- 📅 **AI Study Planner** – Personalized study planning
- 🔔 **Smart Alerts** – Detect academic and productivity problems
- 💬 **AI Student Assistant** – Personalized learning guidance
""")

st.info("Use the pages in the left sidebar to explore each module.")
