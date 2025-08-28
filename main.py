"""
FastAPI Blog Application

A simple blog API built with FastAPI that demonstrates:
- CRUD operations for blog posts
- Query parameters and path parameters
- Pydantic models for request/response validation
- Basic routing and endpoint organization
"""

from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from pydantic import BaseModel, Field
import uvicorn

# Initialize FastAPI application with metadata
app = FastAPI(
    title="Blog API",
    description="A simple blog management API",
    version="1.0.0",
    contact={
        "name": "dasgajraj",
        "twitter": "@dasgajraj",
        "linkedin": "in/dasgajraj"
    }
)

@app.get('/')  # Root endpoint
def index():
    """Returns a list of blogs."""
    return {'data': 'blog-list'}

@app.get('/blog')  # Endpoint to show all blogs
def show_all_blogs(limit: int = Query(10, description="Number of blogs to return"), 
                   published: bool = Query(False, description="Filter by published status"), 
                   sort: Optional[str] = Query(None, description="Sort order")):
    """
    Returns published or unpublished blogs based on query parameters.
    
    Args:
        limit: Maximum number of blogs to return (default: 10)
        published: Filter by published status (default: False)
        sort: Sort order for the blogs (optional)
    
    Returns:
        Dictionary containing the filtered blog data
    """
    if published:
        return {'data': f'{limit} published blogs from DB'}
    else:
        return {'data': f'{limit} unpublished blogs from DB'}

@app.get('/about')  # About endpoint
def about():
    """Returns information about the author."""
    return {'data': {'age': 21, 'location': 'India'}}

@app.get('/social-media')  # Social media endpoint
def social_media():
    """Returns social media handles."""
    return {'data': {'twitter': '@dasgajraj', 'linkedin': 'in/dasgajraj'}}

@app.get('/blog/unpublished')  # Endpoint for unpublished blogs
def unpublished():
    """Returns all unpublished blog data."""
    return {'data': "All Unpublished Data"}

@app.get('/blog/{id}')  # Endpoint for blog by id
def show(id: int):
    """Returns blog data for a given id."""
    return {'data': id}

@app.get('/blog/{id}/comments')  # Endpoint for comments of a blog
def comments(id):
    """Returns comments for a given blog id."""
    return {'data': {'1', '2'}}

class Blog(BaseModel):
    """
    Pydantic model for blog post data validation.
    
    Attributes:
        title: The title of the blog post
        content: The main content/body of the blog post
        published: Whether the blog post is published (default: False)
    """
    title: str = Field(..., description="The title of the blog post", min_length=1, max_length=200)
    content: str = Field(..., description="The main content of the blog post", min_length=1)
    published: Optional[bool] = Field(default=False, description="Publication status of the blog post")

@app.post('/blog')
def create_blog(blog: Blog):
    """
    Creates a new blog post.
    
    Args:
        blog: Blog model containing title, content, and published status
        
    Returns:
        Dictionary with confirmation message and blog details
    """
    return {
        'message': 'Blog created successfully',
        'data': {
            'title': blog.title,
            'content': blog.content,
            'published': blog.published
        }
    }

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=7000)