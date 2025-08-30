from fastapi import FastAPI
from . import schemas  # Import Blog schema from local schemas module

# Initialize FastAPI application
app = FastAPI(
    title="Blog API CRUD Operations",
    description="A simple API for blog CRUD operations",
    version="0.1.0"
)

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