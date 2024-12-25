import streamlit as st
from database import utils
import pandas as pd
from datetime import datetime

def main():
    
    st.title('ClikTrak')
    
    st.header("Existing Equipment Records")
    
    with st.spinner("Fetching records..."):
        df = utils.get_owned_equipment()
    
        if len(df) != 0:
            date_addition = pd.to_datetime(df["Date addition"], format="%Y-%m-%d")
            df["Days Used"] = (datetime.now() - date_addition).dt.days
            st.dataframe(df)
        else:
            st.info("No records found.")
    
    st.header("Contracts")
    
    with st.spinner("Fetching records..."):
        df = utils.get_contracts()
    
        if len(df) != 0:
            st.dataframe(df)
        else:
            st.info("No records found.")

if __name__=='__main__':
    main()