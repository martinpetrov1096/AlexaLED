from flask import Flask, request, render_template
from gpiozero import LED
app = Flask(__name__)
led = LED(27)
@app.route("/on")
def test():
    led.on()
    return "On!"

@app.route("/off")
def test2():
    led.off()
    return render_template("on.html")

@app.route("/status")
def status():
    if(led.is_lit):
        return "on"
    else:
        return "off"

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

