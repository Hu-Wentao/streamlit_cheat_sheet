import streamlit as st

## Config 配置 加密信息
st.header('配置加密信息, 本地模式: 将密文存放到`.streamlit/secrets.toml`中, 远程模式 ')

st.markdown('''
### 管理密钥 博文
https://blog.streamlit.io/secrets-in-sharing-apps/
### 官方文档
https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app/connect-to-data-sources/secrets-management

### 示例
```toml
# Everything in this section will be available as an environment variable 
db_username = "Jane"
db_password = "12345qwerty"

# You can also add other sections if you like.
# The contents of sections as shown below will not become environment variables,
# but they'll be easily accessible from within Streamlit anyway as we show
# later in this doc.   
[my_cool_secrets]
things_i_like = ["Streamlit", "Python"]
```
''')
st.write(st.secrets['db_username'])
