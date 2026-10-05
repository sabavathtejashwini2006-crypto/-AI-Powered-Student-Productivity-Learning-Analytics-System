import streamlit as st
from utils.ml_model import train_model, predict_performance

st.title("🤖 AI Performance Prediction")

st.write("Enter student information to predict the academic performance category.")

study_hours = st.slider("Study Hours per Day", 0.0, 10.0, 4.0, 0.5)
attendance = st.slider("Attendance (%)", 0, 100, 80)
assignment = st.slider("Assignment Completion (%)", 0, 100, 75)
quiz = st.slider("Quiz Score (%)", 0, 100, 70)
previous = st.slider("Previous Marks (%)", 0, 100, 70)
consistency = st.slider("Study Consistency (%)", 0, 100, 70)

if st.button("Predict Performance", type="primary"):
    model = train_model()
    prediction = predict_performance(
        model,
        study_hours,
        attendance,
        assignment,
        quiz,
        previous,
        consistency
    )

    if prediction == "Excellent":
        st.success(f"Predicted Performance: {prediction}")
    elif prediction == "Good":
        st.info(f"Predicted Performance: {prediction}")
    elif prediction == "Average":
        st.warning(f"Predicted Performance: {prediction}")
    else:
        st.error(f"Predicted Performance: {prediction}")

    st.subheader("🔎 Main Factors")
    if study_hours < 3:
        st.write("• Increase focused study time.")
    if attendance < 75:
        st.write("• Improve attendance.")
    if assignment < 70:
        st.write("• Complete more assignments.")
    if quiz < 60:
        st.write("• Practice more quiz questions.")
    if consistency < 60:
        st.write("• Follow a more consistent study routine.")
