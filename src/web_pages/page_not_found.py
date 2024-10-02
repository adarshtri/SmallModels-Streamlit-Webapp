import streamlit as st

from src.helpers.footer import set_footer


def page_not_found():
    st.title("Page not found.")
    set_footer()