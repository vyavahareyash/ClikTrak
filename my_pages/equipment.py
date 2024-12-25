import streamlit as st
from database import utils
from datetime import date
def add():
    
    st.title("Add Equipment")
    
    with st.form("equipment_form"):
        device_name = st.text_input("Device Name", max_chars=100)
        nickname = st.text_input("Nickname", max_chars=50)
        cost = st.number_input("Cost (INR)", min_value=0.0, step=1.0)
        condition = st.selectbox("Condition", ["new", "old"])
        date_add = st.date_input("Date of Addition", value=date.today())

        # Submit button
        submitted = st.form_submit_button("Add Equipment")

        # Handle form submission
        if submitted:
            if not device_name:
                st.error("Device Name is required.")
            else:
                with st.spinner("Adding record..."):
                    utils.add_equipment(device_name, nickname, cost, date_add, condition)
                st.success(f"Equipment '{device_name}' added successfully!")

def remove():
    st.title("Remove Equipment")
    
