from gpiozero import PWMLED
from rgb import *
#Global Variables
variables = {}
variables['currBrightness'] = 1

'''
blueLED= PWMLED(27)


def updateBrightness(newVal):
    variables['currBrightness'] = newVal
    blueLED.value = variables['currBrightness']

def on():
    blueLED.value = variables['currBrightness']

def off():
    variables['currBrightness'] = blueLED.value
    blueLED.off()
'''


#NEW CODE

variables['controller'] = rgbController([17,18,27], rgba(1,1,1,1))