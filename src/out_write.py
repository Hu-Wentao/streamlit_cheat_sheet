import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

# 标题, 相当于 h3
st.header('st.write')
# 子标题,相当于 h4
st.subheader("subheader")
# 表格标题 
st.caption("caption")
# 代码
st.code("print('hello world')")
# 文本
st.text("text")
# 公式
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
# markdown
st.markdown("""
### header3
#### header4

```dart
void main(){
    print("hello world");
}
```
""")
# 数字
st.write(1234)

# 数据框
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

# 文本+数据框 混合输出
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

# 图表
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)


