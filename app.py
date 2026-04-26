import streamlit as st
import pandas as pd
import random
import time

# ----------------------------------------
# PAGE CONFIGURATION & MODERN CSS
# ----------------------------------------
st.set_page_config(page_title="CampusConnect", page_icon="🌐", layout="wide")

st.markdown("""
    <style>
    /* Premium Gradient Header */
    .gradient-text {
        background: -webkit-linear-gradient(45deg, #0056b3, #00d2ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 0px;
    }
    
    /* Modern Sleek Metric Cards */
    [data-testid="stMetricValue"] {
        font-size: 2rem !important;
        font-weight: 700 !important;
        color: #0056b3;
    }
    [data-testid="stMetricLabel"] {
        font-size: 1rem !important;
        color: #666 !important;
        font-weight: 600;
    }
    
    /* Hide the default Streamlit top menu and footer for a clean SaaS look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ----------------------------------------
# INITIALIZE SESSION STATE
# ----------------------------------------
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_role' not in st.session_state:
    st.session_state.user_role = None

if 'tasks' not in st.session_state:
    st.session_state.tasks = pd.DataFrame(columns=['Task ID', 'Campaign Objective', 'Reward', 'Status'])
    st.session_state.tasks.loc[0] = ['CMP-1001', 'Share Hackathon Registration in 3 CUSAT WhatsApp Groups', '50 Pts', 'Active']
    st.session_state.tasks.loc[1] = ['CMP-1002', 'Secure 5 confirmed sign-ups via personal referral link', '100 Pts', 'Active']

if 'leaderboard' not in st.session_state:
    st.session_state.leaderboard = pd.DataFrame({
        'Ambassador': ['Alice', 'Bob', 'Charlie'], 
        'Impact Points': [250, 120, 50],
        'Professional Tier': ['Community Lead 🌟', 'Campus Rep 📈', 'Initiate 🚀']
    })

# ----------------------------------------
# PREMIUM LOGIN SCREEN
# ----------------------------------------
if not st.session_state.logged_in:
    st.markdown('<p class="gradient-text">CampusConnect</p>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2rem; color: #555; margin-bottom: 40px;'>Structured. Scalable. Measurable Community-Led Marketing.</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        # Using a stylized container with a subtle border
        with st.container(border=True):
            st.markdown("<h3 style='text-align: center; color: #333;'>System Authentication</h3>", unsafe_allow_html=True)
            st.write("") # spacing
            role_selection = st.selectbox("Select Access Level", ["Ambassador Workspace", "Manager Dashboard"])
            username = st.text_input("Work Email / ID")
            password = st.text_input("Password", type="password")
            
            st.write("") # spacing
            if st.button("Authenticate & Enter Platform", use_container_width=True, type="primary"):
                if username and password: 
                    st.session_state.logged_in = True
                    st.session_state.user_role = role_selection
                    st.session_state.username = username
                    st.rerun() 
                else:
                    st.error("Authentication required. Please enter credentials.")
    st.stop() 

# ----------------------------------------
# MAIN PLATFORM UI
# ----------------------------------------
# Clean Top Navigation Bar equivalent
col_logo, col_logout = st.columns([4, 1])
with col_logo:
    st.markdown(f"### 🌐 CampusConnect | <span style='font-size: 1.2rem; font-weight: normal; color: #666;'>{st.session_state.user_role}</span>", unsafe_allow_html=True)
with col_logout:
    if st.button("Secure Logout", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.user_role = None
        st.rerun()
