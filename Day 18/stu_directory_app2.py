import streamlit as st
import pandas as pd

st.set_page_config(page_title="🎓 Student Directory", layout="centered")

# Initialize session state to store student data
if "students" not in st.session_state:
    st.session_state.students = []

st.title("🎓 Student Directory App")
st.write("Enter student details below:")

# Input form
with st.form("student_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    course = st.selectbox("Course", ["Engineering", "AI/ML", "Design", "Science", "Commerce"])
    score = st.number_input("Score", min_value=0, max_value=100)

    submitted = st.form_submit_button("Submit")

    if submitted:
        if name and email:
            st.session_state.students.append({
                "Name": name,
                "Email": email,
                "Course": course,
                "Score": score
            })
            st.success("✅ Student added!")
        else:
            st.warning("⚠️ Name and Email are required.")

# Convert session data to DataFrame
df = pd.DataFrame(st.session_state.students)

# Display all students
st.subheader("📄 All Students")
if not df.empty:
    st.dataframe(df)

    # Filter section
    st.subheader("🔍 Filter Students")

    filter_course = st.selectbox("Filter by Course", ["All"] + list(df["Course"].unique()))
    filter_score = st.slider("Minimum Score", 0, 100, 50)

    filtered_df = df.copy()

    if filter_course != "All":
        filtered_df = filtered_df[filtered_df["Course"] == filter_course]
    filtered_df = filtered_df[filtered_df["Score"] >= filter_score]

    st.write("🎯 Filtered Students:")
    st.dataframe(filtered_df)
else:
    st.info("No students added yet.")
