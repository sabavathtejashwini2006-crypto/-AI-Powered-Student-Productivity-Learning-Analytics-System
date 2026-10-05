import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_processing import load_academic_data, calculate_performance

st.title("📊 Student Dashboard")

df = load_academic_data()
df = calculate_performance(df)

student = st.selectbox("Select Student", sorted(df["student_id"].unique()))
data = df[df["student_id"] == student]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Average Marks", f"{data['marks'].mean():.1f}%")
c2.metric("Attendance", f"{data['attendance'].mean():.1f}%")
c3.metric("Study Hours", f"{data['study_hours'].mean():.1f}")
c4.metric("Performance", f"{data['performance_score'].mean():.1f}")

left, right = st.columns(2)

with left:
    fig = px.bar(data, x="subject", y="marks", title="Subject-wise Marks")
    st.plotly_chart(fig, use_container_width=True)

with right:
    fig = px.bar(data, x="subject", y="study_hours", title="Study Hours by Subject")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("📋 Academic Records")
st.dataframe(data, use_container_width=True)
