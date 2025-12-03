import streamlit as st
import os

# 首頁名稱「首頁.html」
html_file = "首頁.html"

if os.path.exists(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # 滿版顯示 + 支援滾動
    st.set_page_config(layout="wide", page_title="沖繩旅遊指南")
    st.components.v1.html(html_content, height=1200, scrolling=True)
else:
    st.error("找不到 首頁.html，請確認檔名正確")
