import streamlit as st
from utils.data_processing import load_academic_data, load_productivity_data

st.title("🔔 Smart Alerts")

academic = load_academic_data()
productivity = load_productivity_data()

student = st.selectbox("Select Student", sorted(academic["student_id"].unique()))
a = academic[academic["student_id"] == student]
p = productivity[productivity["student_id"] == student]

alerts = []

if a["attendance"].mean() < 75:
    alerts.append("⚠️ Attendance is below 75%.")

if a["marks"].mean() < 60:
    alerts.append("⚠️ Overall academic performance needs improvement.")

if a["assignment_score"].mean() < 70:
    alerts.append("⚠️ Assignment completion/performance is low.")

if p["study_hours"].mean() < 3:
    alerts.append("⚠️ Average study time is low.")

if p["task_completion"].mean() < 70:
    alerts.append("⚠️ Task completion is below the recommended project threshold.")

if not alerts:
    st.success("✅ No major alerts detected.")
else:
    for alert in alerts:
        st.warning(alert)
