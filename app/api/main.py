import os

from fastapi import FastAPI, UploadFile

app = FastAPI(title="VideoCaptioner API")


@app.get("/")
async def root():
    return {"message": "VideoCaptioner API is running",
            "guide": "/post to /upload to upload a video file and get the caption"}


@app.post("/upload")
async def upload_file(file: UploadFile):
    """上传文件"""
    # 定义上传文件的目标文件夹
    UPLOAD_FOLDER = "upload"

    # 创建上传文件夹，如果不存在
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    try:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        with open(file_path, "wb") as f:
            contents = await file.read()
            f.write(contents)
        return {"filename": file.filename, "message": f"File saved successfully to {file_path}"}
    except Exception as e:
        return {"error": str(e)}



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
