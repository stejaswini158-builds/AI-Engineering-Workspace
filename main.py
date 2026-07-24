from fastapi import FastAPI

from database import Base, engine
from models.user import User

from auth.routes import router as auth_router
from tools.code_tool.routes import router as code_router
from tools.website_builder.routes import router as website_router
from tools.data_cleaner.routes import router as data_cleaner_router
from tools.document_generator.routes import router as document_router

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Engineering Workspace",
    description="Backend for AI Engineering Workspace",
    version="1.0.0"
)

# Register routers
app.include_router(auth_router)
app.include_router(code_router)
app.include_router(website_router)
app.include_router(data_cleaner_router)
app.include_router(document_router)


@app.get("/")
def home():
    return {
        "message": "🚀 AI Engineering Workspace Backend Running!"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }