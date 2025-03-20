import streamlit as st
import requests
import time

API_URL = "https://example.com/jobs"  # Replace with your actual API endpoint

st.set_page_config(layout="wide")  # Utilize full page width

# Navigation Bar
st.markdown(
    """
    <style>
        .navbar {
            background-color: white;
            padding: 10px;
            color: black;
            font-size: 20px;
            font-weight: bold;
            text-align: left;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
    </style>
    <div class="navbar">🚀 Job Monitoring and Resource Allocation Dashboard</div>
    """,
    unsafe_allow_html=True
)

# Layout for Running Sessions and Projects
col1, col2 = st.columns([1, 1])

# Running Sessions (Left Side)
with col1:
    st.subheader("🖥️ Running Sessions")
    
    def get_running_jobs():
        try:
            response = requests.get(API_URL)
            if response.status_code == 200:
                return response.json()
            else:
                return []
        except Exception as e:
            st.error(f"Error fetching jobs: {e}")
            return []
    
    jobs = get_running_jobs()
    dummy_jobs = [
        {"name": "Session 1", "status": "Running"},
        {"name": "Session 2", "status": "Queued"},
        {"name": "Session 3", "status": "Completed"}
    ]
    jobs = jobs if jobs else dummy_jobs  # Use dummy jobs if API returns none
    
    for job in jobs:
        with st.container():
            st.markdown(f"**{job['name']}**")
            st.text(f"Status: {job['status']}")
    
    # Launch New Session Button
    if st.button("🚀 Launch New Session"):
        with st.expander("New Session Parameters", expanded=True):
            num_gpus = st.number_input("🎛️ Number of GPUs", min_value=1, max_value=8, step=1)
            memory = st.number_input("💾 Memory (GB)", min_value=1, max_value=128, step=1)
            duration = st.number_input("⏳ Session Duration (hours)", min_value=1, max_value=24, step=1)
            submitted = st.button("✅ Submit Request")
            if submitted:
                session_request = {
                    "num_gpus": num_gpus,
                    "memory": memory,
                    "duration": duration,
                }
                try:
                    response = requests.post("https://example.com/request-session", json=session_request)  # Replace API endpoint
                    if response.status_code == 200:
                        st.success("🎉 Session requested successfully!")
                    else:
                        st.error("❌ Failed to request session.")
                except Exception as e:
                    st.error(f"⚠️ Error requesting session: {e}")

# Projects Section (Right Side, Occupies 50% of Page)
with col2:
    st.subheader("📂 Projects")
    projects = [
        {"name": "Project A", "description": "Data analysis project"},
        {"name": "Project B", "description": "Machine learning pipeline"},
        {"name": "Project C", "description": "Web app development"}
    ]
    
    for project in projects:
        with st.container():
            st.markdown(f"**{project['name']}**")
            st.text(f"{project['description']}")
    
    # Launch New Project Button
    if st.button("➕ Launch New Project"):
        with st.expander("New Project Parameters", expanded=True):
            project_name = st.text_input("📌 Project Name")
            project_desc = st.text_area("📝 Description")
            submitted = st.button("✅ Create Project")
            if submitted:
                st.success(f"🎉 Project '{project_name}' created successfully!")

# Auto-refresh every 10 seconds
st.experimental_rerun() if time.sleep(10) else None
