import streamlit as st
import numpy as np
import pandas as pd
from time import time

"""性能优化
"""
a0 = time()


with st.expander("缓存数据"):
    st.markdown("""
    ## 资源 
    https://docs.streamlit.io/library/advanced-features/caching

    ## cache_data
    缓存一切可以放入数据库的内容
    例如 函数的计算结果, 数据框, API返回值, 等

    ## cache_resource
    缓存一切不可以放入数据库的内容
    例如 数据库连接, 机器学习模型, 等
    """)

st.header("1. 最小示例 cache_data ")


@st.cache_data
def long_running_function(param1, param2):
    """
    添加cache_data 直接后, 本护士的返回值将被缓存
    """
    df = pd.DataFrame(
        np.random.rand(2000000, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df


df = long_running_function(1, 2)
st.dataframe(df)

st.button("Rerun")
