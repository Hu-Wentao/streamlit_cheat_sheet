## 速览

### 一般步骤
```python
# 1 导入包
import streamlit as st

# 2.1 配置-布局
st.set_page_config(layout="wide")

# 2.2 配置-全页面静态常量
const_map = {"张三":"zhang san"}


# 3.1 UI-侧边栏
with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    ...

# 3.2 UI-主体内容
st.header("hello world")

# 3.2.1 布局组件
# st.columns(2)

```

## 多页面插件

- 参考文档
https://st-pages.streamlit.app/

### 使用
```shell
# 安装依赖
pip install -r requirements.txt
```
```shell
# 启动
python -m streamlit run app.py
```


## 插件使用
[ext_components](./src/ext_component.py)

## 高级功能

### 缓存 st.cache
https://docs.streamlit.io/library/advanced-features/caching#controlling-cache-size-and-duration

#### 缓存 TTL
```python
@st.cache_data(ttl=3600)  # 👈 Cache data for 1 hour (=3600 seconds)
def get_api_data():
    data = api.get(...)
    return data
```
#### 缓存节点上限
```python
@st.cache_data(max_entries=1000)  # 👈 Maximum 1000 entries in the cache
def get_large_array(seed):
    np.random.seed(seed)
    arr = np.random.rand(100000)
    return arr
```

#### 自定义加载Loading内容
```python
@st.cache_data(show_spinner=False)  # 👈 Disable the spinner
def get_api_data():
    data = api.get(...)
    return data

@st.cache_data(show_spinner="Fetching data from API...")  # 👈 Use custom text for spinner
def get_api_data():
    data = api.get(...)
    return data
```

#### 排除非缓存参数
> 使用 `_`开头命名参数, 则该参数不会被参与hash key计算
```python
@st.cache_data
def fetch_data(_db_connection, num_rows):  # 👈 Don't hash _db_connection
    data = _db_connection.fetch(num_rows)
    return data

connection = init_connection()
fetch_data(connection, 10)
```

#### [更多缓存用法](./doc/CACHE.md)