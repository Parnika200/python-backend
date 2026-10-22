#http status codes
from fastapi import FastAPI,status,HTTPException

app=FastAPI()

@app.post("/users",status_code=status.HTTP_201_CREATED)
def users():
    return {"message":"created"}

# http exceptions

@app.get("/users/{user_id}")
def users(user_id):
    if user_id!=1:
        raise HTTPException(
            status_code=404,
            detail="error"
        )
    return{
        "id":1,
        "name":"anna"
    }