import streamlit as st
import plotly.express as px
from utils.data_processing import load_academic_data

st.title("📚 Academic Analytics")

df = load_academic_data()
student = st.selectbox("Select Student", sorted(df["student_id"].unique()))
data = df[df["student_id"] == student]

st.subheader("Performance Analysis")

fig = px.bar(
    data,
    x="subject",
    y=["marks", "quiz_score", "assignment_score"],
    barmode="group",
    title="Subject Performance"
)
st.plotly_chart(fig, use_container_width=True)

weak = data.sort_values("marks").head(2)["subject"].tolist()
strong = data.sort_values("marks", ascending=False).head(2)["subject"].tolist()

c1, c2 = st.columns(2)
with c1:
    st.success("Strong Subjects: " + ", ".join(strong))
with c2:
    st.warning("Subjects Needing Attention: " + ", ".join(weak))
