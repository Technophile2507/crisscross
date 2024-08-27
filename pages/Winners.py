import streamlit as st
import pandas as pd
import time
import os

# Path to the Excel file
excel_file_path = './participants.xlsx'

# Function to load the data from the Excel file
@st.cache_data(ttl=60)
def load_data(file_path):
    df = pd.read_excel(file_path)
    winners_df = df[df['Verdict'] == 'Winner'].sort_values(by='Time Taken', ascending=True)
    return winners_df

# Function to get the last modified time of the file
def get_last_modified_time(file_path):
    return os.path.getmtime(file_path)

# Streamlit App
st.markdown("<h1 style='text-align: center; '>CrissCross Puzzle Winners Dashboard</h1>", unsafe_allow_html=True)


# Initialize
last_modified_time = get_last_modified_time(excel_file_path)

# Create a placeholder to dynamically update the content
placeholder = st.empty()

# Function to update the dashboard
def update_dashboard():
    with placeholder.container():
        winners_data = load_data(excel_file_path)
        
        # Display the latest winner on top
        st.subheader("🏆 Latest Winner")
        st.write(f"**Name:** {winners_data.iloc[0]['Name']}")
        st.write(f"**Mobile:** {winners_data.iloc[0]['Mobile']}")
        st.write(f"**Time Taken:** {winners_data.iloc[0]['Time Taken']} seconds")
        
        st.subheader("🎉 All Winners")
        st.dataframe(winners_data[['UID', 'Name', 'Mobile', 'Time Taken']])

# Initial dashboard update
update_dashboard()

# Keep checking for updates
while True:
    current_modified_time = get_last_modified_time(excel_file_path)
    
    if current_modified_time != last_modified_time:
        # Update dashboard if the file has been modified
        update_dashboard()
        last_modified_time = current_modified_time
    
    # Pause for a few seconds before checking again
    time.sleep(5)
    st.experimental_rerun()
