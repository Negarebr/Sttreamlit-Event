import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title of the app
st.title("Result")

# Connect to Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Read data from the specified worksheet
df = conn.read(worksheet="Sheet1", usecols=[0, 1, 2], ttl=5).dropna(how="all")

# Display all the data in the dataframe
# st.dataframe(df, hide_index=True, use_container_width=True)

# Check if dataframe is not empty
if not df.empty:
    st.header("List of Participants")

    # Display the total number of participants
    len = df['Name'].__len__()
    st.subheader(f"_Total number of participants:_ {len}")
    
    # Display the list of participants
    st.dataframe(df, hide_index=True, column_order=["Name"])

    # Data analysis and visualization
    st.header("Data Analysis")

    if 'Event' in df.columns: # Check if 'Event' column exists
        Event_counts = df['Event'].value_counts()
        st.bar_chart(data=Event_counts, use_container_width=True,)

else:
    st.write("No data available.")
