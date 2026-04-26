# 🚀 CampusConnect | The Ambassador Growth Engine

**Built for the AICore Connect Hackathon**

Organizations rely on Campus Ambassadors to build brand presence, yet most programs fail silently due to scattered tools, manual tracking, and zero gamification. Valuable ambassadors disengage, and organizations lose the ability to measure ROI. 

**CampusConnect** solves this. It is a centralized SaaS platform where organizations onboard ambassadors, deploy campaigns, and track engagement—and where ambassadors earn tiered recognition for every contribution they make.

### 🌐 [Click Here to View the Live Hosted Platform].(https://campusconnecter.streamlit.app/)
### 📹 [Click Here to Watch the 3-Minute Demo Video](https://youtu.be/dQ6jTeRxeeQ)

---

## 🏆 How We Hit the Evaluation Criteria

### 1. User Experience (25%) + Bonus
We ditched the standard data-script look and built a premium, responsive SaaS interface using custom CSS injections. It features tiered progress bars, sleek toast notifications, and modern tabbed navigation. **Bonus achieved:** The platform is fully hosted and publicly accessible via Streamlit Community Cloud for frictionless, zero-installation access.

### 2. Impact (20%)
Managers no longer need to check WhatsApp groups and spreadsheets. They can deploy a campaign to their entire cohort and view real-time ROI metrics, leaderboards, and pending verifications in under 60 seconds.

### 3. Innovation (20%)
We replaced manual task checking with an **Automated AI Verification Engine**. Ambassadors upload screenshots of their WhatsApp forwards or LinkedIn posts, and the system simulates an AI vision scan to auto-verify the proof and instantly credit Impact Points. 

### 4. Technical Execution (20%)
Built entirely in Python, utilizing Streamlit for rapid frontend deployment and Pandas for session-state data management. The code is structured, clean, and entirely self-contained.

---

## 💻 Features at a Glance

**👑 Manager Dashboard (Admin Console)**
* **Real-time Metrics:** Track total referrals, active ambassadors, and circulating points.
* **Instant Deployment:** Launch new campaigns (e.g., "Share Hackathon Flyer") instantly.
* **Global Leaderboard:** Automatically identify top performers for internships or rewards.

**🛡️ Ambassador Workspace (Player Hub)**
* **Professional Gamification:** Move up the ranks (Initiate 🚀 → Campus Rep 📈 → Community Lead 🌟) based on completed tasks.
* **Action Center:** View pending objectives and their point values clearly.
* **Frictionless Proof Submission:** Direct image upload for immediate task verification.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Frontend Framework:** Streamlit (with Custom CSS)
* **Data Handling:** Pandas
* **Deployment:** Streamlit Community Cloud

---

## ⚙️ How to Run Locally

If you prefer to run the application on your local machine rather than using the hosted link:

1. **Clone the repository:**
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME.git)
cd YOUR_REPO_NAME
```

2. **Install the dependencies:**
```bash
pip install -r requirements.txt
```

3. **Boot the server:**
```bash
streamlit run app.py
```

*(Note: To bypass the login screen during the hackathon evaluation, you may enter any alphanumeric characters into the username and password fields).*
