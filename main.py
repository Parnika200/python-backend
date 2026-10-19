from fastapi import FastAPI

app=FastAPI() #server

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


#QUERY PARAMS

@app.get("/product")
def prod(name : str=None): #default parameter
    return {"name":name}

# POST REQUEST