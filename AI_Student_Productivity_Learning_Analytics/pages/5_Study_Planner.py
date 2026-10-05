import streamlit as st
from datetime import date, timedelta

st.title("📅 Personalized Study Planner")

subjects = st.multiselect(
    "Select subjects",
    ["Python", "DBMS", "Mathematics", "Computer Networks", "Statistics", "Machine Learning"],
    default=["Python", "Mathematics", "DBMS"]
)

hours = st.number_input("Available study hours per day", min_value=1, max_value=12, value=4)
days = st.number_input("Number of days", min_value=1, max_value=30, value=7)

if st.button("Generate Study Plan", type="primary"):
    if not subjects:
        st.warning("Select at least one subject.")
    else:
        st.subheader("📚 Your Study Plan")
        per_subject = max(0.5, round(hours / len(subjects), 1))
        start = date.today()

        for i in range(days):
            d = start + timedelta(days=i)
            st.markdown(f"### {d.strftime('%A, %d %B')}")
            for subject in subjects:
                st.write(f"• **{subject}** — {per_subject} hour(s)")
