from fastapi import FastAPI
import schemas
import models
from database import engine
# Initialize FastAPI application
app = FastAPI(
    title="Blog API CRUD Operations",
    description="A simple API for blog CRUD operations",
    version="0.1.0"
)

models.Base.metadata.create_all(engine)

@app.post('/blog')
def create(data: schemas.Blog):
    """
    Create a new blog post
    
    Parameters:
    - data: Blog schema with title and content fields
    
    Returns:
    - Dictionary with the blog title and content
    """
    return {'title': data.title, 'content': data.content}