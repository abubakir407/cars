from fastapi import FastAPI
from db import Base, engine
from api.photos import photo_router
from api.cars import car_router


Base.metadata.create_all(engine)

# Путь
app = FastAPI(docs_url="/docs")

app.include_router(photo_router)
app.include_router(car_router)
