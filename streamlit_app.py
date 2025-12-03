import streamlit as st
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os
from urllib.parse import unquote

# 建立 FastAPI app
app = FastAPI()

# 掛載靜態檔案（包含所有 .html 和圖片）
app.mount("/static", StaticFiles(directory=".", html=True), name="static")

# 根目錄跳到首頁
@app.get("/")
async def root():
    return FileResponse("首頁.html")

# 通用檔案路由（支援 /住宿.html、/圖片.jpg 等）
@app.get("/{path:path}")
async def serve_path(path: str):
    decoded_path = unquote(path)
    if os.path.exists(decoded_path):
        if decoded_path.endswith('.html'):
            return FileResponse(decoded_path)
        else:
            return FileResponse(decoded_path)
    return HTMLResponse(content="<h1>404 - 找不到檔案</h1><a href='/'>回首頁</a>", status_code=404)

# 讓 Streamlit 啟動 FastAPI（Streamlit Cloud 會自動處理埠）
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8501)

# Streamlit 部分：用 iframe 嵌入根路徑，讓它滿版
st.set_page_config(layout="wide")
st.components.v1.iframe("http://localhost:8501/", width=None, height=1200, scrolling=True)
