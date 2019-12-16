from flask import Flask, request, render_template, json
#from gpiozero import LED
app = Flask(__name__)
#led = LED(27)
currBrightness = 0 #TODO: set to current led brightness
status = 0

@app.route("/on")
def test():
#    led.on()
    return render_template("on.html")

@app.route("/off")
def test2():
#    led.off()
    return render_template("off.html")

@app.route("/status")
def status():
#    if(led.is_lit):
#        return render_template("on.html")
#    else:
    return render_template("off.html")

@app.route("/")
def hello():
    print(currBrightness)
    return render_template("main.html", brightness=currBrightness)





#background processses that happen without any refreshing


#Toggle Power
#@app.route('/toggle_power', methods=['POST'])
#def toggle_power():



#Change brightness
@app.route('/set_brightness',methods=['GET', 'POST'])
def setBrightness():
    if request.method == 'POST':
        currBrightness = int(request.form['myBrightness'])
    
    print(currBrightness) #TODO: set LED to new brightness

    #Returns variable to update page with current brightness
    return json.jsonify({
        'newBrightness': currBrightness
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=False, use_reloader=False)

