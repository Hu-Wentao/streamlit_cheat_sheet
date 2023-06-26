import streamlit as st
from st_pages import show_pages_from_config

show_pages_from_config()

st.header('Home Page')

st.markdown(
    """
#### streamlit 速览教程

请查看本速览之前, 先完成[Streamlit 30天 速成](https://30days.streamlit.app/)
""")
