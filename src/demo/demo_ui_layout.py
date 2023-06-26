import streamlit as st

# 默认布局 wide PC端
st.set_page_config(layout="wide")

# 侧边栏 配置
st.sidebar.header('侧边: Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox(
    'Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox(
    'What is your favorite food?', [
        '', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

# 主页 配置
st.header('App 布局')

with st.expander('About this app'):
    st.write(
        'This app shows the various ways on how you can layout your Streamlit app.')
    st.image(
        'https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png',
        width=250
    )

st.header('主页: Output')

# 主页. Column列表, 自动横向排列, 窄屏幕(手机)自动换行,转为一列
col1, col2, col3 = st.columns(3)

with col1:
    if user_name != '':
        st.write(f'👋 Hello {user_name}!')
    else:
        st.write('👈  Please enter your **name**!')

with col2:
    if user_emoji != '':
        st.write(f'{user_emoji} is your favorite **emoji**!')
    else:
        st.write('👈 Please choose an **emoji**!')

with col3:
    if user_food != '':
        st.write(f'🍴 **{user_food}** is your favorite **food**!')
    else:
        st.write('👈 Please choose your favorite **food**!')
