import streamlit as st

st.title("這是標題")
st.write(
    "這是一個用 st.write 寫的字串,可以處理多種格式,例如:數字,文字,Markdown,數據框等"
)
st.markdown(
    """
    這是一個用 `st.markdown `顯示的純文字字串,可以處理 Markdown 語法。
    例如:
    * **粗體文字** 
    *　*斜體文字* 
    *[連結](https://www.example.com)
    *代碼塊:
    ```python 
    print('Hello streamlit!')
    ```
    """
)
