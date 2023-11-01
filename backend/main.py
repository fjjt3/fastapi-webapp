from fastapi import FastAPI
from core.config import settings
# from db.session import engine
# from db.base import Base //  we use alembic

''' def create_tables():
    Base.metadata.create_all(bind=engine) '''
    
def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_TITLE)
    # create_tables() we use alembic
    return app

app = start_application()

@app.get("/")
def hello():
    return {"msg":"Hello FastAPI"}
