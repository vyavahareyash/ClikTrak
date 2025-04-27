import streamlit as st
from db_utils import *

# display all contracts
def display_contracts():
    contracts = get_all_contracts()
    if contracts:
        for contract in contracts:
            st.subheader(f"Contract ID: {contract['id']}")
            st.write(f"Contract Name: {contract['contract_name']}")
            st.write(f"Total Amount: {contract['total_amount']}")
            st.write("Tasks:")
            for task in contract["tasks"]:
                st.write(f"- {task['task']} (Amount: {task['amount']})")
            st.write("Tags:")
            for tag in contract["tags"]:
                st.write(f"- {tag}")
    else:
        st.write("No contracts found.")
        
display_contracts()