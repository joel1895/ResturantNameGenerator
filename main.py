import streamlit as st
import langchain_helper

st.title("Resturant Name Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine",("Indian","Italian","Mexican","Arbaic","American"))



if cuisine:
    response = langchain_helper.generator_resturant_name_items(cuisine)
    st.header(response['resturant_name'])
    menu_items = response['menu_items'].strip().split(",")
    st.write("**Menu Items**")

    for item in menu_items:
        st.write("-",item)






