import streamlit as st
import os
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
with st.expander("點擊展開/收起"):
    st.markdown("""
    這是展開元件內部""")

image_folder="image"
image_files=os.listdir(image_folder)
st.write(image_files)

png=st.selectbox("圖片設定",["0.png","1.png","2.png"])
width=st.selectbox("寬",["300","310","320","330","340","350","360","370","380","390","400"])
if png=="0.png":
    st.image("image/0.png",width=300)
elif png=="1.png":
    st.image("image/1.png",width=300)
else:    
    st.image("image/2.png",width=300)

st.title("圖片元件")
st.image("image/0.png",width=300)

