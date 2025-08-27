from fastapi import FastAPI
from fastapi import FastAPI  # Import FastAPI framework

app = FastAPI()  # Create FastAPI app instance

@app.get('/')  # Root endpoint
def index():
    """Returns a list of blogs."""
    return {'data': 'blog-list'}

@app.get('/blog')  # Endpoint to show all blogs
def showAllBlogs(limit, published: bool):
    """Returns published or unpublished blogs based on query params."""
    if published:
        return {'data': f'{limit} published blogs from DB'}
    else:
        return {'data': f'{limit} unplblished blogs from DB'}

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

# completed 50 mins..

