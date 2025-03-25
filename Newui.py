import streamlit as st
import ssl
from streamlit.web.server.websocket_headers import _get_websocket_headers
from streamlit.web.server import Server

st.set_page_config(layout="wide")  # Utilize full page width

# SSL Configuration
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile="/path/to/your-cert.pem", keyfile="/path/to/your-key.key")

# Monkey patch Streamlit's Tornado Server to use SSL
def _patched_get_websocket_headers():
    return _get_websocket_headers()

Server._get_websocket_headers = _patched_get_websocket_headers

# Custom SVG Logo
logo_svg = """
    <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64">
        <path d="M24.695 23.8l5.624 2.392c-5.883 2.392-11.636 5.236-17.067 8.47-1.8-.97-3.75-1.875-5.624-2.715 5.495-3.103 11.184-5.883 17.067-8.145m-7.045-2.47A96.76 96.76 0 0 0 .002 28.897c1.745.646 3.556 1.358 5.3 2.07 5.43-3.168 11.184-5.883 17.13-8.016-1.552-.582-3.168-1.1-4.784-1.616" fill="#36c"/><path d="M37.56 23.596c-4.848-2.327-9.826-4.267-14.998-5.883-1.8.517-3.62 1.1-5.366 1.68 5.3 1.552 10.473 3.556 15.45 5.947 1.552-.582 3.232-1.228 4.913-1.745m7.823-2.4c-4.913-2.133-10.02-3.943-15.257-5.366a59.77 59.77 0 0 0-4.913 1.164c5.172 1.487 10.214 3.426 15.063 5.7 1.68-.517 3.426-1.034 5.107-1.487m12.67 4.254C45.64 29.608 34.07 35.556 23.596 43.055c2.586 1.616 5.172 3.297 7.693 5.107C41.18 40.34 52.17 33.745 64 28.832c-2.004-1.228-3.943-2.327-5.947-3.362m-8.533-4.072c-12.865 3.426-24.954 8.92-35.88 16.162 2.457 1.228 4.848 2.52 7.24 3.88 10.668-7.37 22.562-13.125 35.233-16.94a151.34 151.34 0 0 0-6.594-3.103" fill="#e2173e"/>
    </svg>
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
    
    # Dummy session data
    jobs = [
        {"name": "Session 1", "status": "Running"},
        {"name": "Session 2", "status": "Queued"},
        {"name": "Session 3", "status": "Completed"}
    ]
    
    for job in jobs:
        with st.container():
            st.markdown(f"<div style='padding: 10px; border: 1px solid #ddd; border-radius: 10px; margin-bottom: 10px;'>"
                        f"<strong>{job['name']}</strong><br>Status: {job['status']}</div>",
                        unsafe_allow_html=True)

# Projects Section (Right Side)
with col2:
    st.subheader("📂 Projects")
    
    # Dummy project data
    projects = [
        {"name": "Project A", "description": "Data analysis project"},
        {"name": "Project B", "description": "Machine learning pipeline"},
        {"name": "Project C", "description": "Web app development"}
    ]
    
    for project in projects:
        with st.container():
            st.markdown(f"<div style='padding: 10px; border: 1px solid #ddd; border-radius: 10px; margin-bottom: 10px;'>"
                        f"<strong>{project['name']}</strong><br>{project['description']}</div>",
                        unsafe_allow_html=True)

# Start Streamlit Server with SSL
if __name__ == "__main__":
    server = Server.instance()
    server.start(
        config_options={"server.enableCORS": False},
        ssl_context=ssl_context  # Enable SSL
    )



















import streamlit as st
import time

st.set_page_config(layout="wide")  # Utilize full page width

# Custom SVG Logo
logo_svg = """
    <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64">
        <path d="M24.695 23.8l5.624 2.392c-5.883 2.392-11.636 5.236-17.067 8.47-1.8-.97-3.75-1.875-5.624-2.715 5.495-3.103 11.184-5.883 17.067-8.145m-7.045-2.47A96.76 96.76 0 0 0 .002 28.897c1.745.646 3.556 1.358 5.3 2.07 5.43-3.168 11.184-5.883 17.13-8.016-1.552-.582-3.168-1.1-4.784-1.616" fill="#36c"/><path d="M37.56 23.596c-4.848-2.327-9.826-4.267-14.998-5.883-1.8.517-3.62 1.1-5.366 1.68 5.3 1.552 10.473 3.556 15.45 5.947 1.552-.582 3.232-1.228 4.913-1.745m7.823-2.4c-4.913-2.133-10.02-3.943-15.257-5.366a59.77 59.77 0 0 0-4.913 1.164c5.172 1.487 10.214 3.426 15.063 5.7 1.68-.517 3.426-1.034 5.107-1.487m12.67 4.254C45.64 29.608 34.07 35.556 23.596 43.055c2.586 1.616 5.172 3.297 7.693 5.107C41.18 40.34 52.17 33.745 64 28.832c-2.004-1.228-3.943-2.327-5.947-3.362m-8.533-4.072c-12.865 3.426-24.954 8.92-35.88 16.162 2.457 1.228 4.848 2.52 7.24 3.88 10.668-7.37 22.562-13.125 35.233-16.94a151.34 151.34 0 0 0-6.594-3.103" fill="#e2173e"/>
    </svg>
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
         .blur-button {{
            background: rgba(50, 118, 181, 1);
            backdrop-filter: blur(10px);
            border: none;
            padding: 10px 20px;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
            transition: 0.3s;
            color: white;
        }}
        .blur-button:hover {{
            background: rgba(50, 118, 181, 0.8);
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

    # Launch New Session Button (First Place)
    if st.button("🚀 Launch New Session", key="launch_session"):
        with st.expander("New Session Parameters", expanded=True):
            num_gpus = st.number_input("🎛️ Number of GPUs", min_value=1, max_value=8, step=1)
            memory = st.number_input("💾 Memory (GB)", min_value=1, max_value=128, step=1)
            duration = st.number_input("⏳ Session Duration (hours)", min_value=1, max_value=24, step=1)
            submitted = st.button("✅ Submit Request")
            if submitted:
                st.success("🎉 Session requested successfully!")
    
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

# Projects Section (Right Side)
with col2:
    st.subheader("📂 Projects")
    
    # Launch New Project Button (First Place)
    if st.button("➕ Launch New Project", key="launch_project"):
        with st.expander("New Project Parameters", expanded=True):
            project_name = st.text_input("📌 Project Name")
            project_desc = st.text_area("📝 Description")
            submitted = st.button("✅ Create Project")
            if submitted:
                st.success(f"🎉 Project '{project_name}' created successfully!")
    
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



import streamlit as st
import requests
import time

st.set_page_config(layout="wide")


logo_svg = """ <svg xmlns="http://www.w3.org/2000/svg" width="64" height="64">
        <path d="M24.695 23.8l5.624 2.392c-5.883 2.392-11.636 5.236-17.067 8.47-1.8-.97-3.75-1.875-5.624-2.715 5.495-3.103 11.184-5.883 17.067-8.145m-7.045-2.47A96.76 96.76 0 0 0 .002 28.897c1.745.646 3.556 1.358 5.3 2.07 5.43-3.168 11.184-5.883 17.13-8.016-1.552-.582-3.168-1.1-4.784-1.616" fill="#36c"/><path d="M37.56 23.596c-4.848-2.327-9.826-4.267-14.998-5.883-1.8.517-3.62 1.1-5.366 1.68 5.3 1.552 10.473 3.556 15.45 5.947 1.552-.582 3.232-1.228 4.913-1.745m7.823-2.4c-4.913-2.133-10.02-3.943-15.257-5.366a59.77 59.77 0 0 0-4.913 1.164c5.172 1.487 10.214 3.426 15.063 5.7 1.68-.517 3.426-1.034 5.107-1.487m12.67 4.254C45.64 29.608 34.07 35.556 23.596 43.055c2.586 1.616 5.172 3.297 7.693 5.107C41.18 40.34 52.17 33.745 64 28.832c-2.004-1.228-3.943-2.327-5.947-3.362m-8.533-4.072c-12.865 3.426-24.954 8.92-35.88 16.162 2.457 1.228 4.848 2.52 7.24 3.88 10.668-7.37 22.562-13.125 35.233-16.94a151.34 151.34 0 0 0-6.594-3.103" fill="#e2173e"/>
    </svg>
    
"""


st.markdown(
    f"""
    <style>
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

col1, col2 = st.columns([1, 1])


with col1:
    st.subheader("🖥️ Running Sessions")
    
    
    with st.expander("🚀 Launch New Session", expanded=False):
        num_gpus = st.number_input("🎛️ Number of GPUs", min_value=1, max_value=8, step=1)
        memory = st.number_input("💾 Memory (GB)", min_value=1, max_value=128, step=1)
        duration = st.number_input("⏳ Session Duration (hours)", min_value=1, max_value=24, step=1)
        
        if st.button("✅ Submit Request"):
            payload = {"num_gpus": num_gpus, "memory": memory, "duration": duration}
            response = requests.post("http://your-api-endpoint/start_session", json=payload)
            if response.status_code == 200:
                st.success("🎉 Session requested successfully!")
            else:
                st.error("❌ Failed to launch session. Please try again.")
    
   
    jobs = [
        {"name": "Session 1", "status": "Running"},
        {"name": "Session 2", "status": "Queued"},
        {"name": "Session 3", "status": "Completed"}
    ]
    
    for job in jobs:
        with st.container():
            st.markdown(f"<div style='padding: 10px; border: 1px solid #ddd; border-radius: 10px; margin-bottom: 10px;'>"
                        f"<strong>{job['name']}</strong><br>Status: {job['status']}</div>",
                        unsafe_allow_html=True)


with col2:
    st.subheader("📂 Projects")
    
    with st.expander("➕ Launch New Project", expanded=False):
        project_name = st.text_input("📌 Project Name")
        project_desc = st.text_area("📝 Description")
        
        if st.button("✅ Create Project"):
            payload = {"name": project_name, "description": project_desc}
            response = requests.post("http://your-api-endpoint/create_project", json=payload)
            if response.status_code == 200:
                st.success(f"🎉 Project '{project_name}' created successfully!")
            else:
                st.error("❌ Failed to create project. Please try again.")
    

    projects = [
        {"name": "Project A", "description": "Data analysis project"},
        {"name": "Project B", "description": "Machine learning pipeline"},
        {"name": "Project C", "description": "Web app development"}
    ]
    
    for project in projects:
        with st.container():
            st.markdown(f"<div style='padding: 10px; border: 1px solid #ddd; border-radius: 10px; margin-bottom: 10px;'>"
                        f"<strong>{project['name']}</strong><br>{project['description']}</div>",
                        unsafe_allow_html=True)





