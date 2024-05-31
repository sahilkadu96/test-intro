import streamlit as st


a = st.number_input("Enter number a")
b = st.number_input("Enter number b")

if st.button("Add"):
    c = a+b
    st.write(c)
