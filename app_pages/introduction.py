import streamlit as st
from streamlit.components.v1 import html

def show():
    # ===== FONTS: change these numbers =====
    TITLE_PX        = 50   # main title
    TAGLINE_PX      = 24   # orange line
    PARA_PX         = 18   # paragraph text
    FOOTER_PX       = 16   # footer text
    # Optional scale for quick global resize (1.0 keeps as is)
    FONT_SCALE      = 1.00

    # ===== SPACING: change if you want =====
    PAD_TOP_PX      = 24
    PAD_X_PX        = 24
    PAD_BOT_PX      = 48
    PARA_LINE_HT    = 1.8
    PARA_GAP_PX     = 20
    FOOTER_TOP_PX   = 32
    CONTENT_MAX_W   = 1500

    # apply scale
    t_px = int(TITLE_PX   * FONT_SCALE)
    g_px = int(TAGLINE_PX * FONT_SCALE)
    p_px = int(PARA_PX    * FONT_SCALE)
    f_px = int(FOOTER_PX  * FONT_SCALE)

    intro_html = f"""
    <style>
      body {{
        margin: 0;
        font-family: 'Inter', 'Segoe UI', Helvetica, Arial, sans-serif;
        background: radial-gradient(circle at top left, #1b2330 0%, #0f141c 100%);
        color: #E4E8EE;
      }}

      .intro-container {{
        width: 96%;
        max-width: {CONTENT_MAX_W}px;
        margin: 40px auto;
        padding: {PAD_TOP_PX}px {PAD_X_PX}px {PAD_BOT_PX}px;
        background: transparent;
        text-align: center;
      }}

      .intro-title {{
        font-size: {t_px}px;
        font-weight: 600;
        color: #F5F7FA;
        margin: 0 0 16px 0;
        letter-spacing: 0.6px;
      }}

      .intro-tagline {{
        font-size: {g_px}px;
        color: #FFB86C;
        font-weight: 600;
        margin: 0 0 28px 0;
        line-height: 1.35;
      }}

      .intro-text {{
        font-size: {p_px}px;
        line-height: {PARA_LINE_HT};
        margin: 0 0 {PARA_GAP_PX}px 0;
        color: #DCE2EA;
        text-align: justify;
      }}

      .intro-footer {{
        margin-top: {FOOTER_TOP_PX}px;
        font-size: {f_px}px;
        color: #C8D3DF;
        border-top: 1px solid rgba(255,255,255,0.12);
        padding-top: 16px;
      }}

      .intro-footer h4 {{
        font-size: {max(f_px, 18)}px;
        color: #FFB86C;
        margin: 0 0 8px 0;
        font-weight: 600;
      }}

      /* small screens: keep things readable */
      @media (max-width: 900px) {{
        .intro-title  {{ font-size: {max(int(t_px*0.75), 36)}px; }}
        .intro-tagline{{ font-size: {max(int(g_px*0.85), 16)}px; }}
        .intro-text   {{ font-size: {max(int(p_px*0.95), 16)}px; }}
      }}
    </style>

    <div class="intro-container">
      <h1 class="intro-title">The NYC Crime Data Dashboard</h1>

      <p class="intro-tagline">
        Exploring New York City’s crime patterns through data, visualization, and insight.
      </p>

      <p class="intro-text">
        This dashboard uses publicly available data from the New York City Police Department (NYPD)
        to explore citywide crime trends. It helps users understand how incidents vary by
        crime type, borough, time of day, and location.
      </p>

      <p class="intro-text">
        For decades, New York City has shared detailed crime data through open data initiatives.
        This project builds on that transparency, making complex information accessible,
        interactive, and meaningful for residents, researchers, and policymakers.
      </p>

      <p class="intro-text">
        Our goal is to create a user friendly and visual platform that highlights key safety trends,
        supports data driven decision making, and fosters community awareness across all five boroughs.
      </p>

      <div class="intro-footer">
        <h4>Created by:</h4>
        <p>Colvin Kopram · Mohammed Al Muqsit · Mubashirul Islam · Saifuzzaman Tanim</p>
        <p class="intro-credit">CUNY Tech Prep · Data Science Fellowship · Fall 2025</p>
      </div>
    </div>
    """

    html(intro_html, height=860, scrolling=False)
