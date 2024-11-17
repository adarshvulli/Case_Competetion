import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

def app():
    st.title("Modeling: Predictions and Patterns")
    
    # Load the data
    data = pd.read_csv("Case_Competetion/problems_we_tackle_data.csv")
    st.title("Work Status Prediction (IS_VERIFIED)")

    
    data['IS_VERIFIED'] = data['IS_VERIFIED'].astype(int)  # Convert to numeric for modeling

    # Train model
    X = data[['RATE', 'DURATION']].dropna()
    y = data['IS_VERIFIED'].dropna()
    model = LogisticRegression(random_state=42)
    model.fit(X, y)

    # User inputs for simulation
    st.subheader("Predict the likelihood of a shift being worked")
    pay_rate = st.slider("Select Pay Rate ($)", min_value=10, max_value=50, value=25, step=1)
    duration = st.slider("Select Duration (hours)", min_value=1, max_value=12, value=8, step=1)

    # Predict likelihood
    prediction_prob = model.predict_proba([[pay_rate, duration]])[0][1]  # Probability of IS_VERIFIED=True

    # Display result
    st.write(f"**Predicted Likelihood of the Shift Being Worked: {prediction_prob:.2%}**")

    # Explanation
    st.write("""
        **How this works:**
        - The model is trained on historical data to predict whether a worker will work a shift (`IS_VERIFIED`).
        - It uses factors like pay rate and duration to estimate the likelihood of future shifts being worked.
        - Use this simulation to adjust shift attributes (e.g., increase pay rates) and observe their impact.
    """)

    

    st.markdown("---")

    ### Clustering Analysis ###
    st.subheader("2. Clustering Shifts")
    st.write("""
    Shifts are grouped into clusters based on patterns in pay rate and duration. 
    This helps identify similar shifts and tailor strategies for each group.
    """)
    
    # Apply K-Means clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    data['Cluster'] = kmeans.fit_predict(X)
    
    # Visualize clusters
    fig = px.scatter(data, x='RATE', y='DURATION', color='Cluster', 
                     title="Clustering Shifts by Rate and Duration", 
                     labels={'RATE': 'Pay Rate ($)', 'DURATION': 'Shift Duration (hours)'})
    st.plotly_chart(fig)
    
    st.write("""
    **Inference**:
    - Each cluster represents a group of shifts with similar pay rates and durations.
    - Clusters can guide dynamic pricing or tailored incentives for different shift types.
    """)

    st.markdown("---")
    
   
