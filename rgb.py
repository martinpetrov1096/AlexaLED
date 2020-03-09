from gpiozero import PWMLED
from time import sleep

class rgba:
    def __init__(self,r,g,b,a):
        self.red = r
        self.green = g
        self.blue = b
        self.alpha = a



class rgbController:
    
    #r,g, and b have values in the interval of [0,1]
    def __init__(self, pins, rgba):
        self.rLED = PWMLED(pins[0])
        self.gLED = PWMLED(pins[1])
        self.bLED = PWMLED(pins[2])
        #Initial color for the rgb strip
        self.set_rgba(rgba)

    def on(self):
        self.__update()

    def off(self):
        self.rLED.off()
        self.gLED.off()
        self.bLED.off()

    def is_lit(self):
        if self.rLED.is_lit or self.gLED.is_lit or self.bLED.is_lit:
            return True
        else:
            return False

    def get_rgba(self):
        return self.rgba

    #Sets the color for 
    def set_rgba(self,rgba):
        self.rgba = rgba
        self.__update()

    #Private helper method to update the strip to the current values
    def __update(self):
        self.rLED.value = self.rgba.red * self.rgba.alpha
        self.gLED.value = self.rgba.green * self.rgba.alpha
        self.bLED.value = self.rgba.blue * self.rgba.alpha


def main():
    rgbStrip = rgbController([17,18,27], rgba(1,0,0,1))

    while(1):
        rgbStrip.on()
        sleep(1)
        rgbStrip.set_rgba(rgba(1,1,1,1))
        sleep(1)
        rgbStrip.set_rgba(rgba(0,0,1,1))
        sleep(1)
    
if __name__== "__main__":
    main()
