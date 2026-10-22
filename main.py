from fastapi import FastAPI
from pydantic import BaseModel

class student(BaseModel):
    name:str
    age:int
    email:str

app=FastAPI() #server

"""
@app.get("/")
def home():
    return {"message":"hello"}


@app.get("/users")
def users():
    return {"users":["anna","lara","maya"]}


# DYNAMIC ROUTING

@app.get("/student/{s_id}")
def student(s_id):
    return {"id":s_id}

 # data validation

@app.get("/customer/{c_id}")
def customer(c_id:int): # only accepts int parameter
    return {"id":c_id}

"""
#QUERY PARAMS
"""
@app.get("/product")
def prod(name : str=None): #default parameter
    return {"name":name}

@app.get("/product")
def prod(name:str=None,price:int=10):
    return{
        "name":name,
        "price":price
    }

# POST REQUEST

@app.post("/create-user")
def create(std:student):
    return {
        "student":std
    }
"""

#CRUD
todo=[]
class Todo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/addtodo")
def addtodo(new_todo:Todo):
    todo.append(new_todo)
    return {"message":"todo added","data":new_todo}

#DYNAMIC 
@app.get("/todos/{todo_id}")
def todos(todo_id:int):
    for t in todo:
        if t.id==todo_id:
            return t
    return {"error":"not found"}

@app.get("/addtodo")
def seetodo():
    return todo

@app.put("/todos/{todo_id}")
def todos(todo_id:int,updated:Todo):
    for t in todo:
        if t.id==todo_id:
            t.id=updated.id
            t.title=updated.title
            t.completed=updated.completed
            return {"message":"updated","data":updated}
    return {"error":"error"}

@app.delete("/todos/{todo_id}")
def todos(todo_id:int):
    for t in todo:
        if t.id==todo_id:
            todo.pop(t)
        return {"message":"delete"}
    return {"message":"error"}


#
users=[]

#main class
class User(BaseModel):
    name:str
    age:int
    password:int

# response model
class UserResponse(BaseModel):
    name:str
    age:int

@app.post("/create")
def create(user:User):
    users.append(user)
    return {"message","user created"}

@app.get("/users",response_model=UserResponse)
def getUsers():
    return{
        "name":'anna',
        "age":20,
        "password":"124"
    }


@app.put("/create/{user_id}")
def update(user_id:int,user:User,notify:bool=False):
    if user_id<len(users):
        users[user_id]=user

        return{
            "message":"updated",
            "notify":notify,
            "data":user
        }
    return {"error":"not found"}