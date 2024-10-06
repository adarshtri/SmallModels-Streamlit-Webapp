import streamlit as st


def home_page():
    st.write("# Welcome to my ML/AI Project Demos 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """ 
        ----------------------------------------
        On this website, I host my favorite ML/AI personal projects as
        running demos.

        **👈 Select a demo from the sidebar** to explore the demo and
        see what it does.

        ### Want to reach out to me?
        - Email: [adarsh.trivedi100@gmail.com](adarsh.trivedi100@gmail.com)
        - Find me on [LinkedIn](https://www.linkedin.com/in/adarshtri720/)
        - Explore my [GitHub](https://discuss.streamlit.io) to find repositories for
          each of the demos on this website.
        """
    )