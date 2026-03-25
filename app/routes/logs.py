from fastapi import APIRouter, UploadFile
from app.services import parser, s3

router = APIRouter()

@router.post("/upload")
async def upload_log(file: UploadFile):
    content = await file.read()

    # upload to s3
    file_url = s3.upload_file(file.filename, content)

    # analyze logs
    text = content.decode("utf-8", errors="ignore")
    analysis = parser.analyze_logs(text)

    return {
            "file_url": file_url, 
            "analysis": analysis
            }
