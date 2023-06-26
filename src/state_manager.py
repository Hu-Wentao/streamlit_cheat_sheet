import streamlit as st


st.header('状态管理 st.session_state')

with st.expander('资源'):
    st.markdown("""
    ## 文档
    https://docs.streamlit.io/library/api-reference/session-state

    ## 博文
    https://docs.streamlit.io/library/advanced-features/session-state
    """)


def lbs_to_kg():
    st.session_state.kg = st.session_state.lbs/2.2046


def kg_to_lbs():
    st.session_state.lbs = st.session_state.kg*2.2046


st.header('写入状态: Input')
col1, spacer, col2 = st.columns([2, 1, 2])
with col1:
    pounds = st.number_input("Pounds:", key="lbs", on_change=lbs_to_kg)
with col2:
    kilogram = st.number_input("Kilograms:", key="kg", on_change=kg_to_lbs)

st.header('读取状态: Output')
st.write("st.session_state object:", st.session_state)

