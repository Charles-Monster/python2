from utils import init_page

init_page()
import streamlit as st

def menu():
    st.sidebar.title("菜單")
    st.sidebar.page_link(page="main.py",label="首頁",icon="🏠")
    st.sidebar.markdown("---")
    st.title("課程")
    st.sidebar.page_link(page="pages/class16.py",label="課程11",icon="📚")
    st.sidebar.page_link(page="pages/class17.py",label="課程12",icon="📚")
    st.sidebar.page_link(page="pages/class17-2.py",label="課程13",icon="📚")
    st.sidebar.markdown("---")