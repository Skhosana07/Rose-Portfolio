# -*- coding: utf-8 -*-
"""
Created on Sun Feb  1 23:01:13 2026

@author: lskhosana
"""

import streamlit as st
from streamlit_option_menu import option_menu
import base64
import time


st.set_page_config(
    page_title="Linah Rose | Research Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Poppins';
    }
    
.ai-hero {
    text-align:center;
    margin-top:200px;
    padding:70px;
    border-radius:25px;
    background: radial-gradient(circle at center, rgba(0,229,255,0.2), #0A192F);
    color:#00E5FF;
    box-shadow: 0 0 40px rgba(0, 229, 255, 0.4);
    transition: 0.3s ease;
}

.ai-hero h1 {
    font-size:60px;
    font-weight:700;
    text-shadow:0 0 15px #00E5FF;
}

.ai-hero:hover {
    box-shadow: 0 0 60px rgba(0, 229, 255, 0.8);
}

.intro {
    text-align: center;
    margin-top: 150px;
    animation: fadeInIntro 1.5s ease-in-out;
}

.fade-out {
    animation: fadeOutIntro 1s ease-in-out forwards;
}

@keyframes fadeInIntro {
    from { opacity: 0; transform: translateY(40px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeOutIntro {
    from { opacity: 1; }
    to { opacity: 0; }
}

.fade-in {
    animation: fadeIn 1.2s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(25px); }
    to { opacity: 1; transform: translateY(0); }
}

.profile-img {
    width: 300px;

    object-fit: cover;
}

.section-header {
    font-size: 32px;
    font-weight: 700;
    margin-top: 40px;
    margin-bottom: 20px;
}

.card {
    background-color: #a6a6a6;
    padding: 25px;
    border-radius: 15px;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
}

</style>
""", unsafe_allow_html=True)


# Greetings page
if "show_main" not in st.session_state:
    st.session_state.show_main = False

if not st.session_state.show_main:

    st.markdown("""
    <div class="ai-hero">
        <h1>Hello World 👋</h1>
        <h2>I'm Rose Linah Skhosana</h2>
    </div>
    """, unsafe_allow_html=True)

    time.sleep(2)
    st.session_state.show_main = True
    st.rerun()


# Sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["About", "Research", "Resume","Contacts"],
        icons=["person", "book", "file-earmark-text","telephone"],
        default_index=0,
    )
    
#About page
if selected == "About":

    col1, col2 = st.columns([0.5, 1], gap="small")

    with col1:
        image_path = "Profile.JPG"

        with open(image_path, "rb") as img_file:
            img_bytes = base64.b64encode(img_file.read()).decode()

        st.markdown(f"""
            <img src="data:image/jpeg;base64,{img_bytes}" class="profile-img">
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### 🌸 A Bit About Me 🌸")

        st.write("""
        I am a Master's researcher focusing on explainable AI and 
        misinformation detection in low-resource African languages, 
        particularly isiXhosa and isiZulu.

        My research combines machine learning, natural language 
        processing, and multimodal analysis to combat health misinformation.
        """)

 #Academic Background
    st.markdown('<div class="section-header fade-in">Academic Background</div>', unsafe_allow_html=True)

    with st.expander("MSc in Computer Science – North-West University (2025–Present)"):
        st.write("Research focus: Explainable AI & Health Misinformation")

    with st.expander("BSc Hons in Computer Science – Walter Sisulu University (2023)"):
        st.write("Mobile App Development")

    with st.expander("BSc in Computer Science – Walter Sisulu University (2020–2022)"):
        st.write("Major in Computer Science")


#Technical Skills
    st.markdown('<div class="section-header fade-in">Technical Skills</div>', unsafe_allow_html=True)

    skills = {
    "Python": 95,
    "Git & GitHub":90,
    "Streamlit":50,
    "Power BI & Data Analytics": 92,
    "React Native": 90,
    
     }

    for skill, percent in skills.items():
         st.write(f"**{skill}**")
         progress_bar = st.progress(0)
         
         for i in range(percent + 1):
             time.sleep(0.01)   # controls animation speed
             progress_bar.progress(i)
             
         st.write(f"{percent}%")

#Research Page
elif selected == "Research":

    st.markdown("## Research")

    st.subheader("BSc Honours Research: AI-Enhanced Lost and Found Mobile Application")

    st.write("""
    During my BSc Honours in Computer Science at Walter Sisulu University, 
    I designed and developed an Android-based Lost and Found Mobile Application 
    to improve the efficiency of item recovery within Higher Education Institutions.

    The system was developed using Kotlin in Android Studio, with Firebase 
    Authentication, Realtime Database, and Firebase Storage for backend 
    management. The project followed a Design Science Research Methodology 
    combined with Adaptive Software Development to ensure iterative refinement 
    and user-centered development.

    Beyond the core system implementation, I proposed the integration of 
    Artificial Intelligence components to enhance system intelligence and automation.
    """)

    st.markdown("### AI-Based Image Matching Concept")

    st.write("""
    One of the proposed AI enhancements involved incorporating an image 
    matching mechanism to automatically compare uploaded images of lost 
    and found items.

    The idea was to apply computer vision techniques using feature extraction 
    and similarity comparison models to:

    • Extract visual features from uploaded item images  
    • Compare newly uploaded images against existing database entries  
    • Detect potential matches automatically  
    • Notify users when a similarity threshold is met  

    This approach would reduce manual searching and increase the likelihood 
    of successful item recovery. The AI-based matching system would leverage 
    Convolutional Neural Networks (CNNs) or pretrained image embeddings to 
    compute similarity scores between items.
    """)

    st.markdown("### Intelligent Chatbot Integration Concept")

    st.write("""
    Another proposed AI enhancement was the integration of an intelligent 
    chatbot within the mobile application.

    The chatbot would:

    • Assist users in reporting lost or found items  
    • Guide users through structured form completion  
    • Answer frequently asked questions  
    • Provide real-time search assistance  
    • Suggest potential matches based on user descriptions  

    The chatbot could be implemented using Natural Language Processing (NLP) 
    techniques, enabling it to interpret user queries and map them to structured 
    database searches. This would improve accessibility, usability, and user engagement.

    The chatbot concept marked my first structured exploration into AI-driven 
    human-computer interaction and conversational systems.
    """)

    st.markdown("### Research Progression")

    st.write("""
    This Honours research laid the conceptual and technical foundation for my 
    current Master's research. While the Honours project focused on system 
    development and AI conceptual integration, my Master's research extends 
    this foundation into explainable AI and domain-specific misinformation 
    detection in low-resource African languages.

    The transition reflects a progression from applied AI system design 
    to advanced AI model development and explainability.
    """)

# Resume Page
elif selected == "Resume":

    st.markdown("""
    <div style="text-align: center; margin-top: 150px;">
        <h1>Resume</h1>
        <p style="font-size:20px;">
            Please click below to download my CV.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Center the button using columns
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        with open("Rose_CV.pdf", "rb") as file:
            st.download_button(
                label="Download CV",
                data=file,
                file_name="Linah_Rose_CV.pdf",
                mime="application/pdf",
                use_container_width=True
            )
#Contacts Page            
elif selected == "Contacts":

    st.markdown("## 🌸 Get in Touch")

    st.write("")
    
    st.markdown("""
    **Email:** linahrose06@gmail.com  

    **LinkedIn:** [linkedin.com/in/linah-rose-skhosana](www.linkedin.com/in/linah-rose-skhosana)

    **GitHub:** [github.com/Skhosana07](https://github.com/Skhosana07)

    **Location:** South Africa  
    """)

    st.write("")
    st.markdown(
        """
        I’m open to collaborations in **AI, data analytics, and research projects**.
        """
    )
