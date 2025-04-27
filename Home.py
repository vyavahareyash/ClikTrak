from db_utils import *
import streamlit as st

st.title("Contract Management System")

# Contract Name 
contract_name = st.text_input("Contract Name")


# Tags selection
tags = get_tags()
selected_tags = st.multiselect("Select Tags", options=tags)

# Task Selection
available_tasks = get_tasks()

st.subheader("Add Task and Amount")

# Initialize session state to store added tasks
if "added_tasks" not in st.session_state:
    st.session_state.added_tasks = []

# Task input
task_col, amount_col, button_col = st.columns([3, 2, 1])
task_input = task_col.selectbox("Select Task", available_tasks, key="current_task_input")
amount_input = amount_col.number_input("Amount", min_value=0.0, step=100.0, key="current_amount_input")

tasks = []
total_amount = 0

# Add task to list
if button_col.button("Add Task"):
    if task_input and amount_input > 0:
        st.session_state.added_tasks.append({"task": task_input, "amount": amount_input})
        st.success(f"Task '{task_input}' with ₹{amount_input} added.")
        # Reset inputs by deleting keys
        del st.session_state["current_task_input"]
        del st.session_state["current_amount_input"]
    else:
        st.warning("Please select a task and enter a valid amount.")

# Display added tasks
if st.session_state.added_tasks:
    st.markdown("### Tasks Added")
    
    for idx, entry in enumerate(st.session_state.added_tasks, 1):
        st.write(f"{idx}. {entry['task']} — ₹{entry['amount']}")
        total_amount += entry["amount"]
    # Show total
    st.markdown(f"**Total Amount: ₹{total_amount}**")
else:
    st.info("No tasks added yet.")

tasks = st.session_state.added_tasks

contract = {
        "contract_name": contract_name,
        "tasks": tasks,
        "tags": selected_tags,
        "total_amount": total_amount,
    }

add_contract_button = st.button("Add Contract")
if add_contract_button:
    if contract_name and tasks and selected_tags:
        add_contract(contract)
        st.success("Contract added successfully!")
        # Reset the form
        st.session_state.added_tasks = []
        st.session_state.current_task_input = ""
        st.session_state.current_amount_input = 0.0
    else:
        st.warning("Please fill in all fields before adding a contract.")