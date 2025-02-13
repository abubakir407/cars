from fastapi import APIRouter
from db.service import *
from api import result_message

car_router = APIRouter(prefix='/cars', tags=["Машины"])

# Добавление новой машины
@car_router.post('/add_car')
async def add_car(brand: str, model: str, manufactured: int, color: str, description: str = None):
    r = add_car_db(brand, model, manufactured, color, description)
    return result_message(r)

# Вывод
@car_router.get('/show_car')
async def show_car(car_id: int = 0):
    r = get_one_or_all_cars_db(car_id)
    return result_message(r)

# Удаление
@car_router.delete('/delete_car')
async def show_car(car_id: int):
    r = delete_car_db(car_id)
    return result_message(r)

# Изменение
@car_router.put('/edit_car')
async def edit_info_car(car_id: int, info_type: str, new_info: str):
    r = update_car_info_db(car_id, info_type, new_info)
    return result_message(r)
