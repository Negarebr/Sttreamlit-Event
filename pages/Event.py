import streamlit as st
from streamlit_gsheets import GSheetsConnection
from streamlit_card import card
import pandas as pd

# conn = st.connection("gsheets", type=GSheetsConnection)

st.title("Events")

st.write("### Select an Event")

col1, col2 = st.columns(2)

with col1:
    pyCard = card(
        title="Python Programming Event",
        text=["Learning Python with Streamlit and Google Sheets"," ", "Price: $100"],
        image="https://zemez.io/wp-content/uploads/2022/10/python-840x469.png",
        styles={
        "card": {
            "font-size": "16px",
            "text-shadow": "2px 2px #000000",
            "font-style": "italic"
            }
        },
    )

with col2:
    jsCard = card(
        title="JavaScript Programming Event",
        text=["Learning JavaScript with Streamlit and Google Sheets"," ", "Price: $150"],
        image="https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Unofficial_JavaScript_logo_2.svg/220px-Unofficial_JavaScript_logo_2.svg.png",
        styles={
        "card": {
            "font-size": "16px",
            "text-shadow": "2px 2px #000000",
            "font-style": "italic"
            }
        }
    )

event = "Not selected"
price = 0
if pyCard:
    event = "Python Programming Event"
    price = 100

if jsCard:
    event = "JavaScript Programming Event"
    price = 150



st.write("### Enter your details")
st.write(f"Selected Event: __{event}__")
if event == "Not selected":
    st.caption(":red[Please select an event from the list]")
name = st.text_input(label="Name:", placeholder="Enter your name")
if name == "":
    st.caption(":red[Please enter your name]")
email = st.text_input(label="Email address:", placeholder="Enter your email address")
if email == "":
    st.caption(":red[Please enter your email address]")
st.write(f"Price: __${price}__")

bcol1, bcol2 = st.columns(2)
with bcol1:
    submit = st.button("Submit", use_container_width=True, type="primary")
with bcol2:
    cancel = st.button("Cancel", use_container_width=True, type="secondary")



if submit:
    if event == "Not selected":
        st.error("Please select an event from the list.")
    if not name:
        st.error("Name is required.")
    if not email:
        st.error("Email is required.")

    if name and email and event != "Not selected":
        conn = st.connection("gsheets", type=GSheetsConnection)
        df = conn.read(worksheet="Sheet1", usecols=[0, 1, 2, 3]).dropna(how="all")
        df_email = df['Email'].tolist()

        # Check if email already exists
        if email in df_email:
            st.error("Email already exists in the survey.")
        else:
            data = {'Name': name, 'Email': email, 'Event': event, 'Price': price}
            
            temp_df = pd.DataFrame([data])
            updated_df = pd.concat([df, temp_df])
            conn.update(data=updated_df)
            
            # Display the information
            st.success(f"You are registered for the __{event}__ !")
            st.write(f"Name: {name}")
            st.write(f"Email: {email}")
            st.write(f"Event: {event}")
            st.write(f"Price: ${price}")
            st.page_link("Home.py", icon="🏠",label="Go back to Home")

if cancel:
    st.switch_page("Home.py")