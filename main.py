from flask import Flask
from datetime import datetime
myobj = datetime.now()
hour=myobj.hour
minute= myobj.minute
new=str(hour)+":"+str(minute)


app = Flask(__name__)

@app.route('/')
def index():
    return {"message": "Hello World","time":new}

app.run(host='0.0.0.0', port=81)
