from flask import Flask, request, render_template, json, g

from variables import *

app = Flask(__name__)


#ALEXA GET REQUESTS
@app.route("/on")
def alexaOn():
    on()
    return render_template("on.html")

@app.route("/off")
def alexaOff():
    off()
    return render_template("off.html")

@app.route("/status")
def status():
    if(blueLED.is_lit):
        return render_template("on.html")
    else:
        return render_template("off.html")



#MAIN WEBPAGE
@app.route("/")
def hello():
    if(blueLED.is_lit):
        return render_template("main.html", brightness=variables['currBrightness'] * 100)
    else:
        return render_template("main.html", brightness=0)

   


#background processses that happen without any refreshing

#Change brightness
@app.route('/set_brightness',methods=['GET', 'POST'])
def setBrightness():
    if request.method == 'POST':
        updateBrightness(float(request.form['myBrightness']) / 100)

    #Return nothing. 204 is the HTTP empty response
    return ('', 204)



#Toggle Power
#@app.route('/toggle_power', methods=['POST'])
#def toggle_power():



#NEW CODE

@app.route('/setColor', methods=['POST'])
def setColor():
    #if request.method == 'POST':
        




    print("hello")
    return ('', 204)








if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=False, use_reloader=False)

