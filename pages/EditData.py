import streamlit as st
from db_utils import *

st.title("Contract Management System")

tags = get_tags()

# Add new tag
new_tag = st.text_input("Add a new tag")
if st.button("Add Tag"):
    if new_tag and new_tag not in tags:
        add_tag(new_tag)
        st.success(f"Tag '{new_tag}' added.")
    elif new_tag:
        st.warning(f"Tag '{new_tag}' already exists.")
        
# Delete tag
tag_to_delete = st.selectbox("Delete an existing tag", options=tags)
if st.button("Delete Tag"):
    if delete_tag(tag_to_delete):
        st.success(f"Tag '{tag_to_delete}' deleted.")
    else:
        st.error(f"Tag '{tag_to_delete}' not found.")
        
# add task
new_task = st.text_input("Add a new task")
if st.button("Add Task"):
    if new_task and new_task not in get_tasks():
        add_task(new_task)
        st.success(f"Task '{new_task}' added.")
    elif new_task:
        st.warning(f"Task '{new_task}' already exists.")