from flask import Flask, request
from gpiozero import LED
app = Flask(__name__)

@app.route("/on")
def test():
    led = LED(27)
    led.on()
    return "On!"

@app.route("/off")
def test2():
    return "On!"

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
