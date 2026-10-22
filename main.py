from fastapi import FastAPI,HTTPException

app=FastAPI()

@app.get("/users/{user_id}")
def users(user_id):
    if user_id==0:
        raise HTTPException(
            status_code=404,
            detail="not fount"
        )
    return{
        "message":"no error"
    }