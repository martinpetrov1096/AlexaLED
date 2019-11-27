from flask import Flask, request, render_template
from gpiozero import LED
app = Flask(__name__)
led = LED(27)


@app.route("/on")
def test():
    led.on()
    return render_template("on.html")

@app.route("/off")
def test2():
    led.off()
    return render_template("off.html")

@app.route("/status")
def status():
    if(led.is_lit):
        return render_template("on.html")
    else:
        return render_template("off.html")

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

