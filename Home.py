# this file added with compatible modules and codes

import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Registering events and analyzing participant data")

col1, col2 = st.columns(2)

with col1:
    if st.button("Register for an event", type="primary", use_container_width=True):
        st.switch_page("pages/Event.py")

with col2:
    if st.button("View results", type="secondary", use_container_width=True):
        st.switch_page("pages/Result.py")