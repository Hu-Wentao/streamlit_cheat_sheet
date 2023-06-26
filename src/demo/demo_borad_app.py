
import streamlit as st
import requests


get_data = {
    "教育": "education",
    "消遣": "recreational",
    "社交": "social",
    "手工": "diy",
    "慈善": "charity",
    "烹饪": "cooking",
    "放松": "relaxation",
    "音乐": "music",
    "作业": "busywork",
}


st.title('🏀 无聊 API 应用')

# sidebar
st.sidebar.header('Input')
# 创建一个 selectbox
selected_type = get_data[st.sidebar.selectbox(
    '选择一种活动类型',
    get_data.keys(),)]

# 下拉菜单得到参数之后, 请求API得到 data
suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type}'


@st.cache_data
def get_json_data(u: str):
    return requests.get(u)


suggested_activity = get_json_data(suggested_activity_url).json()

# 展示data: 创建两个column
c1, c2 = st.columns(2)
with c1:
    with st.expander('关于App'):
        st.write('你无聊吗? 无聊 API 应用 提供一些有意思的活动建议, 摆脱无聊 做回自己')
with c2:
    with st.expander('JSON data'):
        st.write(suggested_activity)

st.header('建议活动')
st.info(suggested_activity['activity'])

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label='参与者数量',
              value=suggested_activity['participants'], delta='')
with col2:
    st.metric(label='活动类型',
              value=suggested_activity['type'].capitalize(), delta='')
with col3:
    st.metric(label='价格', value=suggested_activity['price'], delta='')
