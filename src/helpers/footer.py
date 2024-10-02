import streamlit as st

def set_footer(name = "Adarsh Trivedi"):

    footer_html = f"""<div style='text-align: center;'>
      <p>Developed with ❤️ by {name}</p>
    </div>"""
    st.markdown(footer_html, unsafe_allow_html=True)