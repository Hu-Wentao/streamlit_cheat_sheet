import streamlit as st
import time

st.header('表单')
with st.expander("""表单的使用限制"""):
    st.markdown("""
## 资源
https://docs.streamlit.io/library/api-reference/control-flow/st.form

## 注意
所有表单都应当包含一个 st.form_submit_button 对象
st.button 和 st.download_button 将无法在表单中使用
表单能够出现在你应用的任何地方（包括侧边栏、列等等），唯独不能嵌入另一个表单之中
""")

# Full example of using the with notation
st.header('1. 使用 `with` 声明form(推荐)')
st.subheader('Coffee machine')

with st.form('my_form'):
    st.subheader('**Order your coffee**')
    # Input widgets
    coffee_bean_val = st.selectbox('Coffee bean', ['Arabica', 'Robusta'])
    coffee_roast_val = st.selectbox(
        'Coffee roast', ['Light', 'Medium', 'Dark'])
    brewing_val = st.selectbox(
        'Brewing method', ['Aeropress', 'Drip', 'French press', 'Moka pot', 'Siphon'])
    serving_type_val = st.selectbox(
        'Serving format', ['Hot', 'Iced', 'Frappe'])
    milk_val = st.select_slider(
        'Milk intensity', ['None', 'Low', 'Medium', 'High'])
    owncup_val = st.checkbox('Bring own cup')

    # 每个From都必须要添加 `st.form_submit_button`, 否则无法退出with阻塞
    submitted = st.form_submit_button('Submit')

if submitted:
    st.markdown(f'''
        ☕ You have ordered:
        - Coffee bean: `{coffee_bean_val}`
        - Coffee roast: `{coffee_roast_val}`
        - Brewing: `{brewing_val}`
        - Serving type: `{serving_type_val}`
        - Milk: `{milk_val}`
        - Bring own cup: `{owncup_val}`
        ''')
else:
    st.write('☝️ Place your order!')


# Short example of using an object notation
st.header('2. 使用 object 声明form')

form = st.form('my_form_2')
selected_val = form.slider('Select a value')
form.form_submit_button('Submit')

st.write('Selected value: ', selected_val)
