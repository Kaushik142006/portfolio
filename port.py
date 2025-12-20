import streamlit as st
from streamlit_lottie import st_lottie
import requests

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Kaushik | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- DATA & CONSTANTS ---
NAME = "Kaushik Sathyanarayana"
ROLE = "Data Scientist & ML Engineer"
DESCRIPTION = """
I am a passionate <span class="intro-highlight">Data Scientist</span> and 
<span class="intro-highlight">Machine Learning enthusiast</span> currently pursuing my studies 
while building real-world AI solutions. I transform complex data into actionable insights 
and develop predictive models that drive innovation.
"""

SOCIAL_LINKS = {
    "LinkedIn": "https://www.linkedin.com/in/kaushik-sathyanarayana-6ab49432b/",
    "GitHub": "https://github.com/Kaushik142006",
}

PROJECTS = [
    {
        "title": "CargoGuard AI Risk System",
        "description": "An advanced AI-driven risk assessment system designed to enhance cargo security by predicting potential threats and vulnerabilities in logistics chains.",
        "url": "https://github.com/Kaushik142006/CargoGuard-AI-risk-system-",
        "icon": "🛡️",
        "tags": ["AI Security", "Risk Assessment", "Predictive Modeling", "Logistics"]
    },
    {
        "title": "RFP Insight Engine",
        "description": "An intelligent system that analyzes Request for Proposal documents using NLP and machine learning to extract key insights, requirements, and actionable information.",
        "url": "https://github.com/Kaushik142006/RFP-Insight-Engine",
        "icon": "📄",
        "tags": ["NLP", "Document Analysis", "Python", "ML"]
    },
    {
        "title": "Student Performance Analyzer",
        "description": "A comprehensive ML solution that predicts and analyzes student academic performance based on various factors, helping educators identify at-risk students.",
        "url": "https://github.com/Kaushik142006/student-performance-analyzer",
        "icon": "📚",
        "tags": ["Predictive Analytics", "Education", "Scikit-learn", "Data Analysis"]
    },
    {
        "title": "Fire Weather Prediction",
        "description": "A predictive model that forecasts fire weather conditions using meteorological data and machine learning algorithms to help prevent wildfire risks.",
        "url": "https://github.com/Kaushik142006/fire-weather-prediction",
        "icon": "🔥",
        "tags": ["Weather Prediction", "Random Forest", "Data Science", "Safety"]
    },
    {
        "title": "Travel Package Purchase Prediction",
        "description": "A classification model that predicts customer likelihood to purchase travel packages based on demographics and behavior.",
        "url": "https://github.com/Kaushik142006/Travel-package-Purchase-Prediction",
        "icon": "✈️",
        "tags": ["Classification", "Marketing", "Customer Behavior", "ML"]
    }
]

SKILLS = [
    {"name": "Python", "icon": "🐍"}, {"name": "Machine Learning", "icon": "🤖"},
    {"name": "Data Science", "icon": "📊"}, {"name": "Deep Learning", "icon": "🧠"},
    {"name": "NLP", "icon": "💬"}, {"name": "Feature Engineering", "icon": "🔧"},
    {"name": "Pandas", "icon": "🐼"}, {"name": "NumPy", "icon": "🔢"},
    {"name": "Scikit-learn", "icon": "⚙️"}, {"name": "Data Cleaning", "icon": "🧹"},
    {"name": "Data Preprocessing", "icon": "🔄"}, {"name": "Data Analysis", "icon": "📈"},
    {"name": "SQL", "icon": "🗄️"}, {"name": "Git", "icon": "📦"},
    {"name": "Jupyter Notebook", "icon": "📓"}, {"name": "Problem Solving", "icon": "💡"},
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

# --- CONTACT FORM MODAL ---
@st.dialog("Contact Me")
def contact_form():
    # Specific Styling for the Modal
    st.markdown("""
    <style>
    /* Force the modal content background to white */
    div[role="dialog"] section {
        background-color: #ffffff !important;
    }
    div[role="dialog"] {
        color: #000000 !important;
    }
    
    /* Make Labels Dark Black */
    div[data-testid="stTextInput"] label, div[data-testid="stTextArea"] label {
        color: #000000 !important;
        font-weight: 600 !important;
    }
    
    /* Make Input Fields Dark with White Text */
    div[data-testid="stTextInput"] input, div[data-testid="stTextArea"] textarea {
        background-color: #252540 !important; /* Dark Blue/Black */
        color: #ffffff !important; /* White Text */
        border: 1px solid #444466 !important;
    }
    
    /* Input placeholder color styling */
    div[data-testid="stTextInput"] input::placeholder, div[data-testid="stTextArea"] textarea::placeholder {
        color: #a0a0c0 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    with st.form("contact_form"):
        name = st.text_input("Name", placeholder="Your name")
        email = st.text_input("Email", placeholder="Your email")
        subject = st.text_input("Subject", placeholder="Subject of your email")
        message = st.text_area("Message", placeholder="Your message")
        
        submit_button = st.form_submit_button("Send Message", type="primary", use_container_width=True)

        if submit_button:
            if not name or not email or not message:
                st.error("Please fill in all required fields.")
            else:
                # --- EMAIL SENDING LOGIC (Using FormSubmit.co) ---
                form_url = "https://formsubmit.co/kaushiksathya2006@gmail.com"
                
                # Hidden parameters to configure FormSubmit behavior
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
                        st.success("Message sent successfully! 🚀 Check your inbox.")
                    else:
                        st.error("There was an error sending your message. Please try again.")
                except Exception as e:
                    st.error(f"Error: {e}")

# --- CSS STYLING ---
def load_css():
    """Injects the CSS styles."""
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    * { font-family: 'Poppins', sans-serif; }
    .stApp { background: linear-gradient(135deg, #0f0f23 0%, #1a1a3e 50%, #0f0f23 100%); }
    
    /* Buttons in Streamlit default styling override for 'Email Me' */
    div.stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        padding: 10px 25px;
        border-radius: 50px;
        transition: all 0.3s ease;
        font-weight: 600;
    }
    div.stButton > button:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
        border: none;
        color: white;
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
    
    /* Buttons */
    .social-btn { display: inline-flex; align-items: center; gap: 10px; padding: 15px 30px; border-radius: 50px; text-decoration: none; font-weight: 600; font-size: 1rem; transition: all 0.4s; margin: 10px; position: relative; overflow: hidden; }
    .social-btn:hover { transform: translateY(-8px) scale(1.05); }
    .linkedin-btn { background: linear-gradient(135deg, #0077b5, #00a0dc); color: white; }
    .github-btn { background: linear-gradient(135deg, #333, #555); color: white; }
    .email-btn { background: linear-gradient(135deg, #ea4335, #ff6b6b); color: white; }
    .resume-btn { background: linear-gradient(135deg, #00c853, #69f0ae); color: white; }
    
    /* UPDATED: Added !important to FORCE WHITE TEXT */
    a.project-link { 
        display: inline-flex; 
        align-items: center; 
        gap: 8px; 
        padding: 12px 25px; 
        background: linear-gradient(135deg, rgba(79, 172, 254, 0.2), rgba(0, 242, 254, 0.2)); 
        border: 1px solid rgba(79, 172, 254, 0.4); 
        border-radius: 50px; 
        color: #ffffff !important; /* Forces Bright White Text */
        text-decoration: none !important; 
        font-weight: 500; 
        font-size: 0.9rem; 
        transition: all 0.3s ease; 
    }
    
    /* Visited links also stay white */
    a.project-link:visited {
        color: #ffffff !important;
    }

    a.project-link:hover { 
        background: linear-gradient(135deg, #4facfe, #00f2fe); 
        color: #0f0f23 !important; /* Dark Text on Hover */
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
    
    /* ------- HIDE STREAMLIT BRANDING ------- */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Specific override for YOUR custom footer */
    footer.custom-footer {
        visibility: visible;
        display: block;
        text-align: center; 
        padding: 40px; 
        color: #6666a8; 
        animation: fadeInUp 1s ease-out;
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

# --- UI SECTIONS ---
def header_section(lottie_url):
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown(f"""
        <div style="padding-top: 50px;">
            <p style="color: #667eea; font-size: 1.2rem; animation: fadeInUp 0.8s ease-out; margin-bottom: 5px;">👋 Hello, I'm</p>
            <h1 class="hero-title">{NAME}</h1>
            <p class="hero-subtitle">{ROLE}</p>
            <p class="hero-description">{DESCRIPTION}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Social Buttons
        st.markdown(f"""
        <div style="margin-top: 30px;">
            <a href="{SOCIAL_LINKS['LinkedIn']}" target="_blank" class="social-btn linkedin-btn">LinkedIn</a>
            <a href="{SOCIAL_LINKS['GitHub']}" target="_blank" class="social-btn github-btn">GitHub</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        lottie_json = load_lottie_url(lottie_url)
        if lottie_json:
            st_lottie(lottie_json, height=400, key="coding")
        else:
            st.markdown("""<div style="height: 400px; display: flex; align-items: center; justify-content: center; font-size: 8rem;">👨‍💻</div>""", unsafe_allow_html=True)

def about_section():
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="about-card">
            <p style="color: #c0c0d8; font-size: 1.1rem; line-height: 2; text-align: center;">
                I am a passionate learner with a solid foundation in <span class="intro-highlight">Machine Learning</span>, 
                including both supervised and unsupervised learning techniques. 
                <br><br>
                I am now expanding my skills into <span class="intro-highlight">Deep Learning</span>, 
                <span class="intro-highlight">NLP</span>, and <span class="intro-highlight">Agentic AI</span>.
                I also have a growing interest in <span class="intro-highlight">Robotics</span>.
            </p>
        </div>
        """, unsafe_allow_html=True)

def experience_section():
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Education & Experience</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="edu-card">
            <div style="font-size: 3rem; margin-bottom: 15px;">🎓</div>
            <h3 style="color: #ffffff; font-size: 1.5rem; background: linear-gradient(90deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Education</h3>
            <p style="color: #a0a0c0; font-size: 1.1rem;">B.E. in Robotics & Artificial Intelligence</p>
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

def footer_section():
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Let\'s Connect</h2>', unsafe_allow_html=True)
    
    # FIXED: Added spacing to prevent the section-title underline from overlapping the text below
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div style="text-align: center; position: relative; z-index: 2;">
            <p style="color: #a0a0c0; font-size: 1.2rem; margin-bottom: 30px; text-decoration: none;">
                I'm always open to discussing new projects and creative ideas.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        b_col1, b_col2, b_col3 = st.columns([1, 2, 1])
        with b_col2:
            if st.button("✉️ Email Me", use_container_width=True):
                contact_form()

    # FIXED: Added 'class="custom-footer"' so the CSS override works and shows the copyright text
    st.markdown("""
    <br><br>
    <footer class="custom-footer">
        <p style="font-size: 1rem;">Made with ❤️ using Streamlit</p>
        <p style="font-size: 0.85rem; margin-top: 10px;">© 2025 Kaushik Sathyanarayana. All Rights Reserved</p>
    </footer>
    """, unsafe_allow_html=True)

# --- MAIN APP ---
if __name__ == "__main__":
    load_css()
    header_section("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
    about_section()
    experience_section()
    projects_section()
    skills_section()
    footer_section()