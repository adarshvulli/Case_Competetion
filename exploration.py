import streamlit as st
import pandas as pd
import plotly.express as px

def app():
    st.title("Data Exploration")
    
    # Load data
    data = pd.read_csv("problems_we_tackle_data.csv")
    data['CANCELED'] = data['CANCELED_AT'].notnull()
    data['CLAIMED'] = data['CLAIMED_AT'].notnull()
    data['SHIFT_AGE'] = (pd.to_datetime(data['SHIFT_START_AT']) - pd.to_datetime(data['SHIFT_CREATED_AT'])).dt.total_seconds() / 3600
    data['DURATION_BIN'] = pd.cut(data['DURATION'], bins=[0, 4, 8, 12, 16], labels=["0-4", "4-8", "8-12", "12-16"])
    
    # Dataset Overview
    st.subheader("Dataset Overview")
    st.write("Explore the structure and sample of the dataset below:")
    st.dataframe(data.head(10))
    st.write("""
        **Inference**: 
        - The dataset contains 10000 rows and 14 columns, with each row representing a shift.
        - The columns include shift details like start time, duration, pay rate, and status.
    """)
    describe = data.describe()
    st.write(describe)
    st.markdown("---")  # Divider
    
    # Interactive Pay Rate Distribution
    st.subheader("1. Interactive Pay Rate Distribution")
    st.write("Adjust the bin size to see how pay rates are distributed.")
    bin_size = st.slider("Bin Size", 5, 50, 20, key="bin_size")
    fig = px.histogram(data, x="RATE", nbins=bin_size, title="Pay Rate Distribution")
    st.plotly_chart(fig)
    st.write("""
        **Inference**: 
        - The distribution shows a concentration of pay rates between $ 20 and $ 25, 
          which are the most common offered rates. 
        - Higher pay rates above $30 are rare and may influence worker decisions.
    """)
    st.markdown("---")  # Divider
    
    # Cancellations by Timeslot
    st.subheader("2. Cancellations by Timeslot")
    st.write("Analyze how cancellations are distributed across different timeslots.")
    fig = px.bar(data.groupby('SLOT')['CANCELED'].mean().reset_index(), 
                 x='SLOT', y='CANCELED', title="Cancellation Rates by Timeslot")
    st.plotly_chart(fig)
    st.write("""
        **Inference**: 
        - Cancellation rates are highest for overnight (noc) shifts, possibly due to worker fatigue or scheduling conflicts. 
        - Morning and evening shifts show similar and lower cancellation rates.
    """)
    st.markdown("---")  # Divider
    
    # Shift Duration Analysis
    st.subheader("3. Shift Duration vs. Cancellations")
    st.write("Explore cancellation rates for shifts of different durations.")
    fig = px.bar(data.groupby('DURATION_BIN')['CANCELED'].mean().reset_index(), 
                 x='DURATION_BIN', y='CANCELED', title="Cancellation Rates by Shift Duration")
    st.plotly_chart(fig)
    st.write("""
        **Inference**: 
        - Shorter shifts (0-4 hours) have higher cancellation rates, likely due to low worker interest in short-duration commitments.
        - Longer shifts beyond 12 hours have very low cancellation rates, possibly due to their limited occurrence.
    """)
    st.markdown("---")  # Divider
    
    # Shift Aging Analysis
    st.subheader("4. Shift Aging and Cancellations")
    st.write("Explore how the time between shift creation and start affects cancellations.")
    data['SHIFT_AGE_BIN'] = pd.cut(data['SHIFT_AGE'], bins=[0, 24, 72, 168, 336, 720], 
                                   labels=["<1 day", "1-3 days", "3-7 days", "1-2 weeks", "2+ weeks"])
    fig = px.bar(data.groupby('SHIFT_AGE_BIN')['CANCELED'].mean().reset_index(), 
                 x='SHIFT_AGE_BIN', y='CANCELED', title="Cancellation Rates by Shift Age")
    st.plotly_chart(fig)
    st.write("""
        **Inference**: 
        - Shifts created 3–7 days or 1–2 weeks in advance have the highest cancellation rates, 
          likely due to workers overcommitting when shifts are posted far in advance.
        - Shifts posted less than 1 day before the start time show the lowest cancellation rates.
    """)
    st.markdown("---")  # Divider
    
    # Timeslot and Pay Rate Interaction
    st.subheader("5. Pay Rate by Timeslot")
    st.write("Analyze how average pay rates vary across different timeslots.")
    fig = px.bar(data.groupby('SLOT')['RATE'].mean().reset_index(), 
                 x='SLOT', y='RATE', title="Average Pay Rate by Timeslot")
    st.plotly_chart(fig)
    st.write("""
        **Inference**: 
        - Overnight (noc) shifts tend to have slightly higher average pay rates, 
          likely due to their lower popularity among workers. 
        - Morning (am) and evening (pm) shifts offer similar pay rates.
    """)
    st.markdown("---")  # Divider
    
    st.title("Seasonal Worker Patterns")

    st.write("""
    This analysis explores seasonal patterns in worker behavior, focusing on shift claims and completions across different days, 
    months, and seasons. Understanding these patterns helps optimize shift postings and engagement strategies.
    """)

    # Load data
    data = pd.read_csv("/Users/jarvis/Library/CloudStorage/OneDrive-IndianaUniversity/sem3/iuinnovates challenge/problems_we_tackle_data.csv")
    data['CLAIMED_AT'] = pd.to_datetime(data['CLAIMED_AT'])
    data['SHIFT_START_AT'] = pd.to_datetime(data['SHIFT_START_AT'])
    data['IS_VERIFIED'] = data['IS_VERIFIED'].astype(int)

    # Extract temporal features
    data['Day of Week'] = data['CLAIMED_AT'].dt.day_name()
    data['Month'] = data['CLAIMED_AT'].dt.month_name()
    data['Hour of Day'] = data['CLAIMED_AT'].dt.hour

    ### Day of Week Analysis ###
    st.subheader("1. Shift Claims by Day of Week")
    claims_by_day = data.groupby('Day of Week')['IS_VERIFIED'].mean().reindex([
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ])
    fig1 = px.bar(claims_by_day, x=claims_by_day.index, y=claims_by_day.values,
                  labels={'x': 'Day of Week', 'y': 'Average Shift Completion Rate'},
                  title="Average Shift Completion Rate by Day of Week")
    st.plotly_chart(fig1)
    st.write("""
    **Inference**:
    - Engagement tends to vary by day of the week, with higher completion rates on specific days.
    - Weekends may show distinct patterns due to worker availability or preferences.
    """)

    ### Month Analysis ###
    st.subheader("2. Shift Claims by Month")
    claims_by_month = data.groupby('Month')['IS_VERIFIED'].mean().reindex([
        "January", "February", "March", "April", "May", "June", "July",
        "August", "September", "October", "November", "December"
    ])
    fig2 = px.bar(claims_by_month, x=claims_by_month.index, y=claims_by_month.values,
                  labels={'x': 'Month', 'y': 'Average Shift Completion Rate'},
                  title="Average Shift Completion Rate by Month")
    st.plotly_chart(fig2)
    st.write("""
    **Inference**:
    - Certain months may exhibit seasonal peaks (e.g., summer months or holiday periods).
    - Low engagement periods could align with worker availability or external factors like holidays.
    """)

    ### Hourly Analysis ###
    st.subheader("3. Shift Claims by Hour of Day")
    claims_by_hour = data.groupby('Hour of Day')['IS_VERIFIED'].mean()
    fig3 = px.line(claims_by_hour, x=claims_by_hour.index, y=claims_by_hour.values,
                   labels={'x': 'Hour of Day', 'y': 'Average Shift Completion Rate'},
                   title="Average Shift Completion Rate by Hour of Day")
    st.plotly_chart(fig3)
    st.write("""
    **Inference**:
    - Worker engagement peaks during specific hours, likely aligning with their availability.
    - Overnight hours may show lower engagement, requiring special incentives for those shifts.
    """)

    ### Combined Heatmap ###
    st.subheader("4. Heatmap of Shift Claims by Day and Hour")
    heatmap_data = data.groupby(['Day of Week', 'Hour of Day'])['IS_VERIFIED'].mean().unstack()
    fig4 = px.imshow(heatmap_data, 
                     labels={'x': 'Hour of Day', 'y': 'Day of Week', 'color': 'Completion Rate'},
                     title="Heatmap of Shift Completion Rates by Day and Hour",
                     aspect="auto")
    st.plotly_chart(fig4)
    st.write("""
    **Inference**:
    - The heatmap shows granular patterns of engagement by day and hour.
    - Use these insights to adjust shift postings to align with high-engagement periods.
    """)

    st.markdown("---")
    st.subheader("Recommendations")
    st.write("""
    Based on the observed patterns:
    - **Target High-Engagement Periods**: Focus shift postings on days and hours with peak engagement.
    - **Boost Low-Engagement Times**: Offer incentives or bonuses for shifts during low-engagement periods.
    - **Seasonal Adjustments**: Prepare for seasonal peaks or dips by increasing worker outreach or adjusting shift attributes.
    - **Monitor Trends**: Regularly analyze new data to identify changes in worker behavior over time.
    """)

