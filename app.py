import streamlit as st
from st_pages import show_pages_from_config

show_pages_from_config()

st.markdown(
    """
## Home 

### streamlit 速览教程

请查看本速览之前, 先完成[Streamlit 30天 速成 https://30days.streamlit.app/](https://30days.streamlit.app/) 

## Todo
- [ ] 添加 doc引用到app内部
- [ ] 添加 Streamlit 30Days 章节解析
- [ ] 添加 Streamlit Gallery , 展示组件内容
""")
