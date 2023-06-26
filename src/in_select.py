import streamlit as st

# 下拉单选菜单
st.header('下拉单选菜单 (选择枚举) 返回值-string, 选项-list, 默认值-string')

option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)


# 下拉多选菜单
st.header('下拉多选菜单 (选择枚举List) 返回值-list, 选项-list, 默认值-list')
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)


# 复选框(也可以当作单选框/RadioBtn使用)
st.header('复选框 (选择枚举) 返回值-bool, 选项-list, 默认值-bool')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
if icecream:
    st.write("Great! Here's some more 🍦")
if coffee:
    st.write("Okay, here's some coffee ☕")
if cola:
    st.write("Here you go 🥤")
