import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_processing import load_productivity_data

st.title("⏱️ Productivity Analytics")

df = load_productivity_data()
student = st.selectbox("Select Student", sorted(df["student_id"].unique()))
data = df[df["student_id"] == student].copy()

data["productivity_score"] = (
    data["study_hours"].clip(0, 8) / 8 * 40
    + data["task_completion"] * 0.35
    + data["consistency"] * 0.25
)

c1, c2, c3 = st.columns(3)
c1.metric("Avg Study Hours", f"{data['study_hours'].mean():.1f}")
c2.metric("Task Completion", f"{data['task_completion'].mean():.1f}%")
c3.metric("Productivity Score", f"{data['productivity_score'].mean():.1f}/100")

fig = px.line(
    data,
    x="date",
    y="study_hours",
    markers=True,
    title="Study Hours Trend"
)
st.plotly_chart(fig, use_container_width=True)

fig = px.line(
    data,
    x="date",
    y="productivity_score",
    markers=True,
    title="Productivity Score Trend"
)
st.plotly_chart(fig, use_container_width=True)
