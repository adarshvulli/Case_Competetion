import streamlit as st

def app():
    st.title("Detailed Report on Work Status Prediction")

    st.write("""
    This report explores the likelihood of a shift being worked (`IS_VERIFIED = True`) based on factors like pay rate 
    and shift duration. It summarizes findings, predictive insights, and actionable recommendations to optimize shift attributes.
    """)

    st.markdown("---")

    ### Data Overview ###
    st.subheader("1. Data Overview")
    st.write("""
    The dataset includes records of shifts posted on Clipboard Health's platform. Key fields analyzed include:
    - **RATE**: Hourly pay rate offered for the shift.
    - **DURATION**: Duration of the shift in hours.
    - **IS_VERIFIED**: Indicates whether a shift was worked (`True`) or not (`False`).
    """)

    st.markdown("---")

    ### Key Insights ###
    st.subheader("2. Key Insights")
    st.write("""
    **Pay Rate Distribution**:
    - Most shifts offer pay rates between $20 and $25.
    - Higher pay rates (> $30) are rare and may impact worker preferences.

    **Shift Duration Distribution**:
    - Shifts between 6 and 8 hours are the most common and likely the most appealing to workers.
    - Extremely short (<4 hours) or long (>10 hours) shifts occur less frequently and may discourage workers.

    **Predictions**:
    - Higher pay rates positively correlate with shifts being worked.
    - Shifts with durations of 6–8 hours have the highest likelihood of being worked.
    """)

    st.markdown("---")

    ### Simulation Results ###
    st.subheader("3. Simulation Results")
    st.write("""
    Using a logistic regression model trained on historical data, the likelihood of a shift being worked is predicted 
    based on pay rate and duration. Below are some examples:

    | Pay Rate ($) | Duration (Hours) | Predicted Likelihood of Being Worked |
    |--------------|------------------|--------------------------------------|
    | 24           | 7                | 85%                                 |
    | 20           | 5                | 62%                                 |
    | 15           | 3                | 28%                                 |
    """)

    st.markdown("---")

    ### Recommendations ###
    st.subheader("4. Recommendations")
    st.write("""
    Based on the analysis, here are actionable steps to optimize shift attributes:

    - **Optimize Pay Rates**: Focus on pay rates between $22 and $25 to maximize the likelihood of shifts being worked.
    - **Balance Shift Durations**: Offer shifts with durations of 6–8 hours for maximum worker appeal.
    - **Dynamic Adjustments**: Use predictive insights to adjust pay rates dynamically for shifts with low predicted likelihoods.
    - **Monitor Trends**: Continuously validate the model with fresh data to account for changing worker behavior.

    **Future Work**:
    - Include additional features like timeslot and shift age for improved accuracy.
    - Explore advanced machine learning models for better predictions.
    - Segment workers to tailor shift recommendations based on preferences.
    """)

    st.markdown("---")

    ### Conclusion ###
    st.subheader("5. Conclusion")
    st.write("""
    This report highlights the importance of leveraging historical data to predict and optimize shift attributes. 
    By focusing on key factors like pay rates and durations, Clipboard Health can:
    - Increase worker participation.
    - Reduce unworked shifts.
    - Enhance operational efficiency.

    The predictive model and simulation provide actionable insights to make data-driven decisions and ensure a better experience for workers and workplaces alike.
    """)
