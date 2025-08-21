from fastapi import FastAPI

myapp = FastAPI()

@myapp.get('/')
def index():
    return {'data' : {'name': {'first': 'Das Gajraj',  'last': 'Sharma'}}}

@myapp.get('/about')
def about():
    return {'data' : {'age': 21, 'location': 'India'}}

@myapp.get('/social-media')
def social_media():
    return {'data' : {'twitter': '@dasgajraj', 'linkedin': 'in/dasgajraj'}}

