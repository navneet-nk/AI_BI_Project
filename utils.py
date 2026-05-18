import streamlit as st

def download_dataset(filtered_data):

    csv = filtered_data.to_csv(
        index=False
    ).encode('utf-8')

    st.download_button(
        label="Download CSV File",
        data=csv,
        file_name='filtered_dataset.csv',
        mime='text/csv'
    )