import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.header('组件使用 `streamlit_pandas_profiling`')
st.markdown(
    """
## 使用外部组件, 详情参考链接
https://30days.streamlit.app/?challenge=Day14

## 自定义组件-官方文档
https://docs.streamlit.io/library/components

## 官方组件列表
https://streamlit.io/components
- 民间的组件列表
https://okld-gallery.streamlit.app/?p=streamlit-gallery


### 常用组件

- pages 多页面,提供侧边栏切换页面功能 **常用**
https://github.com/blackary/st_pages

- option-menu 功能类似 selectbox,可用于侧边导航栏按钮等
https://github.com/victoryhb/streamlit-option-menu

- tags 标签, 功能和样式类似 multiselect, UI效果更接近 appwrite的enum框
https://github.com/gagan3012/streamlit-tags

- extras 附加组件, 如折叠的文本内容(参考IDEA MD文档折叠)
https://github.com/arnaudmiribel/streamlit-extras

- player 播放器
https://github.com/okld/streamlit-player

- embedcode 将外部代码(如github仓库,gist)嵌入到app内
https://github.com/randyzwitch/streamlit-embedcode

- cropper 图片裁剪工具
https://github.com/turner-anderson/streamlit-cropper

- discourse 嵌入discourse论坛
https://github.com/okld/streamlit-discourse
https://github.com/okld/streamlit-disqus


"""
)

# df = pd.read_csv(
#     'https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

# pr = df.profile_report()
# st_profile_report(pr)
