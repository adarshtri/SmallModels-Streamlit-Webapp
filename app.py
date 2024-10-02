import streamlit as st

from src.helpers.page_loader import load_page_based_on_query_params

# Read URL parameters
params = st.query_params

page_loader = load_page_based_on_query_params(params)

page_loader()