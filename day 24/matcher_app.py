# app.py

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# STEP 1: Load the dataset

@st.cache_data
def load_students():
    # Load student profiles from CSV
    df = pd.read_csv("students.csv")
    return df

students_df = load_students()


#STEP 2: Vectorize student skills using TF-IDF

# TF-IDF converts text into numerical values to calculate similarity
vectorizer = TfidfVectorizer()
skill_matrix = vectorizer.fit_transform(students_df['skills'])

# 🖥️ Streamlit App UI

st.set_page_config(page_title="🤝 Student Skill Matcher", layout="centered")
st.title("🤝 Find Your Perfect Collaborator")
st.markdown("Enter your skills below to match with other students working on similar tech stacks!")

# Optional domain filter (e.g., AI, Web Dev, Cybersecurity)
domains = ['All'] + sorted(students_df['domain'].unique())
selected_domain = st.selectbox("🎯 Filter by Project Domain (optional):", domains)

# Skill input box
user_input = st.text_input("💬 Enter your skills (comma-separated):", "Python, Machine Learning")

#  When user clicks "Find Matches"

if st.button("🔍 Find Matches"):
    if user_input.strip() == "":
        st.warning("Please enter at least one skill.")
    else:
        # Vectorize the input
        user_vec = vectorizer.transform([user_input])

        # Calculate cosine similarity between user and all students
        similarity_scores = cosine_similarity(user_vec, skill_matrix).flatten()

        # Append scores to DataFrame
        results_df = students_df.copy()
        results_df['match_score'] = similarity_scores * 100  # Convert to percentage

        # Apply domain filter
        if selected_domain != "All":
            results_df = results_df[results_df['domain'] == selected_domain]

        # Sort and pick top 3 matches
        top_matches = results_df.sort_values(by='match_score', ascending=False).head(3)

        
        # 🧑‍💻 Display Top Matches
        
        if not top_matches.empty:
            st.subheader("🔗 Top 3 Collaborator Matches:")
            for _, row in top_matches.iterrows():
                st.markdown(f"""
                #### 👤 {row['name']}
                - 🛠️ **Skills**: {row['skills']}
                - 📁 **Domain**: {row['domain']}
                - 📊 **Match Score**: `{row['match_score']:.2f}%`
                ---
                """)
        else:
            st.warning("No matches found for your input or selected domain.")
