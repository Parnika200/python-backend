from fastapi import FastAPI,Depends

app=FastAPI()

def fun():
    return{
        "message":"common logic"
    }

@app.get("/home")
def home(data=Depends(fun)):
    return data


#reusable code

def getuser():
    return{
        "name":"anna"
    }

@app.get("/profile")
def profile(data=Depends(getuser)):
    return data

@app.get("/dashboard")
def dashboard(data=Depends(getuser)):
    return data