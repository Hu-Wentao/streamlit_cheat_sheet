""" 布局组件
"""
import streamlit as st

st.markdown("""
## 参考材料
https://docs.streamlit.io/library/api-reference/layout


## 布局组件
### st.sidebar 侧边栏
### st.column 列(一般会自动排列成行, 窄屏收缩成列)
### st.tabs 表
### st.expander 展开面板

## 三方插件
### streamlit-pydantic
根据 pydantic模型自动生成UI
https://github.com/lukasmasuch/streamlit-pydantic

### streamlit-elements
可拖放组件的 管理员页面卡片组件
https://github.com/okld/streamlit-elements
""")

# 侧边栏, 在侧边栏放一个 slider
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)


# 展开面板
with st.expander('展开面板: About this app'):
    st.write(
        'This app shows the various ways on how you can layout your Streamlit app.')
    st.image(
        'https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png',
        width=250
    )
