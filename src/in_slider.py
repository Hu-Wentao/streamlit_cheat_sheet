import streamlit as st
from datetime import time, datetime

# 滑块
st.header('数值滑块  返回值-int, 最小值-int, 最大值-int, 默认值-int')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')


st.subheader(
    '范围滑块  返回值-tupl[float,float], 最小值-int, 最大值-int, 默认值-tuple[float, float]')
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values-', values)

st.subheader(
    '时间-范围滑块  返回值-tuple, 最小值-datetime.time, 最大值-datetime.time, 默认值-tuple[]')
appointment = st.slider(
    "Schedule your appointment-",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for-", appointment)

# 样例 4

st.subheader(
    '日期时间-范围滑块  返回值-datetime.datetime, 最小值-datetime.datetime, 最大值-datetime.datetime, 默认值-datetime.datetime')
start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh-mm")
st.write("Start time-", start_time)


st.markdown("""
# 相关组件 select_slider
> 可以选择 enum 类型的值

https://docs.streamlit.io/library/api-reference/widgets/st.select_slider
```python
st.select_slider(label, options=(), value=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
```
""")


color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)
