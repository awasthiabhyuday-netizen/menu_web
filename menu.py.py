import streamlit as st
import pandas as pd

name = st.text_input("Enter your first name: ")
fname = st.text_input("Enter your father's name: ")
adr = st.text_input("Enter your address: ")
classdata = st.selectbox("select your class", ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5" ])
button = st.button("Submit")
if button:
    data = {
        "Name": [name],
        "Father's Name": [fname],
        "Address": [adr],
        "Class": [classdata]
    }
    df = pd.DataFrame(data)
    st.write("Submitted Data:")
    st.dataframe(df)



