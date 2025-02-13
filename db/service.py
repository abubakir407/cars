from db import get_db
from db.models import *

# Добавление новой машины
def add_car_db(brand, model, manufactured, color, description = None):
    db = next(get_db())
    new_car = Car(brand=brand, model=model, manufactured=manufactured, color=color, description=description)
    db.add(new_car)
    db.commit()
    return True

# Вывод
def get_one_or_all_cars_db(car_id = 0):
    db = next(get_db())
    if car_id:
        exact_car = db.query(Car).filter_by(id=car_id).first()
        if exact_car:
            car_photos = db.query(CarPhoto).filter_by(id=car_id).all()
            if car_photos:
                return exact_car, car_photos
            else:
                return exact_car
        return False
    return db.query(Car).all(), db.query(CarPhoto).all()

# Удаление
def delete_car_db(car_id):
    db = next(get_db())
    car_no_more = db.query(Car).filter_by(id=car_id).first()
    if car_no_more:
        car_photos = db.query(CarPhoto).filter_by(id=car_id).all()
        if car_photos:
            for photo in car_photos:
                db.delete(photo)
        db.delete(car_no_more)
        db.commit()
        return True
    return False

# Изменение
def update_car_info_db(car_id, info_type, new_info):
    db = next(get_db())
    car = db.query(Car).filter_by(id=car_id).first()
    if car:
        if info_type == 'color':
            car.color = new_info
        elif info_type == 'description':
            car.description = new_info

# Добавление фотографии
def add_photo_db(car_id, photo_file):
    db = next(get_db())
    new_photo = CarPhoto(car_id=car_id, photo_file=photo_file)
    db.add(new_photo)
    db.commit()
    return True

# Удаление фотографии
def delete_photo_db(photo_id):
    db = next(get_db())
    photo_away = db.query(CarPhoto).filter_by(id=photo_id).first()
    if photo_away:
        db.delete(photo_away)
        db.commit()
        return True
    return False

