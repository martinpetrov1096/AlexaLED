from flask import Flask, request, render_template, json, g
from gpiozero import PWMLED
app = Flask(__name__)
led = PWMLED(27)

#Global Variables
variables = {}
variables['currBrightness'] = 1


#ALEXA GET REQUESTS
@app.route("/on")
def alexaOn():
    led.value = variables['currBrightness']
    return render_template("on.html")

@app.route("/off")
def alexaOff():
    led.off()
    return render_template("off.html")

@app.route("/status")
def status():
    if(led.is_lit):
        return render_template("on.html")
    else:
        return render_template("off.html")



#MAIN WEBPAGE
@app.route("/")
def hello():
    return render_template("main.html", brightness=led.value * 100)

#background processses that happen without any refreshing


#Toggle Power
#@app.route('/toggle_power', methods=['POST'])
#def toggle_power():



#Change brightness
@app.route('/set_brightness',methods=['GET', 'POST'])
def setBrightness():
    if request.method == 'POST':
        variables['currBrightness'] = float(request.form['myBrightness']) / 100
        led.value = variables['currBrightness']
    print(led.value) #TODO: set LED to new brightness

    #Return nothing
    return ''


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=False, use_reloader=False)

