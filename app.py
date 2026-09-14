import streamlit as st
from recommender import recommend_jobs


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Tech Career Path 🚀",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 0% 0%, rgba(255, 190, 220, 0.55), transparent 28%),
        radial-gradient(circle at 100% 0%, rgba(190, 205, 255, 0.55), transparent 28%),
        radial-gradient(circle at 0% 100%, rgba(190, 245, 225, 0.50), transparent 28%),
        radial-gradient(circle at 100% 100%, rgba(255, 225, 190, 0.50), transparent 28%),
        linear-gradient(135deg, #fff9fc 0%, #f7f7ff 100%);
    min-height: 100vh;
}

header {
    visibility: hidden;
}

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


/* =========================================================
   HERO
   ========================================================= */

.hero {
    text-align: center;
    padding: 30px 10px 10px 10px;
}

.hero-badge {
    display: inline-block;
    padding: 9px 20px;
    border-radius: 30px;
    background: linear-gradient(90deg, #ffe4f0, #eee7ff);
    color: #7048a8;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.4px;
    box-shadow: 0 8px 25px rgba(139, 92, 246, 0.10);
    margin-bottom: 20px;
}

.hero-title {
    font-size: 56px;
    font-weight: 800;
    line-height: 1.15;
    color: #172554;
    margin: 0;
}

.gradient-text {
    background: linear-gradient(90deg, #ec4899, #a855f7, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    color: #64748b;
    font-size: 17px;
    margin-top: 18px;
}


/* =========================================================
   FEATURE PILLS
   ========================================================= */

.feature-container {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 12px;
    margin: 30px 0 40px 0;
}

.feature-pill {
    background: rgba(255, 255, 255, 0.92);
    border: 1px solid rgba(255,255,255,0.95);
    border-radius: 30px;
    padding: 11px 19px;
    color: #475569;
    font-size: 13px;
    font-weight: 600;
    box-shadow: 0 8px 25px rgba(100,116,139,0.10);
}


/* =========================================================
   INPUT CARD
   ========================================================= */

.input-card {
    background: rgba(255,255,255,0.95);
    border-radius: 28px;
    padding: 30px;
    border: 1px solid rgba(255,255,255,0.95);
    box-shadow: 0 20px 55px rgba(100,116,139,0.12);
    margin-bottom: 20px;
}

.input-title {
    color: #1e293b;
    font-size: 25px;
    font-weight: 700;
    margin-bottom: 8px;
}

.input-description {
    color: #64748b;
    font-size: 14px;
    line-height: 1.7;
}


/* =========================================================
   TEXT INPUT
   ========================================================= */

.stTextInput > div > div > input {
    background: #ffffff !important;
    color: #1e293b !important;
    border: 2px solid #ddd6fe !important;
    border-radius: 17px !important;
    padding: 17px 20px !important;
    font-size: 16px !important;
    box-shadow: 0 8px 25px rgba(139,92,246,0.08) !important;
}

.stTextInput > div > div > input::placeholder {
    color: #94a3b8 !important;
    opacity: 1 !important;
}

.stTextInput > div > div > input:focus {
    border-color: #a78bfa !important;
    box-shadow:
        0 0 0 4px rgba(167,139,250,0.15),
        0 10px 30px rgba(139,92,246,0.10) !important;
}


/* =========================================================
   TRY SKILLS
   ========================================================= */

.try-title {
    color: #64748b;
    font-size: 14px;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 10px;
}

.skill-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.skill-tag {
    display: inline-block;
    background: linear-gradient(135deg, #eef2ff, #fdf2f8);
    color: #5965a7;
    border: 1px solid #e5e7eb;
    border-radius: 20px;
    padding: 8px 14px;
    font-size: 13px;
}


/* =========================================================
   BUTTON
   ========================================================= */

.stButton {
    margin-top: 18px;
}

.stButton > button {
    width: 100%;
    border: none !important;
    border-radius: 17px !important;
    padding: 15px 25px !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    color: white !important;
    background: linear-gradient(135deg, #ec4899, #a855f7, #6366f1) !important;
    box-shadow: 0 12px 30px rgba(168,85,247,0.25) !important;
    transition: all 0.25s ease !important;
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 18px 40px rgba(168,85,247,0.35) !important;
}


/* =========================================================
   VALIDATION WARNING
   ========================================================= */

.warning-box {
    background: #fff8d9;
    border: 2px solid #f3d36b;
    border-radius: 18px;
    padding: 18px 22px;
    margin-top: 22px;
    color: #6b4f00;
    font-size: 15px;
    font-weight: 600;
    text-align: center;
    box-shadow: 0 8px 22px rgba(180,140,20,0.10);
}


/* =========================================================
   NO MATCH
   ========================================================= */

.no-match-box {
    background: linear-gradient(135deg, #fff1f2, #fdf4ff);
    border: 2px solid #f9a8d4;
    border-radius: 24px;
    padding: 32px;
    margin-top: 30px;
    text-align: center;
    box-shadow: 0 12px 35px rgba(236,72,153,0.10);
}

.no-match-icon {
    font-size: 40px;
    margin-bottom: 10px;
}

.no-match-title {
    color: #831843;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 12px;
}

.no-match-text {
    color: #64748b;
    font-size: 14px;
    line-height: 1.8;
}


/* =========================================================
   RESULTS TITLE
   ========================================================= */

.results-title {
    text-align: center;
    margin-top: 55px;
    margin-bottom: 30px;
}

.results-title h2 {
    color: #172554;
    font-size: 34px;
    font-weight: 800;
    margin-bottom: 8px;
}

.results-title p {
    color: #64748b;
    font-size: 14px;
}


/* =========================================================
   RESULT CARD
   ========================================================= */

.result-card {
    background: rgba(255,255,255,0.96);
    border-radius: 25px;
    padding: 25px;
    min-height: 220px;
    border: 2px solid rgba(255,255,255,0.95);
    box-shadow: 0 15px 40px rgba(100,116,139,0.12);
    transition: all 0.3s ease;
}

.result-card:hover {
    transform: translateY(-7px);
    box-shadow: 0 25px 50px rgba(139,92,246,0.17);
    border-color: #ddd6fe;
}

.rank-badge {
    display: inline-block;
    background: linear-gradient(135deg, #fce7f3, #ede9fe);
    color: #7c3aed;
    padding: 8px 15px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 700;
}

.job-title {
    color: #172554;
    font-size: 21px;
    font-weight: 700;
    line-height: 1.35;
    margin-top: 18px;
}

.score {
    font-size: 32px;
    font-weight: 800;
    margin-top: 12px;
    background: linear-gradient(90deg, #ec4899, #8b5cf6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.score-label {
    color: #94a3b8;
    font-size: 12px;
}


/* =========================================================
   SKILL INFORMATION
   ========================================================= */

.info-box {
    background: linear-gradient(135deg, #f8faff, #fff7fb);
    border-radius: 16px;
    padding: 15px;
    margin-top: 15px;
    color: #64748b;
    font-size: 12px;
    line-height: 1.7;
    border: 1px solid #f1f5f9;
}

.info-box-title {
    color: #475569;
    font-weight: 700;
    margin-bottom: 6px;
}


/* =========================================================
   WHY CAREER
   ========================================================= */

.why-box {
    background: linear-gradient(90deg, #fff0f7, #f5f3ff);
    color: #7c2d5e;
    border-radius: 15px;
    padding: 15px;
    margin-top: 15px;
    text-align: center;
    font-size: 12px;
    line-height: 1.6;
}


/* =========================================================
   MOTIVATION
   ========================================================= */

.motivation {
    margin-top: 50px;
    padding: 30px;
    border-radius: 27px;
    text-align: center;
    background: linear-gradient(120deg, #fff0f7, #eef2ff, #ecfdf5);
    border: 1px solid rgba(255,255,255,0.9);
    box-shadow: 0 12px 40px rgba(100,116,139,0.10);
}

.motivation h3 {
    color: #312e81;
    font-size: 22px;
    margin-bottom: 10px;
}

.motivation p {
    color: #64748b;
    font-size: 14px;
    max-width: 720px;
    margin: auto;
    line-height: 1.7;
}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {
    text-align: center;
    margin-top: 50px;
    color: #94a3b8;
    font-size: 12px;
    line-height: 2;
}


/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 768px) {

    .hero-title {
        font-size: 38px;
    }

    .hero-subtitle {
        font-size: 15px;
    }

    .input-card {
        padding: 22px;
    }

    .results-title h2 {
        font-size: 27px;
    }

    .result-card {
        margin-bottom: 20px;
    }

}

</style>
""",
unsafe_allow_html=True
)


# =========================================================
# HERO
# =========================================================

st.markdown(
"""
<div class="hero">

<div class="hero-badge">
✨ AI-POWERED CAREER DISCOVERY
</div>

<h1 class="hero-title">
Find Your Perfect<br>
<span class="gradient-text">Tech Career Path 🚀</span>
</h1>

<p class="hero-subtitle">
Your skills have a direction. Let AI help you discover it.
</p>

</div>
""",
unsafe_allow_html=True
)


# =========================================================
# FEATURE PILLS
# =========================================================

st.markdown(
"""
<div class="feature-container">

<div class="feature-pill">
💻 25+ Tech Roles
</div>

<div class="feature-pill">
🤖 AI Recommendation
</div>

<div class="feature-pill">
📊 TF-IDF Analysis
</div>

<div class="feature-pill">
🎯 Top 3 Matches
</div>

</div>
""",
unsafe_allow_html=True
)


# =========================================================
# INPUT INFORMATION
# =========================================================

st.markdown(
"""
<div class="input-card">

<div class="input-title">
💡 Tell Us About Your Skills
</div>

<div class="input-description">
Enter at least 3 technical skills separated by commas.
Our recommendation engine will find the career paths
that best match your profile.
</div>

</div>
""",
unsafe_allow_html=True
)


# =========================================================
# USER INPUT
# =========================================================

user_skills = st.text_input(
    "Skills",
    placeholder="Example: Python, Machine Learning, SQL",
    label_visibility="collapsed"
)


# =========================================================
# SKILL SUGGESTIONS
# =========================================================

st.markdown(
"""
<div class="try-title">
✨ Try these skills:
</div>

<div class="skill-tags">

<span class="skill-tag">Python</span>
<span class="skill-tag">Machine Learning</span>
<span class="skill-tag">SQL</span>
<span class="skill-tag">AWS</span>
<span class="skill-tag">Docker</span>
<span class="skill-tag">Data Analysis</span>
<span class="skill-tag">React</span>
<span class="skill-tag">JavaScript</span>

</div>
""",
unsafe_allow_html=True
)


# =========================================================
# BUTTON
# =========================================================

recommend_button = st.button(
    "🚀 Discover My Career Path"
)


# =========================================================
# RECOMMENDATIONS
# =========================================================

if recommend_button:

    # -----------------------------------------------------
    # CLEAN USER INPUT
    # -----------------------------------------------------

    skills = [
        skill.strip()
        for skill in user_skills.split(",")
        if skill.strip()
    ]


    # -----------------------------------------------------
    # VALIDATE INPUT
    # -----------------------------------------------------

    if len(skills) < 3:

        st.markdown(
"""
<div class="warning-box">
🌸 Please enter at least 3 technical skills to get accurate recommendations.
<br>
<span style="font-size:13px; font-weight:500;">
Example: Python, Machine Learning, SQL
</span>
</div>
""",
unsafe_allow_html=True
        )


    else:

        # -------------------------------------------------
        # COMBINE SKILLS
        # -------------------------------------------------

        skill_text = ", ".join(skills)


        # -------------------------------------------------
        # RUN ML RECOMMENDER
        # -------------------------------------------------

        try:

            results = recommend_jobs(
                skill_text,
                top_n=3
            )

        except Exception as error:

            st.error(
                "Something went wrong while generating recommendations."
            )

            st.code(str(error))

            st.stop()


        # -------------------------------------------------
        # CHECK EMPTY RESULTS
        # -------------------------------------------------

        if results is None or results.empty:

            st.markdown(
"""
<div class="no-match-box">

<div class="no-match-icon">
💭
</div>

<div class="no-match-title">
We couldn't find a strong career match
</div>

<div class="no-match-text">

The skills you entered don't have a strong
match with our technology career database.

<br><br>

Try technical skills such as:

<br><br>

<b>
Python • Machine Learning • SQL • AWS • Docker
• React • Data Analysis
</b>

</div>

</div>
""",
unsafe_allow_html=True
            )


        else:

            # -------------------------------------------------
            # GET BEST SCORE
            # -------------------------------------------------

            best_score = float(
                results["Similarity_Score"].max()
            )


            # -------------------------------------------------
            # NO MEANINGFUL MATCH
            # -------------------------------------------------

            if best_score < 0.05:

                st.markdown(
"""
<div class="no-match-box">

<div class="no-match-icon">
💭
</div>

<div class="no-match-title">
We couldn't find a strong career match
</div>

<div class="no-match-text">

The skills you entered don't have a strong
match with our technology career database.

<br><br>

Try entering technical skills such as:

<br><br>

<b>
Python • Machine Learning • SQL • AWS • Docker
• React • Data Analysis
</b>

</div>

</div>
""",
unsafe_allow_html=True
                )


            else:

                # =============================================
                # RESULTS HEADER
                # =============================================

                st.markdown(
"""
<div class="results-title">

<h2>
🏆 Your Top 3 Career Matches
</h2>

<p>
Based on TF-IDF and cosine similarity between your
skills and career requirements.
</p>

</div>
""",
unsafe_allow_html=True
                )


                # =============================================
                # CREATE THREE COLUMNS
                # =============================================

                columns = st.columns(3)


                # =============================================
                # LOOP THROUGH RESULTS
                # =============================================

                for rank, (_, row) in enumerate(
                    results.iterrows(),
                    start=1
                ):

                    # -----------------------------------------
                    # SCORE
                    # -----------------------------------------

                    score = float(
                        row["Similarity_Score"]
                    ) * 100

                    score = max(
                        0,
                        min(score, 100)
                    )


                    # -----------------------------------------
                    # CAREER NAME
                    # -----------------------------------------

                    job_role = str(
                        row["Job_Role"]
                    )


                    # -----------------------------------------
                    # CAREER SKILLS
                    # -----------------------------------------

                    career_skills = [
                        skill.strip()
                        for skill in str(
                            row["Skills"]
                        ).split(",")
                        if skill.strip()
                    ]


                    # -----------------------------------------
                    # USER SKILLS LOWERCASE
                    # -----------------------------------------

                    user_lower = [
                        skill.lower()
                        for skill in skills
                    ]


                    # -----------------------------------------
                    # FIND MATCHED SKILLS
                    # -----------------------------------------

                    matched_skills = []


                    for user_skill in user_lower:

                        for career_skill in career_skills:

                            career_lower = career_skill.lower()

                            if (
                                user_skill == career_lower
                                or user_skill in career_lower
                                or career_lower in user_skill
                            ):

                                if career_skill not in matched_skills:

                                    matched_skills.append(
                                        career_skill
                                    )


                    # -----------------------------------------
                    # SKILLS TO LEARN
                    # -----------------------------------------

                    skills_to_learn = [
                        skill
                        for skill in career_skills
                        if skill not in matched_skills
                    ]


                    # Keep cards clean

                    matched_skills = matched_skills[:6]

                    skills_to_learn = skills_to_learn[:6]


                    # -----------------------------------------
                    # MATCH MESSAGE
                    # -----------------------------------------

                    if score >= 70:

                        message = (
                            "🌟 Excellent match! Your skills "
                            "strongly align with this career."
                        )

                    elif score >= 40:

                        message = (
                            "💪 Good potential! You already have "
                            "several relevant skills."
                        )

                    else:

                        message = (
                            "✨ A career path worth exploring. "
                            "Keep building the required skills."
                        )


                    # =========================================
                    # RESULT CARD
                    # =========================================

                    with columns[rank - 1]:

                        st.markdown(
f"""
<div class="result-card">

<div class="rank-badge">
🏅 Rank #{rank}
</div>

<div class="job-title">
{job_role}
</div>

<div class="score">
{score:.1f}%
</div>

<div class="score-label">
Career Match Score
</div>

</div>
""",
unsafe_allow_html=True
                        )


                        # -------------------------------------
                        # PROGRESS BAR
                        # -------------------------------------

                        st.progress(
                            int(score)
                        )


                        # -------------------------------------
                        # MATCHED SKILLS
                        # -------------------------------------

                        if matched_skills:

                            matched_text = ", ".join(
                                matched_skills
                            )

                        else:

                            matched_text = (
                                "No direct skill matches found."
                            )


                        st.markdown(
f"""
<div class="info-box">

<div class="info-box-title">
🧩 Skills You Already Match
</div>

{matched_text}

</div>
""",
unsafe_allow_html=True
                        )


                        # -------------------------------------
                        # SKILLS TO LEARN
                        # -------------------------------------

                        if skills_to_learn:

                            learn_text = ", ".join(
                                skills_to_learn
                            )

                        else:

                            learn_text = (
                                "You already cover the listed skills! 🎉"
                            )


                        st.markdown(
f"""
<div class="info-box">

<div class="info-box-title">
📚 Skills You Can Learn Next
</div>

{learn_text}

</div>
""",
unsafe_allow_html=True
                        )


                        # -------------------------------------
                        # WHY CAREER
                        # -------------------------------------

                        st.markdown(
f"""
<div class="why-box">

💡 <b>Why this career?</b>

<br><br>

{message}

</div>
""",
unsafe_allow_html=True
                        )


                # =============================================
                # MOTIVATIONAL SECTION
                # =============================================

                st.markdown(
"""
<div class="motivation">

<h3>
💡 Keep Learning. Keep Building. Keep Growing. 💖
</h3>

<p>
Your skills are the beginning of your journey.
Keep learning, build real projects, participate in
hackathons and turn your interests into your future career.
</p>

</div>
""",
unsafe_allow_html=True
                )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
"""
<div class="footer">

🚀 <b>Tech Career Path</b>
&nbsp; | &nbsp;
Built with Python + Streamlit
&nbsp; | &nbsp;
DecodeLabs AI Internship — Project 3

</div>
""",
unsafe_allow_html=True
)