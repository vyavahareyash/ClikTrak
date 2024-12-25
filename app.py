import streamlit as st
from my_pages import equipment as eq, home, contract as cont

def main():
    
    st.set_page_config(
            page_title="ClikTrak",
        )
    
    page = st.sidebar.radio("Go to:",["Home", "Add Equipment", "Remove Equipment", "Add Contract"])
    
    if page == "Home":
        home.main()
    elif page == "Add Equipment":
        eq.add()
    elif page == "Remove Equipment":
        eq.remove()
    elif page == "Add Contract":
        cont.add()

if __name__ == '__main__':
    main()