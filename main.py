from fastapi import FastAPI
from datetime import datetime
myobj = datetime.now()
hour=myobj.hour
minute= myobj.minute
new=str(hour)+":"+str(minute)
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World","time":new}