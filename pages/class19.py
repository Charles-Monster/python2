import streamlit as st
from utils import init_page


init_page()
st.title("聊天室規範")

demo_messages =[
    {"role":"user","content":"你好，請問要怎麼學python?"},
                {"role":"assistant","content":"學習python的基本步驟:\n1.了解基礎語法\n2.練習寫簡單程式\n3.解決實際問題"},
{"role":"user","content":"看起來不難耶"},
{"role":"assistant","content":"沒錯!循序漸進地學習最重要。要步要試試看寫個簡單的程式?"}]
for message in demo_messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
if message:=st.chat_input("請輸入訊息"):
    with st.chat_message("user"):
        st.write(message)
    with st.chat_message("assistant"):
        st.write(f"這是示範回覆:我收到你的訊息:[{message}]")