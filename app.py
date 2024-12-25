import streamlit as st
from my_pages import equipment as eq, home

def main():
    
    st.set_page_config(
            page_title="ClikTrak",
        )
    
    page = st.sidebar.radio("Go to:",["Home", "Add Equipment", "Remove Equipment"])
    
    if page == "Home":
        home.main()
    elif page == "Add Equipment":
        eq.add()
    elif page == "Remove Equipment":
        eq.remove()

if __name__ == '__main__':
    main()