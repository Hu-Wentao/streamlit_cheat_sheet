import streamlit as st
import time

st.header('展示图片')
st.image(
    'https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png',
    width=250
)


st.header("进度条")

my_bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.05)
    my_bar.progress(percent_complete + 1)

# 全屏-彩色气球上升动画; 当上面的阻塞函数执行完毕后, 执行下面的代码,播放一次气球动画
# 刷新页面后, 状态会重置, 重新等待进度条结束, 然后再次播放气球动画
st.balloons()
