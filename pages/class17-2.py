from utils import init_page

init_page()
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
image_width=st.number_input("輸入圖片寬度",value=300,step=10)
png=st.selectbox("選擇圖片",["0.png","1.png","2.png"])
st.write(f"你選的圖片是{png}")
if png=="0.png":
    st.image(f"image/0.png",width=image_width)
elif png=="1.png":
    st.image(f"image/1.png",width=image_width)
else:
    st.image(f"image/2.png",width=image_width)
st.title("圖片元件")
st.image("image/0.png",width=300)

