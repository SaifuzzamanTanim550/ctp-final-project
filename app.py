from pathlib import Path
import base64
import mimetypes
import streamlit as st

# Import custom pages
from app_pages import (
    introduction,
    overview,
    map_page,
    heatmap_page,
    timeseries_page,
    data_page,
    expansion_page,
)

# ───────────────── Helper ─────────────────
def img_to_data_uri(path: str) -> str:
    p = Path(path)
    if not p.exists():
        return ""
    mime = mimetypes.guess_type(p.name)[0] or "image/png"
    b64 = base64.b64encode(p.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{b64}"

# ───────────────── Page setup ─────────────────
st.set_page_config(page_title="CAMP | NYC Crime Dashboard", layout="wide")

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Header
st.markdown(
    """
<header class="site-header">
  <div class="site-header-inner">
    <div class="site-title">CAMP — Criminal Activity Mapping &amp; Predictor</div>
    <div class="site-subtitle">New York City Crime Dashboard</div>
  </div>
</header>
""",
    unsafe_allow_html=True,
)

# ───────────────── Sidebar ─────────────────
logo_uri = img_to_data_uri("image/ctp_logo.png")
st.sidebar.markdown(
    f"""
<div class="sidebar-header">
  {'<img src="'+logo_uri+'" class="profile-pic" alt="Logo"/>' if logo_uri else ''}
  <h2>CUNY Tech Prep Team</h2>
  <p>Data Science Cohort · Fall 2025</p>
</div>
""",
    unsafe_allow_html=True,
)

# ───────────────── Navigation ─────────────────
if "active_page" not in st.session_state:
    st.session_state.active_page = "Introduction"

def go(page: str):
    st.session_state.active_page = page
    st.experimental_rerun()

def nav_btn(label: str, page: str, icon: str = ""):
    if st.sidebar.button(f"{icon}  {label}", use_container_width=True, key=f"nav_{page}"):
        go(page)

nav_btn("Introduction", "Introduction", "🏙️")
nav_btn("Overview", "Overview", "📊")
nav_btn("Map", "Map", "🗺️")
nav_btn("Heat Map", "Heat Map", "🔥")
nav_btn("Time Series", "Time Series", "📈")
nav_btn("Data", "Data", "🧮")
nav_btn("Potential Expansions", "Potential Expansions", "🧭")

# ───────────────── Page routing ─────────────────
page = st.session_state.active_page

if page == "Introduction":
    introduction.show()
elif page == "Overview":
    overview.show()
elif page == "Map":
    map_page.show()
elif page == "Heat Map":
    heatmap_page.show()
elif page == "Time Series":
    timeseries_page.show()
elif page == "Data":
    data_page.show()
elif page == "Potential Expansions":
    expansion_page.show()
