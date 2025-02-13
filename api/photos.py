from fastapi import APIRouter, UploadFile, File
import random
from db.service import *
from api import result_message

photo_router = APIRouter(prefix="/photo", tags=["Фотографии"])

#Добавление фотографии
@photo_router.post("/add_photo")
async def add_photo(car_id: int, photo_file: UploadFile = File(...)):
    file_id = random.randint(1, 1000000)
    if photo_file:
        with open(f"db/images/photo_{file_id}_{car_id}.jpg", "wb") as photo:
            photo_to_save = await photo_file.read()
            photo.write(photo_to_save)
            add_photo_db(car_id, photo.name)
            return {"status": 1, "message": "Фото успешно сохранено"}
    return {"status": 0, "message": False}

#Удаление фотографии
@photo_router.delete("/add_photo")
async def delete_photo(photo_id: int):
    r = delete_photo_db(photo_id)
    return result_message(r)
