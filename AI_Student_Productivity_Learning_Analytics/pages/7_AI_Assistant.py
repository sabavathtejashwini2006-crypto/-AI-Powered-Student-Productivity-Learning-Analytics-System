import streamlit as st
from utils.data_processing import load_academic_data, load_productivity_data

st.title("💬 AI Student Assistant")

academic = load_academic_data()
productivity = load_productivity_data()

student = st.selectbox("Select Student", sorted(academic["student_id"].unique()))
a = academic[academic["student_id"] == student]
p = productivity[productivity["student_id"] == student]

question = st.text_input("Ask something about your learning and productivity")

if st.button("Get Recommendation", type="primary"):
    if not question.strip():
        st.warning("Enter a question first.")
    else:
        avg_marks = a["marks"].mean()
        avg_study = p["study_hours"].mean()
        weak = a.sort_values("marks").iloc[0]["subject"]

        st.subheader("🤖 Personalized Response")

        q = question.lower()

        if "weak" in q or "subject" in q:
            st.write(f"Your lowest-performing subject in this sample is **{weak}**. Consider allocating additional practice time to it.")
        elif "study" in q or "today" in q:
            st.write(f"Your average study time is **{avg_study:.1f} hours/day**. Focus on your weakest subject first, followed by revision.")
        elif "performance" in q or "marks" in q:
            st.write(f"Your current average marks are **{avg_marks:.1f}%**. Maintain strong subjects and spend additional time on lower-scoring areas.")
        else:
            st.write("Based on your current analytics, focus on consistency, weak subjects, assignment completion, and regular revision.")
