import streamlit as st
import pandas as pd
import numpy as np

st.header('折线图 返回值-pandas.DataFrame, ')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

st.markdown("""
# 相关组件 area_chart
https://docs.streamlit.io/library/api-reference/charts/st.altair_chart
```python
st.altair_chart(altair_chart, use_container_width=False, theme="streamlit")
```
""")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

c = alt.Chart(chart_data).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.altair_chart(c, use_container_width=True)
