import mraa
import time

DELTA_T = 0.2
RES = 0.00976
VCC = 5.0

#print (mraa.getVersion())


def get_height():
    try:
        x = mraa.Aio(0)
        sen_value = x.read()
    except:
        print ("Are you sure you have an ADC?")

    time.sleep(DELTA_T)

    # Compute height in inches
    height_inch = (sen_value * VCC) / (1023 * RES)
    
    # Compute heigth in centimeters
    height_cm = height_inch * 2.54

    # Return height value
    return height_cm

while True:
    height = get_height()
    print("{0} cm".format(get_height()))
