from fastapi import FastAPI
import uvicorn
from database.db import Base, engine
from routes.users_routes import router

def create_tables():
    Base.metadata.create_all(bind=engine)

create_tables()

app = FastAPI()

# Incluir rutas
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)

