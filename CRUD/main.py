from fastapi import FastAPI,Depends,status,Response,HTTPException
import schemas
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session
# Initialize FastAPI application
app = FastAPI(
    title="Blog API CRUD Operations",
    description="A simple API for blog CRUD operations",
    version="0.1.0"
)

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

# @app.post('/blog',status_code=201)
@app.post('/blog',status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog,db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title,content=request.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get('/blog')
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id}',status_code=200)
def get_blog_by_id(id:int, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Blog with id = {id} not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id = {id} not found")
        
    return blog

@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id = {id} not found")
    blog.title = request.title
    blog.content = request.content
    db.commit()
    db.refresh(blog)
    return blog

@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id = {id} not found")
    db.delete(blog)
    db.commit()