from flask import Flask
from flask_ask import Ask, statement
import RPi.GPIO as GPIO
 
app = Flask(__name__)
ask = Ask(app, '/')
 
@ask.intent('LedIntent')
def led(color, status):
  if color.lower() not in pins.keys():
    return statement("I don't have {} light".format(color)) 
  GPIO.output(pins[color], GPIO.HIGH if status == 'on' else GPIO.LOW)
  return statement('Turning the {} light {}'.format(color, status))
 
if __name__ == '__main__':
  try:
    GPIO.setmode(GPIO.BCM)
    pins = {'red':0, 'yellow':1, 'green':2}
    for pin in pins.values(): 
      GPIO.setup(pin, GPIO.OUT)
    app.run(debug=True)
  finally:
    GPIO.cleanup()