import streamlit as st

st.set_page_config(page_title="Clipboard Health Analysis", layout="wide")



# # Add all the pages
# st.sidebar.title("Navigation")
# st.sidebar.markdown("""
# - [Home](#home)
# - [Data Exploration](#exploration)
# - [Predictive Modeling](#modeling)
# - [Recommendations](recommendations.py)
# """)
# Import pages
import home
import exploration 
import modeling
import recommendations

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
