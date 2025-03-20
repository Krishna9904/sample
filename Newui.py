import streamlit as st
import time

st.set_page_config(layout="wide")  # Utilize full page width

# Bank of America SVG Logo
logo_svg = """
    <img src="https://upload.wikimedia.org/wikipedia/commons/2/2c/Bank_of_America_logo.svg"
    width="150" style="vertical-align: middle;"/>
"""

# Custom Navigation Bar
st.markdown(
    f"""
    <style>
        body {{
            background: linear-gradient(to bottom, #ffffff, #f0f0f0);
        }}
        .navbar {{
            background-color: white;
            padding: 15px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            display: flex;
            align-items: center;
            font-size: 20px;
            font-weight: bold;
        }}
        .navbar span {{
            margin-left: 15px;
        }}
    </style>
    <div class="navbar">{logo_svg} <span>Job Monitoring and Resource Allocation Dashboard</span></div>
    """,
    unsafe_allow_html=True
)

# Layout for Running Sessions and Projects
col1, col2 = st.columns([1, 1])

# Running Sessions (Left Side)
with col1:
    st.subheader("🖥️ Running Sessions")

    # Dummy session data (No API Call)
    jobs = [
        {"name": "Session 1", "status": "Running"},
        {"name": "Session 2", "status": "Queued"},
        {"name": "Session 3", "status": "Completed"}
    ]
    
    # Display sessions as tiles
    for job in jobs:
        with st.container():
            st.markdown(f"<div style='padding: 10px; border: 1px solid #ddd; border-radius: 10px; margin-bottom: 10px;'>"
                        f"<strong>{job['name']}</strong><br>Status: {job['status']}</div>",
                        unsafe_allow_html=True)
    
    # Launch New Session Button (No API Call)
    if st.button("🚀 Launch New Session"):
        with st.expander("New Session Parameters", expanded=True):
            num_gpus = st.number_input("🎛️ Number of GPUs", min_value=1, max_value=8, step=1)
            memory = st.number_input("💾 Memory (GB)", min_value=1, max_value=128, step=1)
            duration = st.number_input("⏳ Session Duration (hours)", min_value=1, max_value=24, step=1)
            submitted = st.button("✅ Submit Request")
            if submitted:
                st.success("🎉 Session requested successfully!")

# Projects Section (Right Side)
with col2:
    st.subheader("📂 Projects")

    # Dummy project data (No API Call)
    projects = [
        {"name": "Project A", "description": "Data analysis project"},
        {"name": "Project B", "description": "Machine learning pipeline"},
        {"name": "Project C", "description": "Web app development"}
    ]
    
    # Display projects as tiles
    for project in projects:
        with st.container():
            st.markdown(f"<div style='padding: 10px; border: 1px solid #ddd; border-radius: 10px; margin-bottom: 10px;'>"
                        f"<strong>{project['name']}</strong><br>{project['description']}</div>",
                        unsafe_allow_html=True)
    
    # Launch New Project Button (No API Call)
    if st.button("➕ Launch New Project"):
        with st.expander("New Project Parameters", expanded=True):
            project_name = st.text_input("📌 Project Name")
            project_desc = st.text_area("📝 Description")
            submitted = st.button("✅ Create Project")
            if submitted:
                st.success(f"🎉 Project '{project_name}' created successfully!")

# Auto-refresh every 10 seconds
st.experimental_rerun() if time.sleep(10) else None
