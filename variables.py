#Global Variables
variables = {}
variables['currBrightness'] = 1


def updateBrightness(newVal):
    variables['currBrightness'] = newVal
    led.value = variables['currBrightness']

def on():
    led.value = currBrightness

def off():
    currBrightness = led.value
    led.off()


