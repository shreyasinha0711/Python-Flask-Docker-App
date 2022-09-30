from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return '<center><h1 style="background-color:#80d4ff;"></br>Hello AirBus !! Welcome</br></br></h1></center>'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
