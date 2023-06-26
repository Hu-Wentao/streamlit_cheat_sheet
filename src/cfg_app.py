import streamlit as st

st.markdown("""
## 配置选项
https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options


### 全局配置
路径
`~/.streamlit/config.toml`
示例
```toml
[server]
port = 80
```

### 项目配置
路径
`./.streamlit/config.toml`

配置环境变量, 以 `STREAMLIT_` 开头, 例如
```shell
export STREAMLIT_SERVER_PORT=80
export STREAMLIT_SERVER_COOKIE_SECRET=dontforgottochangeme
```

运行
```shell
# 使用参数
streamlit run your_script.py --server.port 80
```

## 更多信息
https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options
""")
