# 🚀 Tech Career Path — AI-Powered Career Recommendation System

<div align="center">

### 💡 Discover the Tech Career That Matches Your Skills

An AI-powered career recommendation web application that analyzes your technical skills and recommends the most suitable technology career paths using **TF-IDF** and **Cosine Similarity**.

<br>

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas)
![Scikit Learn](https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

</div>

---

## 🌟 Overview

Choosing the right technology career can be difficult because the IT industry contains hundreds of different roles, each requiring a different combination of skills.

**Tech Career Path** solves this problem by allowing users to enter their technical skills and receive personalized career recommendations.

The system compares the user's skills with the skills required for different technology careers and identifies the **Top 3 most relevant career paths**.

The recommendation engine uses:

> **TF-IDF Vectorization + Cosine Similarity**

to measure the similarity between the user's skills and career requirements.

---

## 🎯 Problem Statement

Students and aspiring technology professionals often know the skills they have but are unsure about which career path best matches those skills.

For example, someone who knows:

```text
Python
Machine Learning
SQL
```

may be suitable for several careers such as:

- 🤖 AI Engineer
- 🧠 Machine Learning Engineer
- 📊 Data Scientist

However, manually comparing skills across multiple career paths can be time-consuming.

### 💡 Our Solution

Tech Career Path provides an easy-to-use AI-powered system that:

1. Accepts the user's technical skills.
2. Converts the skills into numerical representations.
3. Compares them with career skill requirements.
4. Calculates similarity scores.
5. Ranks the most relevant career paths.
6. Shows the Top 3 recommendations.
7. Identifies existing and missing skills.

---

## ✨ Key Features

### 🧠 AI-Based Recommendation

Uses machine-learning-based text similarity to recommend careers based on the user's technical skills.

### 📊 TF-IDF Analysis

TF-IDF converts skill descriptions into numerical vectors while giving importance to relevant terms.

### 🎯 Cosine Similarity

Cosine similarity measures how closely the user's skills match the requirements of each career.

### 🏆 Top 3 Career Matches

The system displays the three career paths with the highest similarity scores.

### 📈 Match Score

Each recommendation includes a percentage-based similarity score.

### 🧩 Skills You Already Match

The application identifies skills from the career requirements that match the user's existing skills.

### 📚 Skills You Can Learn Next

The application highlights additional skills that can help the user prepare for the recommended career.

### 💭 Intelligent No-Match Handling

If the entered skills do not have a meaningful match with the technology career database, the system provides a helpful message instead of showing misleading recommendations.

### ⚠️ Input Validation

The application requires at least **3 technical skills** to generate meaningful recommendations.

### 🎨 Modern User Interface

The Streamlit interface includes:

- Pastel gradient design
- Interactive buttons
- Career cards
- Skill tags
- Match indicators
- Responsive layout
- Friendly messages and emojis

---

## 💻 Technology Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Core programming language |
| 🎈 Streamlit | Web application framework |
| 🐼 Pandas | Dataset handling and processing |
| 🤖 Scikit-learn | TF-IDF and cosine similarity |
| 📄 CSV | Career skills dataset |
| 🎨 HTML/CSS | Custom frontend styling |
| 🔧 Git & GitHub | Version control and project hosting |

---

## 🧠 How the Recommendation System Works

The application follows a simple machine-learning pipeline.

```text
             👤 USER
               │
               ▼
      Enter Technical Skills
               │
               ▼
        🧹 Input Processing
               │
               ▼
        🔤 TF-IDF Vectorization
               │
               ▼
       📐 Cosine Similarity
               │
               ▼
     Compare With Career Skills
               │
               ▼
        📊 Calculate Scores
               │
               ▼
         🏆 Rank Careers
               │
               ▼
       ⭐ TOP 3 RECOMMENDATIONS
               │
       ┌───────┼────────┐
       ▼       ▼        ▼
   Match %   Skills   Skills to
             Matched   Learn
```

---

## 🔍 Recommendation Methodology

### Step 1 — User Input

The user enters at least three technical skills.

Example:

```text
Python, Machine Learning, SQL
```

### Step 2 — Skill Processing

The entered skills are cleaned and combined into a text representation.

### Step 3 — TF-IDF Vectorization

The system uses `TfidfVectorizer` from Scikit-learn to convert text into numerical vectors.

TF-IDF helps identify the importance of terms within the career skill descriptions.

### Step 4 — Cosine Similarity

The user's skill vector is compared with each career's skill vector using cosine similarity.

A higher similarity means the user's skills are more closely related to the career requirements.

### Step 5 — Ranking

Career paths are sorted according to their similarity scores.

### Step 6 — Recommendation

The system displays the Top 3 career paths along with:

- Match percentage
- Matching skills
- Skills to learn
- Career guidance

---

## 💼 Career Roles

The dataset contains **25+ technology career roles** covering areas such as:

### 🤖 Artificial Intelligence & Machine Learning

- AI Engineer
- Machine Learning Engineer
- Deep Learning Engineer
- Generative AI Engineer
- NLP Engineer
- Computer Vision Engineer
- MLOps Engineer
- Data Scientist
- AI Research Scientist

### 📊 Data & Analytics

- Data Analyst
- Data Engineer
- Business Intelligence Analyst

### ☁️ Cloud & DevOps

- Cloud Engineer
- Cloud Architect
- DevOps Engineer
- Cloud DevOps Engineer
- Site Reliability Engineer

### 💻 Software Engineering

- Software Engineer
- Backend Developer
- Full Stack Developer
- Frontend Developer
- Systems Engineer

### 🗄️ Database & Security

- Database Administrator
- Cybersecurity Analyst
- Software QA Engineer

---

## 🗂️ Project Structure

```text
Tech-Stack-Recommender/
│
├── 📄 app.py
│   └── Streamlit web application and frontend
│
├── 📄 recommender.py
│   └── TF-IDF + Cosine Similarity recommendation engine
│
├── 📄 raw_skills.csv
│   └── Career roles and required skills
│
├── 📄 requirements.txt
│   └── Python dependencies
│
├── 📄 README.md
│   └── Project documentation
│
├── 📄 .gitignore
│   └── Files excluded from Git
│
└── 📁 venv/
    └── Local Python virtual environment
```

> `venv/` is used locally and should not be uploaded to GitHub.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Move into the project directory:

```bash
cd Tech-Stack-Recommender
```

---

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

---

### 3️⃣ Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

## 🧪 Example

### Input

```text
Python, Machine Learning, SQL
```

### Output

The system analyzes the skills and generates the most relevant career paths.

Example:

```text
🏆 Your Top 3 Career Matches

🥇 AI Engineer
    Match Score: XX%

🥈 Machine Learning Engineer
    Match Score: XX%

🥉 Data Scientist
    Match Score: XX%
```

The application also shows:

```text
🧩 Skills You Already Match

📚 Skills You Can Learn Next

💡 Why this career?
```

---

## 🚫 Invalid / Weak Input Handling

The system also handles inappropriate or unrelated inputs.

For example:

```text
cooking, driving, running
```

Instead of falsely recommending technology careers, the application displays:

```text
💭 We couldn't find a strong career match.
```

It then suggests technical skills such as:

```text
Python
Machine Learning
SQL
AWS
Docker
React
Data Analysis
```

---

## 🎨 User Interface

The application was designed to provide a simple and enjoyable experience with:

✨ Pastel gradients  
🚀 Career-focused visuals  
🏆 Ranking cards  
📊 Match scores  
💡 Career insights  
🧩 Skill analysis  
📚 Learning suggestions  

---

## 📌 Project Objectives

The main objectives of this project are:

- Build a practical AI-powered recommendation system.
- Apply Natural Language Processing concepts to career data.
- Understand TF-IDF vectorization.
- Implement cosine similarity.
- Create a user-friendly machine learning web application.
- Help students understand possible technology career paths.
- Provide personalized skill-development suggestions.

---

## 🔮 Future Enhancements

The project can be further improved by adding:

- 👤 User profiles
- 📄 Resume upload and skill extraction
- 🧠 Advanced NLP models
- 🤖 Large Language Model integration
- 🎯 Personalized learning roadmaps
- 📚 Course recommendations
- 💼 Job vacancy recommendations
- 📈 Career demand analysis
- 🌍 Location-based career opportunities
- 📊 Career comparison dashboard
- 🔐 User authentication
- 💾 Database integration
- 📱 Mobile-friendly application
- ☁️ Cloud deployment

---

## 🔐 Data & Privacy

The current version does not require users to create an account or provide personal information.

The recommendation process is based on the technical skills entered into the application.

---

## 📚 Learning Outcomes

Through this project, I gained practical experience with:

- Python programming
- Pandas
- Scikit-learn
- Natural Language Processing
- TF-IDF
- Cosine Similarity
- Recommendation systems
- Streamlit
- Data preprocessing
- Frontend customization
- Git and GitHub
- Project documentation

---

## 👩‍💻 Project Information

**Project:** Tech Career Path — AI-Powered Career Recommendation System

**Program:** Artificial Intelligence Internship

**Organization:** DecodeLabs

**Project:** Internship Project 3

**Domain:** Artificial Intelligence / Machine Learning / NLP

**Developer:** Sanika Sapkal

---

## ⭐ Why This Project?

Technology careers are constantly evolving, and students often struggle to understand which career path fits their current skill set.

This project turns a simple list of skills into an actionable career direction.

> **Your skills are the starting point.  
> The right career path is the destination. 🚀**

---

## 📜 License

This project is created for educational and internship purposes.

---

<div align="center">

### 🚀 Tech Career Path

**Discover your skills. Explore your possibilities. Build your future. 💜**

Made with ❤️ using Python, Machine Learning & Streamlit

</div>

🧠 System Structure
Your actual application works like this:
                    👤 USER
                       │
                       ▼
              Enter 3+ Technical Skills
                       │
                       ▼
                🧹 Input Processing
                       │
                       ▼
              📄 Career Skills Dataset
                       │
                       ▼
               🔤 TF-IDF Vectorization
                       │
                       ▼
              📐 Cosine Similarity
                       │
                       ▼
                📊 Similarity Scores
                       │
                       ▼
                 📈 Sort Careers
                       │
                       ▼
                  🏆 Top 3
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
     Match Score   Matched Skills   Skills to
                                  Learn Next
                       │
                       ▼
                 💡 Career Insight
                       │
                       ▼
                🎨 Streamlit UI
🔄 Project Architecture
You can also show your architecture in your documentation/presentation as:
┌──────────────────────────────────────┐
│             USER INTERFACE           │
│              Streamlit               │
│                                      │
│  User enters technical skills        │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│          INPUT VALIDATION             │
│                                      │
│  Minimum 3 skills                    │
│  Empty input handling                │
│  Weak/no-match handling              │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│       RECOMMENDATION ENGINE          │
│                                      │
│  TF-IDF Vectorization                │
│            +                         │
│  Cosine Similarity                   │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│             DATASET                  │
│                                      │
│       raw_skills.csv                 │
│                                      │
│       25+ Career Roles               │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│          RANKING SYSTEM              │
│                                      │
│  Calculate similarity                │
│  Sort scores                         │
│  Select Top 3                        │
└──────────────────┬───────────────────┘
                   │
                   ▼
┌──────────────────────────────────────┐
│           RESULTS                    │
│                                      │
│  🏆 Top 3 Careers                    │
│  📊 Match Score                      │
│  🧩 Matched Skills                   │
│  📚 Skills to Learn                  │
│  💡 Why This Career                  │
└──────────────────────────────────────┘

## 👩‍💻 Author

**Sanika Nitin Sapkal**

B.Sc. Artificial Intelligence & Machine Learning | AI/ML Enthusiast

Built as part of my Artificial Intelligence Internship at DecodeLabs.

## screenshots
## INPUT
<img width="1897" height="912" alt="Screenshot 2026-09-14 180428" src="https://github.com/user-attachments/assets/2944996c-ddeb-45d0-ad52-23f4d59b4e3b" />

## OUTPUT
<img width="1897" height="910" alt="Screenshot 2026-09-14 180449" src="https://github.com/user-attachments/assets/d4106048-2747-4930-913b-5767a69dcc13" />

## NO-MATCH
<img width="1907" height="917" alt="Screenshot 2026-09-14 180526" src="https://github.com/user-attachments/assets/25a9f1b2-19b1-4f96-8cf5-13dc481723ef" />

