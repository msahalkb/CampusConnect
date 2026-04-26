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

st.divider()

# ----------------------------------------
# MANAGER DASHBOARD (SaaS Style)
# ----------------------------------------
if st.session_state.user_role == "Manager Dashboard":
    
    # Hero Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Active Ambassadors", "12", "High Retention")
    col2.metric("Campaigns Completed", "45", "+10 this week")
    col3.metric("Total Referrals", "124", "Excellent ROI")
    col4.metric("Pending Verifications", "3", "Action Required")
    
    st.write("")
    st.write("")
    
    # Modern Tabbed Interface
    tab1, tab2 = st.tabs(["📊 Campaign Deployment & Tracking", "🏆 Ambassador Leaderboard"])
    
    with tab1:
        colA, colB = st.columns([1.5, 2])
        with colA:
            with st.container(border=True):
                st.subheader("Deploy New Campaign")
                desc = st.text_area("Task Objective (e.g., Promote IEEE workshop on LinkedIn)")
                points = st.slider("Reward Value (Points)", min_value=10, max_value=500, step=10, value=50)
                
                if st.button("🚀 Launch to Cohort", type="primary", use_container_width=True):
                    if desc:
                        new_task = pd.DataFrame([{
                            'Task ID': f"CMP-{random.randint(1000,9999)}", 
                            'Campaign Objective': desc, 
                            'Reward': f"{points} Pts", 
                            'Status': 'Active'
                        }])
                        st.session_state.tasks = pd.concat([st.session_state.tasks, new_task], ignore_index=True)
                        st.toast('Campaign deployed successfully to all ambassadors!', icon='✅')
                    else:
                        st.error("Please provide a task objective.")

        with colB:
            st.subheader("Live Campaign Tracker")
            st.dataframe(st.session_state.tasks, use_container_width=True, hide_index=True)
            
    with tab2:
        st.subheader("Global Cohort Leaderboard")
        st.dataframe(
            st.session_state.leaderboard.sort_values(by='Impact Points', ascending=False).reset_index(drop=True), 
            use_container_width=True,
            hide_index=True
        )

# ----------------------------------------
# AMBASSADOR WORKSPACE (SaaS Style)
# ----------------------------------------
elif st.session_state.user_role == "Ambassador Workspace":
    
    # Personalized Hero Section
    st.markdown(f"<h2>Welcome back, <span style='color: #0056b3;'>{st.session_state.username}</span></h2>", unsafe_allow_html=True)
    
    st.markdown("**Your Professional Growth Track**")
    st.progress(65, text="Tier Progress: Campus Rep 📈 (35 Points away from Community Lead 🌟)")
    st.write("")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Impact Points", "165", "Top 15% of Cohort")
    col2.metric("Activity Streak", "4 Weeks", "High Consistency")
    col3.metric("Current Tier", "Campus Rep", "1 Promotion Earned")
    
    st.write("")
    st.write("")
    
    tab1, tab2 = st.tabs(["📋 Active Campaigns", "🏆 Global Leaderboard"])
    
    with tab1:
        colA, colB = st.columns([2, 1.5])
        with colA:
            st.subheader("Action Center")
            active_quests = st.session_state.tasks[st.session_state.tasks['Status'] == 'Active']
            if active_quests.empty:
                st.info("All caught up. Excellent work.")
            else:
                st.dataframe(active_quests, use_container_width=True, hide_index=True)
                
        with colB:
            with st.container(border=True):
                st.subheader("Automated Verification")
                st.markdown("<span style='font-size: 0.9rem; color: #666;'>Upload proof of completion for instant AI processing.</span>", unsafe_allow_html=True)
                
                task_id = st.selectbox("Select Task ID to Verify", active_quests['Task ID'].tolist() if not active_quests.empty else ["No Active Tasks"])
                proof_data = st.file_uploader("Upload Document / Screenshot", type=['png', 'jpg', 'jpeg'])
                
                if st.button("Run AI Verification Engine", type="primary", use_container_width=True):
                    if task_id != "No Active Tasks" and proof_data:
                        with st.spinner("Analyzing document parameters..."):
                            time.sleep(2) 
                            st.toast(f'Verification Successful! Points credited for {task_id}.', icon='✨')
                    else:
                        st.error("Please provide your proof document.")

    with tab2:
        st.subheader("Cohort Leaderboard")
        st.dataframe(
            st.session_state.leaderboard.sort_values(by='Impact Points', ascending=False).reset_index(drop=True), 
            use_container_width=True,
            hide_index=True
        )
