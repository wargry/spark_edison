import mraa
import time
import random

def color(R, G, B):
    x = mraa.I2c(0)    
    x.address(0x62)    
                   
    # initialise device
    x.writeReg(0, 0)     
    x.writeReg(1, 0)      
                      
    # sent RGB color data 
    x.writeReg(0x08, R)
    x.writeReg(0x04, G)
    x.writeReg(0x02, B)
    x.write('Hola')
	
# This example will change the LCD backlight on the Grove-LCD RGB backlight
# to a nice shade of purple

while True:
    R = random.randint(1, 255)
    G = random.randint(1, 255)
    B = random.randint(1, 255)
    color(R,G,B)
    time.sleep(0.5)

