# 🤝 AI-Powered Student Skill Matcher

Find your perfect collaborators for tech projects based on shared skills and interests!

## 📌 Project Overview

This web app helps students connect with potential collaborators by analyzing their skills and interests. Think of it as a **“Tinder for tech collabs”** — just enter your skills, and the app recommends the top 3 most compatible students to work with.

It uses:
- ✅ **TF-IDF vectorization** to convert skills into numerical features
- ✅ **Cosine similarity** to measure compatibility
- ✅ **Streamlit** to build an interactive and user-friendly web app

---

## 🚀 Features

- 🔍 Enter your skills to find similar profiles
- 🎯 Filter by project domain (e.g., AI, Web Dev, Cybersecurity)
- 📊 View top 3 student matches with match percentage
- 📁 Uses a real-world-style `.csv` dataset of student profiles
- ⚡ Fast and lightweight app (runs locally or on Streamlit Cloud)

---

## 📂 Dataset: `students.csv`

A synthetic dataset containing 20–30 student profiles with the following fields:

| Column   | Description                        |
|----------|------------------------------------|
| name     | Full name of the student           |
| skills   | Comma-separated list of skills     |
| domain   | Main interest/project area         |

### ✨ Example:

```csv
name,skills,domain
Divya Rao,"JavaScript, UI/UX Design, Figma",Web Development
Karan Das,"Data Science, Python, NumPy",Data Science
Simran Kaur,"Networking, Cybersecurity, Firewalls",Cybersecurity