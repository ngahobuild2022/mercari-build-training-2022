import hashlib
import aiofiles
from fastapi import UploadFile
import os

def hash_image(file_name):
  file_name_without_extension = os.path.splitext(file_name)[0]
  hash = hashlib.sha256(file_name_without_extension.encode('utf-8')).hexdigest()
  return f'{hash}.jpg'

async def upload_image(file_path: str, file: UploadFile):
  async with aiofiles.open(file_path, 'wb') as out_file:
    while content := await file.read(1024):
      await out_file.write(content)

  return os.path.basename(out_file.name)