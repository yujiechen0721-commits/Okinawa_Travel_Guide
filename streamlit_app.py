import streamlit as st
import os

# 設定滿版
st.set_page_config(layout="wide", page_title="沖繩旅遊指南")

# 讀取首頁（用 utf-8 避免中文字亂碼）
html_file = "首頁.html"
if os.path.exists(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=1200, scrolling=True)
else:
    st.write("### 歡迎來到沖繩旅遊指南！")
    st.write("找不到首頁.html，請檢查檔案。")
    st.image("首頁封面圖.png")  # 先顯示一張圖測試
