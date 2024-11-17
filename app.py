import streamlit as st
import home
import exploration 
import modeling
import recommendations

st.set_page_config(page_title="Clipboard Health Analysis", layout="wide")


# Create dictionary of pages
pages = {
    "Home": home.app,
    "Data Exploration": exploration.app,
    "Predictive Modeling": modeling.app,
    "Recommendations": recommendations.app
}

# Radio button for navigation
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Run selected page
pages[selection]()

