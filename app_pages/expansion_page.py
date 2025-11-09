import streamlit as st

def show():
    st.markdown("<h2 class='section-title'>Potential Expansions</h2>", unsafe_allow_html=True)
    st.markdown(
        """
<ul class="bullet">
  <li>Predict high-risk time windows per borough and premise type.</li>
  <li>Integrate 311, weather, and transit data for richer insights.</li>
  <li>Automate updates with the latest NYPD data releases.</li>
</ul>
""",
        unsafe_allow_html=True,
    )
