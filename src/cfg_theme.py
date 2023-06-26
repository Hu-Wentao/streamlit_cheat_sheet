import streamlit as st

st.title('自定义App主题')

st.write('将下面的内容保存到 `.streamlit/config.toml` 中')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")