import http

from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def test():
    return render_template("test.html")

#rendering the HTML page which has the button
@app.route('/json')
def json():
    return render_template('test.html')

#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return "nothing"

if __name__ == "__main__":
    app.run(threaded=True, host='0.0.0.0', port=8080)

