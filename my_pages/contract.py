import streamlit as st
from datetime import datetime, date
from database import utils as ut

def add():
    # Contract Manager page
    st.title("Add Contract")

    # Fetch owned equipment
    equipment_options = ut.get_equip()

    with st.form("contract_form"):
        contract_name = st.text_input("Contract Name", max_chars=100)
        selected_equipment = st.multiselect("Select Equipment", options=list(equipment_options.values()))
        start_date = st.date_input("Start Date", value=date.today())
        end_date = st.date_input("End Date", value=date.today())
        charges = st.number_input("Charges (INR)", min_value=0.0, step=1.0)

        # Submit button
        submitted = st.form_submit_button("Add Contract")

        # Handle form submission
        if submitted:
            if not contract_name or not selected_equipment:
                st.error("Contract Name and at least one equipment selection are required.")
            else:
                equipment_ids = ",".join(selected_equipment)
                ut.add_contract(contract_name, equipment_ids, start_date, end_date, charges)
                st.success(f"Contract '{contract_name}' added successfully!")
