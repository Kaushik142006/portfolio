import streamlit as st
from streamlit_lottie import st_lottie
import requests
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Kaushik | Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- DATA & CONSTANTS ---
NAME = "Kaushik Sathyanarayana"
ROLE = "Data Scientist & ML Engineer"
DESCRIPTION = """
I am a <span class="intro-highlight">B.E. student in Robotics and Artificial Intelligence</span> 
at <span class="intro-highlight">Dayananda Sagar College of Engineering</span>. 
I am passionate about <span class="intro-highlight">Data Science</span>, 
<span class="intro-highlight">Natural Language Processing </span> and <span class="intro-highlight">Machine Learning</span>, and I actively build projects 
to strengthen my skills in data analysis, machine learning, and intelligent systems 
while exploring areas such as deep learning, NLP, and robotics.
"""


SOCIAL_LINKS = {
    "LinkedIn": "https://www.linkedin.com/in/kaushik-sathyanarayana-6ab49432b/",
    "GitHub": "https://github.com/Kaushik142006",
}

RESUME_URL = "https://raw.githubusercontent.com/Kaushik142006/portfolio/main/kaushik_resume.pdf"

PROJECTS = [
    {
        "title": "CargoGuard AI Risk System",
        "description": "An advanced AI-driven system designed to assess and mitigate risks in cargo logistics, ensuring safety and efficiency through predictive risk modeling.",
        "url": "https://github.com/Kaushik142006/CargoGuard-AI-risk-system-",
        "icon": "📦",
        "tags": ["AI", "Risk Assessment", "Logistics", "Python"]
    },
    {
        "title": "RFP Insight Engine",
        "description": "An intelligent system that analyzes Request for Proposal documents using NLP and machine learning to extract key insights, requirements, and actionable information.",
        "url": "https://github.com/Kaushik142006/RFP-Insight-Engine",
        "icon": "📄",
        "tags": ["Document Analysis", "Python", "ML","Text Analytics"]
    },
    {
        "title": "Student Performance Analyzer",
        "description": "A comprehensive data analysis system developed to study student academic performance, uncover key influencing factors, and support early identification of academically at-risk students.",
        "url": "https://github.com/Kaushik142006/student-performance-analyzer",
        "icon": "📚",
        "tags": ["Pandas", "Education", "EDA", "Data Analysis"]
    },
    {
        "title":"News Detector AI",
        "description":"An NLP-based system designed to classify news articles as real or fake using machine learning techniques for accurate content verification and misinformation detection.",
        "url":"https://github.com/Kaushik142006/News-Detector-AI",
        "icon":"📰",
        "tags":["NLP", "Text Classification", "ML"]

    },
    {
        "title": "Fire Weather Prediction",
        "description": "A predictive model that forecasts fire weather conditions using meteorological data and machine learning algorithms to help prevent wildfire risks.",
        "url": "https://github.com/Kaushik142006/fire-weather-prediction",
        "icon": "🔥",
        "tags": ["Weather Prediction", "Random Forest", "Data Science", "Safety", "ML"]
    },
    {
        "title": "Travel Package Purchase Prediction",
        "description": "A machine learning based classification system that analyzes customer demographic, behavioral, and historical interaction data to predict the likelihood of purchasing travel packages.The model helps in businesse and understands customer preferences.",
        "url": "https://github.com/Kaushik142006/Travel-package-Purchase-Prediction",
        "icon": "✈️",
        "tags": ["Classification", "Marketing", "Customer Behavior", "ML"]
    }
]

SKILLS = [
    {"name": "Python", "icon": "🐍"},
    {"name": "Machine Learning", "icon": "🤖"},
    {"name": "Deep Learning", "icon": "🧠"},
    {"name": "Data Science", "icon": "📊"},
    {"name": "Natural Language Processing (NLP)", "icon": "💬"},
    {"name": "Scikit-learn", "icon": "⚙️"},
    {"name": "NLTK", "icon": "🧰"},
    {"name": "Gensim", "icon": "📚"},
    {"name": "Pandas", "icon": "🐼"},
    {"name": "NumPy", "icon": "🔢"},
    {"name": "Matplotlib", "icon": "📈"},
    {"name": "Feature Engineering", "icon": "🔧"},
    {"name": "SQL", "icon": "🗄️"},
    {"name": "Streamlit", "icon": "🖥️"},
    {"name": "Git", "icon": "📦"},
    {"name": "Jupyter Notebook", "icon": "📓"},
]


# --- ASSET LOADING ---
@st.cache_data
def load_lottie_url(url: str):
    """Loads Lottie animation from URL with caching."""
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception as e:
        print(f"Error loading Lottie: {e}")
        return None

# --- CSS STYLING ---
def load_css():
    """Injects the CSS styles."""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    * { font-family: 'Poppins', sans-serif; }
    .stApp { background: linear-gradient(135deg, #0f0f23 0%, #1a1a3e 50%, #0f0f23 100%); }
    
    /* ========================================
       NAVIGATION BAR (NEW FEATURE)
    ======================================== */
    .navbar {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background: rgba(15, 15, 35, 0.95);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border-bottom: 1px solid rgba(102, 126, 234, 0.2);
        padding: 15px 0;
        z-index: 9999;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
        animation: slideDown 0.5s ease-out;
    }
    
    .navbar-content {
        max-width: 1400px;
        margin: 0 auto;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0 40px;
    }
    
    .navbar-links {
        display: flex;
        gap: 35px;
        align-items: center;
    }
    
    /* ENHANCED: Improved navigation link hover states with glow */
    .nav-link {
        color: #c0c0d8;
        text-decoration: none;
        font-weight: 500;
        font-size: 0.95rem;
        padding: 8px 16px;
        border-radius: 25px;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        cursor: pointer;
    }
    
    .nav-link:hover {
        color: #ffffff;
        background: rgba(102, 126, 234, 0.2);
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .nav-link::after {
        content: '';
        position: absolute;
        bottom: 2px;
        left: 50%;
        transform: translateX(-50%) scaleX(0);
        width: 70%;
        height: 2px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        box-shadow: 0 0 8px rgba(102, 126, 234, 0.6);
        transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .nav-link:hover::after {
        transform: translateX(-50%) scaleX(1);
    }
    
    @keyframes slideDown {
        from { transform: translateY(-100%); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    
    /* FIXED: Reduced padding to decrease gap below navbar */
    .main-content {
        padding-top: 70px;
    }
    
    /* FIXED: Remove white background from Lottie animation container */
    div[data-testid="stImage"],
    div[data-testid="stLottie"],
    .stLottie,
    iframe[title="streamlit_lottie.streamlit_lottie"] {
        background-color: transparent !important;
        background: transparent !important;
    }
    
    /* ENHANCED: Add glow effect around illustration area */
    .illustration-wrapper {
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        padding: 20px;
    }
    
    .illustration-wrapper::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 120%;
        height: 120%;
        background: radial-gradient(circle, rgba(102, 126, 234, 0.15) 0%, transparent 70%);
        border-radius: 50%;
        animation: pulseGlowIllustration 4s ease-in-out infinite;
        z-index: -1;
    }
    
    .illustration-wrapper::after {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 110%;
        height: 110%;
        border: 2px solid transparent;
        border-radius: 50%;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.3), rgba(118, 75, 162, 0.3), rgba(240, 147, 251, 0.3));
        background-clip: padding-box;
        -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
        -webkit-mask-composite: xor;
        mask-composite: exclude;
        padding: 2px;
        animation: rotateBorder 8s linear infinite;
        z-index: -1;
    }
    
    @keyframes pulseGlowIllustration {
        0%, 100% { 
            opacity: 0.6;
            transform: translate(-50%, -50%) scale(1);
        }
        50% { 
            opacity: 1;
            transform: translate(-50%, -50%) scale(1.05);
        }
    }
    
    @keyframes rotateBorder {
        0% { filter: hue-rotate(0deg); }
        100% { filter: hue-rotate(360deg); }
    }
    
    /* ========================================
       IMPROVED SOCIAL BUTTONS (ENHANCED)
    ======================================== */
    .social-btn {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 15px 30px;
        border-radius: 50px;
        text-decoration: none;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        margin: 10px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    /* LinkedIn - Official Brand Color */
    .linkedin-btn, .linkedin-btn:visited, .linkedin-btn:active, .linkedin-btn:focus {
        background: linear-gradient(135deg, #0077B5, #00A0DC);
        color: #ffffff !important;
        text-decoration: none !important;
    }
    
    .linkedin-btn:hover {
        background: linear-gradient(135deg, #005582, #0077B5);
        transform: translateY(-8px) scale(1.08);
        box-shadow: 0 12px 35px rgba(0, 119, 181, 0.5), 0 0 30px rgba(0, 160, 220, 0.3);
        filter: brightness(1.1);
        color: #ffffff !important;
    }
    
    .linkedin-btn::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .linkedin-btn:hover::before {
        width: 300px;
        height: 300px;
    }
    
    /* GitHub - Official Brand Color */
    .github-btn {
        background: linear-gradient(135deg, #24292e, #2f363d);
        color: white;
    }
    
    .github-btn:hover {
        background: linear-gradient(135deg, #1a1e22, #24292e);
        transform: translateY(-8px) scale(1.08);
        box-shadow: 0 12px 35px rgba(36, 41, 46, 0.6), 0 0 30px rgba(47, 54, 61, 0.4);
        filter: brightness(1.2);
    }
    
    .github-btn::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.15);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .github-btn:hover::before {
        width: 300px;
        height: 300px;
    }

    /* Resume - Cyan/Blue Code */
    .resume-btn, .resume-btn:visited, .resume-btn:hover, .resume-btn:active, .resume-btn:focus {
        background: linear-gradient(135deg, #4facfe, #00f2fe);
        color: #ffffff !important;
        text-decoration: none !important;
    }
    
    .resume-btn:hover {
        background: linear-gradient(135deg, #00c6fb, #005bea);
        transform: translateY(-8px) scale(1.08);
        box-shadow: 0 12px 35px rgba(0, 198, 251, 0.5), 0 0 30px rgba(0, 91, 234, 0.3);
        filter: brightness(1.1);
        color: #ffffff !important;
    }
    
    .resume-btn::before {
        content: '';
        position: absolute;
        top: 50%;
        left: 50%;
        width: 0;
        height: 0;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        transform: translate(-50%, -50%);
        transition: width 0.6s, height 0.6s;
    }
    
    .resume-btn:hover::before {
        width: 300px;
        height: 300px;
    }
    
    /* Social button text should stay white and visible */
    .social-btn span {
        position: relative;
        z-index: 1;
    }
    
    /* ========================================
       CONTACT SECTION (NEW INLINE FORM)
    ======================================== */
    .contact-section {
        max-width: 800px;
        margin: 60px auto;
        background: linear-gradient(145deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
        border: 2px solid rgba(102, 126, 234, 0.3);
        border-radius: 30px;
        padding: 50px 45px;
        backdrop-filter: blur(20px);
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        animation: fadeInUp 1s ease-out, pulseGlow 4s ease-in-out infinite;
    }
    
    .contact-title {
        font-size: 2rem;
        font-weight: 600;
        text-align: center;
        color: #ffffff;
        margin-bottom: 15px;
        background: linear-gradient(90deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .contact-subtitle {
        text-align: center;
        color: #a0a0c0;
        font-size: 1.05rem;
        margin-bottom: 35px;
    }
    
    /* Streamlit Form Input Styling for Contact Section */
    div[data-testid="stForm"] {
        background: transparent;
        border: none;
    }
    
    div[data-testid="stForm"] label {
        color: #e0e0f0 !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        margin-bottom: 8px !important;
    }
    
    div[data-testid="stForm"] input,
    div[data-testid="stForm"] textarea {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: #ffffff !important;
        border: 2px solid rgba(102, 126, 234, 0.3) !important;
        border-radius: 12px !important;
        padding: 14px !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
    }
    
    div[data-testid="stForm"] input:focus,
    div[data-testid="stForm"] textarea:focus {
        border-color: rgba(102, 126, 234, 0.8) !important;
        box-shadow: 0 0 20px rgba(102, 126, 234, 0.3) !important;
        background-color: rgba(255, 255, 255, 0.08) !important;
    }
    
    div[data-testid="stForm"] input::placeholder,
    div[data-testid="stForm"] textarea::placeholder {
        color: #8888a8 !important;
    }
    
    /* Contact Form Submit Button */
    div[data-testid="stForm"] button[kind="primaryFormSubmit"] {
        background: linear-gradient(135deg, #667eea, #764ba2) !important;
        color: white !important;
        border: none !important;
        padding: 14px 35px !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
        transition: all 0.4s ease !important;
        margin-top: 10px !important;
        width: 100% !important;
    }
    
    div[data-testid="stForm"] button[kind="primaryFormSubmit"]:hover {
        transform: translateY(-4px) !important;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4) !important;
        background: linear-gradient(135deg, #764ba2, #667eea) !important;
    }

    /* Animations */
    @keyframes fadeInUp { from { opacity: 0; transform: translateY(40px); } to { opacity: 1; transform: translateY(0); } }
    @keyframes fadeInLeft { from { opacity: 0; transform: translateX(-40px); } to { opacity: 1; transform: translateX(0); } }
    @keyframes fadeInRight { from { opacity: 0; transform: translateX(40px); } to { opacity: 1; transform: translateX(0); } }
    @keyframes float { 0%, 100% { transform: translateY(0px); } 50% { transform: translateY(-20px); } }
    @keyframes floatRotate { 0%, 100% { transform: translateY(0px) rotate(0deg); } 25% { transform: translateY(-10px) rotate(5deg); } 50% { transform: translateY(-20px) rotate(0deg); } 75% { transform: translateY(-10px) rotate(-5deg); } }
    @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.05); } }
    @keyframes pulseGlow { 0%, 100% { transform: scale(1); box-shadow: 0 0 20px rgba(102, 126, 234, 0.3); } 50% { transform: scale(1.02); box-shadow: 0 0 40px rgba(102, 126, 234, 0.6); } }
    @keyframes gradient { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
    @keyframes shimmer { 0% { background-position: -200% 0; } 100% { background-position: 200% 0; } }
    @keyframes bounce { 0%, 20%, 50%, 80%, 100% { transform: translateY(0); } 40% { transform: translateY(-15px); } 60% { transform: translateY(-7px); } }
    @keyframes slideInScale { from { opacity: 0; transform: scale(0.8) translateY(30px); } to { opacity: 1; transform: scale(1) translateY(0); } }
    @keyframes borderGlow { 0%, 100% { border-color: rgba(102, 126, 234, 0.3); } 50% { border-color: rgba(118, 75, 162, 0.8); } }
    @keyframes textGlow { 0%, 100% { text-shadow: 0 0 10px rgba(102, 126, 234, 0.5); } 50% { text-shadow: 0 0 30px rgba(102, 126, 234, 1), 0 0 60px rgba(118, 75, 162, 0.5); } }
    @keyframes particleFloat { 0%, 100% { transform: translateY(0) translateX(0) rotate(0deg); opacity: 0.6; } 25% { transform: translateY(-30px) translateX(10px) rotate(90deg); opacity: 1; } 50% { transform: translateY(-50px) translateX(-10px) rotate(180deg); opacity: 0.6; } 75% { transform: translateY(-30px) translateX(15px) rotate(270deg); opacity: 1; } }

    /* Typography */
    .hero-title { font-size: 3.5rem; font-weight: 700; background: linear-gradient(90deg, #667eea, #764ba2, #f093fb, #667eea); background-size: 300% 300%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: gradient 4s ease infinite, fadeInUp 1s ease-out, textGlow 3s ease-in-out infinite; margin-bottom: 0; line-height: 1.2; }
    .hero-subtitle { font-size: 1.8rem; color: #a0a0c0; animation: fadeInUp 1s ease-out 0.2s both; margin-top: 10px; }
    .hero-description { font-size: 1.1rem; color: #8888a8; line-height: 1.8; animation: fadeInUp 1s ease-out 0.4s both; max-width: 600px; }
    .intro-highlight { background: linear-gradient(90deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; font-weight: 600; }
    .section-title { font-size: 2.5rem; font-weight: 600; text-align: center; color: #ffffff !important; margin-bottom: 50px; animation: fadeInUp 0.8s ease-out, textGlow 4s ease-in-out infinite; position: relative; }
    
    /* Decoration Under Section Titles */
    .section-title::after { content: ''; position: absolute; bottom: -15px; left: 50%; transform: translateX(-50%); width: 80px; height: 4px; background: linear-gradient(90deg, #667eea, #764ba2); border-radius: 2px; animation: shimmer 2s linear infinite; background-size: 200% 100%; }

    /* Cards */
    .skill-card { background: linear-gradient(145deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1)); border: 1px solid rgba(102, 126, 234, 0.2); border-radius: 20px; padding: 25px 20px; text-align: center; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); animation: slideInScale 0.6s ease-out both, borderGlow 3s ease-in-out infinite; backdrop-filter: blur(10px); cursor: pointer; height: 140px; display: flex; flex-direction: column; justify-content: center; align-items: center; }
    .skill-card:hover { transform: translateY(-15px) scale(1.05) rotateX(5deg); background: linear-gradient(145deg, rgba(102, 126, 234, 0.25), rgba(118, 75, 162, 0.25)); border-color: rgba(102, 126, 234, 0.7); box-shadow: 0 25px 50px rgba(102, 126, 234, 0.4), 0 0 30px rgba(118, 75, 162, 0.3); }
    .skill-icon { font-size: 2.5rem; margin-bottom: 10px; display: block; animation: floatRotate 4s ease-in-out infinite; }
    .skill-name { font-size: 0.95rem; font-weight: 500; color: #e0e0f0; margin: 0; }
    
    .about-card { background: linear-gradient(145deg, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0.02)); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 30px; padding: 40px; animation: fadeInLeft 1s ease-out, pulseGlow 4s ease-in-out infinite; backdrop-filter: blur(10px); }
    .edu-card, .exp-card { border-radius: 25px; padding: 35px; backdrop-filter: blur(10px); transition: all 0.4s ease; position: relative; overflow: hidden; }
    .edu-card { background: linear-gradient(145deg, rgba(102, 126, 234, 0.08), rgba(118, 75, 162, 0.08)); border: 2px solid rgba(102, 126, 234, 0.2); animation: fadeInRight 1s ease-out, borderGlow 3s ease-in-out infinite; }
    .exp-card { background: linear-gradient(145deg, rgba(240, 147, 251, 0.08), rgba(245, 87, 108, 0.08)); border: 2px solid rgba(240, 147, 251, 0.2); animation: fadeInLeft 1s ease-out, borderGlow 3s ease-in-out infinite; }
    .edu-card:hover, .exp-card:hover { transform: translateY(-10px); }
    
    .project-card { background: linear-gradient(145deg, rgba(79, 172, 254, 0.1), rgba(0, 242, 254, 0.05)); border: 2px solid rgba(79, 172, 254, 0.2); border-radius: 25px; padding: 30px; animation: slideInScale 0.8s ease-out both; backdrop-filter: blur(10px); transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); height: 100%; position: relative; overflow: hidden; }
    .project-card:hover { transform: translateY(-15px) scale(1.02); border-color: rgba(79, 172, 254, 0.6); box-shadow: 0 30px 60px rgba(79, 172, 254, 0.3), 0 0 40px rgba(0, 242, 254, 0.2); }
    .project-title { font-size: 1.3rem; font-weight: 600; color: #ffffff; margin-bottom: 15px; background: linear-gradient(90deg, #4facfe, #00f2fe); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .project-desc { font-size: 0.95rem; color: #a0a0c0; line-height: 1.7; margin-bottom: 20px; }
    
    /* Project Links - Bright White Text */
    a.project-link { 
        display: inline-flex; 
        align-items: center; 
        gap: 8px; 
        padding: 12px 25px; 
        background: linear-gradient(135deg, rgba(79, 172, 254, 0.2), rgba(0, 242, 254, 0.2)); 
        border: 1px solid rgba(79, 172, 254, 0.4); 
        border-radius: 50px; 
        color: #ffffff !important;
        text-decoration: none !important; 
        font-weight: 500; 
        font-size: 0.9rem; 
        transition: all 0.3s ease; 
    }
    
    a.project-link:visited {
        color: #ffffff !important;
    }

    a.project-link:hover { 
        background: linear-gradient(135deg, #4facfe, #00f2fe); 
        color: #0f0f23 !important;
        transform: scale(1.05); 
    }
    
    /* Elements */
    .divider { height: 2px; background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.5), transparent); margin: 80px 0; animation: shimmer 3s linear infinite; background-size: 200% 100%; }
    .tech-tag { display: inline-block; padding: 6px 14px; margin: 4px; background: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(118, 75, 162, 0.2)); border: 1px solid rgba(102, 126, 234, 0.3); border-radius: 20px; font-size: 0.8rem; color: #c0c0e0; animation: fadeInUp 0.5s ease-out both; }
    
    /* Background Shapes */
    .floating-shapes { position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: -1; overflow: hidden; }
    .shape { position: absolute; border-radius: 50%; animation: float 6s ease-in-out infinite; opacity: 0.1; }
    .shape-1 { width: 300px; height: 300px; background: linear-gradient(135deg, #667eea, #764ba2); top: 10%; left: -150px; animation: morphing 8s ease-in-out infinite, float 6s ease-in-out infinite; }
    .shape-2 { width: 200px; height: 200px; background: linear-gradient(135deg, #f093fb, #f5576c); top: 60%; right: -100px; animation: morphing 10s ease-in-out infinite, float 8s ease-in-out infinite; animation-delay: 2s; }
    .shape-3 { width: 150px; height: 150px; background: linear-gradient(135deg, #4facfe, #00f2fe); bottom: 10%; left: 20%; animation: morphing 7s ease-in-out infinite, float 5s ease-in-out infinite; animation-delay: 4s; }
    .shape-4 { width: 100px; height: 100px; background: linear-gradient(135deg, #fa709a, #fee140); top: 30%; right: 15%; animation: morphing 9s ease-in-out infinite, float 7s ease-in-out infinite; animation-delay: 1s; }
    .shape-5 { width: 80px; height: 80px; background: linear-gradient(135deg, #a8edea, #fed6e3); bottom: 30%; right: 25%; animation: morphing 6s ease-in-out infinite, particleFloat 10s ease-in-out infinite; animation-delay: 3s; }
    @keyframes morphing { 0%, 100% { border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%; } 25% { border-radius: 58% 42% 75% 25% / 76% 46% 54% 24%; } 50% { border-radius: 50% 50% 33% 67% / 55% 27% 73% 45%; } 75% { border-radius: 33% 67% 58% 42% / 63% 68% 32% 37%; } }
    
    /* About card specific styling */
    .about-card p {
        margin: 0 0 18px 0 !important;
        line-height: 1.9 !important;
        text-align: center;
        color: #c0c0d8;
    }
    .about-card {
        max-width: 1100px;
        width: 95%;
        padding: 45px;
        font-size: 1.15rem;
    }
    
    /* ------- HIDE STREAMLIT BRANDING ------- */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Specific override for custom footer */
    footer.custom-footer {
        visibility: visible;
        display: block;
        text-align: center; 
        padding: 40px; 
        color: #6666a8; 
        animation: fadeInUp 1s ease-out;
    }
    
    
    /* ========================================
       CONTACT FORM INPUT FIX - BLACK TEXT ON LIGHT BACKGROUND
    ======================================== */
    /* Text inputs and textarea - Pure black text, light background */
    div[data-testid="stForm"] input[type="text"],
    div[data-testid="stForm"] input[type="email"],
    div[data-testid="stForm"] textarea {
        background-color: #f5f5f5 !important;
        color: #000000 !important;
        caret-color: #000000 !important;
        border: 2px solid #d0d0d0 !important;
        border-radius: 8px !important;
        padding: 12px !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
    }
    
    /* Placeholder text - Light gray */
    div[data-testid="stForm"] input::placeholder,
    div[data-testid="stForm"] textarea::placeholder {
        color: #999999 !important;
        opacity: 1 !important;
    }
    
    /* Focus state - Keep black text, add border glow */
    div[data-testid="stForm"] input:focus,
    div[data-testid="stForm"] textarea:focus {
        background-color: #ffffff !important;
        color: #000000 !important;
        caret-color: #000000 !important;
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2) !important;
        outline: none !important;
    }
    
    /* Labels - Keep white for dark background */
    div[data-testid="stForm"] label {
        color: #ffffff !important;
        font-weight: 600 !important;
        margin-bottom: 6px !important;
    }
    
    /* ========================================
       RESPONSIVE DESIGN (MOBILE & TABLET)
    ======================================== */
    
    /* Tablet & Small Desktop (1024px and below) */
    @media (max-width: 1024px) {
        .navbar-content {
            padding: 0 20px;
        }
        
        .navbar-links {
            gap: 20px;
        }
        
        .hero-title {
            font-size: 2.8rem;
        }
        
        .illustration-wrapper {
            margin-top: 50px;
        }
    }
    
    /* Mobile Devices (768px and below) */
    @media (max-width: 768px) {
        /* Navigation */
        .navbar {
            padding: 10px 0;
            background: rgba(15, 15, 35, 0.98); /* Less transparent on mobile */
        }
        
        .navbar-content {
            flex-direction: column;
            gap: 15px;
            padding: 0 10px;
        }
        
        .navbar-links {
            gap: 10px;
            flex-wrap: wrap;
            justify-content: center;
        }
        
        .nav-link {
            font-size: 0.85rem;
            padding: 6px 12px;
        }
        
        /* Typography Scaling */
        .hero-title {
            font-size: 2.2rem;
            text-align: center;
        }
        
        .hero-subtitle {
            font-size: 1.3rem;
            text-align: center;
        }
        
        .hero-description {
            font-size: 1rem;
            text-align: center;
            margin: 0 auto;
        }
        
        .punch-line {
            text-align: center;
            font-size: 1rem;
        }
        
        .section-title {
            font-size: 2rem;
        }
        
        /* Layout Adjustments */
        .main-content {
            padding-top: 120px; /* More space for stacked navbar */
        }
        
        /* Cards */
        .why-hire-grid {
            grid-template-columns: 1fr; /* Stack hire items */
        }
        
        .edu-card, .exp-card, .about-card, .project-card, .contact-section {
            padding: 25px;
        }
        
        .skill-card {
            height: 120px; /* Smaller skill cards */
        }
        
        .skill-icon {
            font-size: 2rem;
        }
        
        /* Tech Cloud */
        .tech-cloud {
            padding: 20px 10px;
            gap: 15px;
        }
        
        .tech-cloud-item {
            padding: 10px 15px;
        }
        
        /* Social Buttons */
        .social-btn {
            padding: 12px 20px;
            font-size: 0.9rem;
        }
        
        /* Center Social Buttons Container */
        div:has(.social-btn) {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        /* Illustration */
        .illustration-wrapper {
            margin-top: 30px;
            transform: scale(0.9);
        }
        
        /* Footer Quote */
        .footer-quote {
            font-size: 1.1rem;
            margin: 40px 0 20px 0;
        }
    }
    
    /* Small Mobile (480px and below) */
    @media (max-width: 480px) {
        .hero-title {
            font-size: 1.8rem;
        }
        
        .nav-link {
            font-size: 0.75rem;
            padding: 5px 10px;
        }
        
        .project-card {
            padding: 20px;
        }
        
        .social-btn {
            width: 100%; /* Full width buttons on very small screens */
            justify-content: center;
            margin: 5px 0;
        }
        
        .navbar-links {
            gap: 5px;
        }
    }

    /* Smooth scrolling */
    html {
        scroll-behavior: smooth;
    }
    </style>
    
    <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
        <div class="shape shape-4"></div>
        <div class="shape shape-5"></div>
    </div>
    """, unsafe_allow_html=True)

# --- NAVIGATION BAR (NEW FEATURE) ---
def navigation_bar():
    """Renders the sticky navigation bar with smooth scroll functionality."""
    st.markdown("""
    <div class="navbar">
        <div class="navbar-content">
            <div class="navbar-links">
                <a href="#home" class="nav-link">Home</a>
                <a href="#about" class="nav-link">About</a>
                <a href="#skills" class="nav-link">Skills</a>
                <a href="#projects" class="nav-link">Projects</a>
                <a href="#contact" class="nav-link">Contact</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- UI SECTIONS ---
def header_section(lottie_url):
    """Header section with hero content and Lottie animation."""
    # Add anchor for navigation
    st.markdown('<div id="home"></div>', unsafe_allow_html=True)
    # FIXED: Removed extra <br> to reduce gap below navbar
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown(f"""
        <div style="padding-top: 20px;">
            <p style="color: #667eea; font-size: 1.2rem; animation: fadeInUp 0.8s ease-out; margin-bottom: 5px;">👋 Hello, I'm</p>
            <h1 class="hero-title">{NAME}</h1>
            <p class="hero-subtitle">{ROLE}</p>
            <p class="hero-description">{DESCRIPTION}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # ENHANCED Social Buttons with new hover effects and brand colors
        st.markdown(f"""
        <div style="margin-top: 30px;">
            <a href="{SOCIAL_LINKS['LinkedIn']}" target="_blank" class="social-btn linkedin-btn">
                <span>💼 LinkedIn</span>
            </a>
            <a href="{SOCIAL_LINKS['GitHub']}" target="_blank" class="social-btn github-btn">
                <span>💻 GitHub</span>
            </a>
            <a href="{RESUME_URL}" target="_blank" class="social-btn resume-btn">
                <span>📄 Resume</span>
            </a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # ENHANCED: Wrap Lottie animation in illustration wrapper for glow effect
        st.markdown('<div class="illustration-wrapper">', unsafe_allow_html=True)
        lottie_json = load_lottie_url(lottie_url)
        if lottie_json:
            st_lottie(lottie_json, height=400, key="coding")
        else:
            st.markdown("""<div style="height: 400px; display: flex; align-items: center; justify-content: center; font-size: 8rem;">👨‍💻</div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

def about_section():
    """About section with personal introduction."""
    # Add anchor for navigation
    st.markdown('<div id="about"></div>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)

    about_html = """
    <div style="display: flex; justify-content: center; width: 100%;">
        <div class="about-card">
            <p>
                I am a passionate and dedicated student with strong hands-on knowledge in
                <span class="intro-highlight">Data Science</span> and
                <span class="intro-highlight">Machine Learning</span>. I have worked with both
                <span class="intro-highlight">supervised</span> and
                <span class="intro-highlight">unsupervised learning</span> techniques, and I enjoy
                building and evaluating machine learning models to solve real-world problems.
            </p>
            <p>
                I have a strong interest in working with data, understanding patterns, and
                extracting meaningful insights from complex datasets. I enjoy applying
                data-driven approaches to practical use cases by transforming raw data into
                actionable and impactful solutions.
            </p>
            <p>
                I also have practical knowledge of
                <span class="intro-highlight">Natural Language Processing (NLP)</span>, where I work
                with text preprocessing, feature extraction, and basic language understanding
                techniques. Along with this, I have a strong foundation in
                <span class="intro-highlight">Python</span>, which I use extensively for data analysis,
                machine learning, and end-to-end project development.
            </p>
            <p>
                Currently, I am focused on expanding my knowledge in
                <span class="intro-highlight">Deep Learning</span>, while continuously strengthening
                my core machine learning fundamentals. I am actively learning, building projects,
                and exploring advanced AI concepts, with a growing interest in combining
                artificial intelligence with real-world systems such as
                <span class="intro-highlight">Robotics</span>.
            </p>
        </div>
    </div>
    """
    
    st.markdown(about_html, unsafe_allow_html=True)

def experience_section():
    """Education and Experience section."""
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Education & Experience</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="edu-card">
            <div style="font-size: 3rem; margin-bottom: 15px;">🎓</div>
            <h3 style="color: #ffffff; font-size: 1.5rem; background: linear-gradient(90deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Education</h3>
            <p style="color: #a0a0c0; font-size: 1.1rem;">B.E. in Artificial Intelligence & Robotics </p>
            <p style="color: #8888a8;">Dayananda Sagar College of Engineering</p>
            <div style="display: flex; align-items: center; gap: 10px; margin-top: 15px;">
                <span style="color: #667eea;">📅</span><p style="color: #c0c0d8; margin: 0;">2024 - 2028</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="exp-card">
            <div style="font-size: 3rem; margin-bottom: 15px;">💼</div>
            <h3 style="color: #ffffff; font-size: 1.5rem; background: linear-gradient(90deg, #f093fb, #f5576c); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Experience</h3>
            <p style="color: #a0a0c0; font-size: 1.1rem;">Aspiring Data Scientist & ML Engineer</p>
            <p style="color: #8888a8;">Building Real-World ML Projects</p>
            <div style="display: flex; align-items: center; gap: 10px; margin-top: 15px;">
                <span style="color: #f093fb;">🚀</span><p style="color: #c0c0d8; margin: 0;">5+ Projects Completed</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

def projects_section():
    """Featured projects section."""
    # Add anchor for navigation
    st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Featured Projects</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    for idx, project in enumerate(PROJECTS):
        column = col1 if idx % 2 == 0 else col2
        tags_html = "".join([f'<span class="tech-tag">{tag}</span>' for tag in project["tags"]])
        
        with column:
            st.markdown(f"""
            <div class="project-card" style="margin-bottom: 25px;">
                <div style="font-size: 3rem; margin-bottom: 15px;">{project["icon"]}</div>
                <h3 class="project-title">{project["title"]}</h3>
                <p class="project-desc">{project["description"]}</p>
                <div style="margin-bottom: 20px;">{tags_html}</div>
                <a href="{project["url"]}" target="_blank" class="project-link">View on GitHub</a>
            </div>
            """, unsafe_allow_html=True)

def skills_section():
    """Skills showcase section."""
    # Add anchor for navigation
    st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">My Skills</h2>', unsafe_allow_html=True)
    
    cols = st.columns(5)
    for idx, skill in enumerate(SKILLS):
        with cols[idx % 5]:
            delay = idx * 0.1
            st.markdown(f"""
            <div class="skill-card" style="animation-delay: {delay}s;">
                <span class="skill-icon">{skill['icon']}</span>
                <p class="skill-name">{skill['name']}</p>
            </div>
            <br>
            """, unsafe_allow_html=True)

def contact_section():
    """NEW: Direct contact form section (replaces modal)."""
    # Add anchor for navigation
    st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Get In Touch</h2>', unsafe_allow_html=True)
    
    # Contact form in a styled container
    st.markdown("""
    <div class="contact-section">
        <h3 class="contact-title">📬 Contact Me</h3>
        <p class="contact-subtitle">Have a question or want to work together? Send me a message!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create the form
    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name *", placeholder="Your name")
        with col2:
            email = st.text_input("Email *", placeholder="your.email@example.com")
        
        subject = st.text_input("Subject", placeholder="What's this about?")
        message = st.text_area("Message *", placeholder="Your message here...", height=150)
        
        submit_button = st.form_submit_button("🚀 Send Message", use_container_width=True)

        if submit_button:
            if not name or not email or not message:
                st.error("⚠️ Please fill in all required fields (Name, Email, and Message).")
            else:
                # Email sending logic using FormSubmit.co
                form_url = "https://formsubmit.co/kaushiksathya2006@gmail.com"
                
                data = {
                    "name": name,
                    "email": email,
                    "subject": subject if subject else "New Message from Portfolio",
                    "message": message,
                    "_captcha": "false",
                    "_template": "table"
                }
                
                try:
                    response = requests.post(form_url, data=data)
                    if response.status_code == 200:
                        st.success("✅ Message sent successfully! I'll get back to you soon. 🚀")
                    else:
                        st.error("❌ There was an error sending your message. Please try again.")
                except Exception as e:
                    st.error(f"❌ Error: {e}")

def footer_section():
    """Footer section with copyright information."""
    st.markdown("""
    <br><br>
    <footer class="custom-footer">
        <p style="font-size: 1rem;">Made with ❤️ using Streamlit</p>
        <p style="font-size: 0.85rem; margin-top: 10px;">© 2026 Kaushik Sathyanarayana. All Rights Reserved</p>
    </footer>
    """, unsafe_allow_html=True)

# --- MAIN APP ---
if __name__ == "__main__":
    # Load CSS first ensuring it is applied before any UI element
    load_css()

    # Render navigation bar first
    navigation_bar()
    
    # Add main-content wrapper to prevent navbar overlap
    st.markdown('<div class="main-content">', unsafe_allow_html=True)
    
    # Render all sections
    header_section("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
    about_section()
    experience_section()
    projects_section()
    skills_section()
    contact_section()  # NEW: Direct contact form instead of modal
    footer_section()
    
    st.markdown('</div>', unsafe_allow_html=True)