import boto3
import uuid

s3 = boto3.client("s3")

BUCKET_NAME = "log-analyzer-upland1"

def upload_file(filename: str, content: bytes):
    unique_name = f"{uuid.uuid4()}-{filename}"

    s3.put_object(
        Bucket = BUCKET_NAME,
        Key = unique_name,
        Body = content
            )
    
    return f"https://{BUCKET_NAME}.s3.amazonaws.com/{unique_name}"
