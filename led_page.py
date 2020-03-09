from flask import Flask, request, render_template, json, g

from variables import *

app = Flask(__name__)

#MAIN WEBPAGE. Returns main.html with the values for the current led state
@app.route("/")
def main():
    currColor = variables['controller'].get_rgba()
    return render_template("main.html", currPower=variables['controller'].is_lit(),
                                        currAlpha=currColor.alpha * 100,
                                        currRed=currColor.red * 100,
                                        currGreen=currColor.green * 100,
                                        currBlue=currColor.blue * 100
    )


@app.route('/setColor', methods=['POST'])
def setColor():
    if request.method == 'POST':
        color = rgba(
            float(request.form['myRed']) / 100,
            float(request.form['myGreen']) / 100,
            float(request.form['myBlue']) / 100,
            float(request.form['myAlpha']) / 100,
        )   
        variables['controller'].set_rgba(color)
        if request.form.get('myPower'):
            variables['controller'].on()
        else:
            variables['controller'].off()       

    return ('', 204)


###########################
#######ALEXA REQUESTS########
###########################
@app.route("/on")
def alexaOn():
    variables['controller'].on()
    return "ON"

@app.route("/off")
def alexaOff():
    variables['controller'].off()
    return "OFF"

@app.route("/status")
def status():
    if(variables['controller'].is_lit()):
        return "ON"
    else:
        return "OFF"








if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=False, use_reloader=False)

