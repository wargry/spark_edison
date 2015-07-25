#!/usr/bin/env python

import mraa
import time
from  multiprocessing import Value, Process, Lock

class Sensor:
    "Defines Sensor attributes and methods"

    def __init__(self, type = '' , unit = '' , conv_ratio = 1 ,  
                 file = '', timeint = 60, status = 1) :
        self.type = type
        self.unit = unit
        self.conv_ratio = conv_ratio
        self.file = file 
        self.timeint = timeint
        self.status = status
    def thread(self, args):
        return 
    def __init__gpio(self):
        return
    def thread_write(self, args):
        return


class Pluviometer(Sensor):
    "Defines methods to read from pluviometer"
    
    def __init__gpio(self, gpio_pin, gpio_dir):
        self.gpio = mraa.Gpio(gpio_pin)
        self.gpio.dir(gpio_dir)
    def __init__(self, type = '' , unit = '' , conv_ratio = 1 ,
                 file = '', timeint = 60, status = 1, gpio_pin = 4,
                 gpio_dir = mraa.DIR_IN) : 
        Sensor.__init__(self, type, unit, conv_ratio, file,timeint, status) 

        self.__init__gpio(gpio_pin, gpio_dir)
    def thread(self, args):
        print 'Hello from thread_pluv'
        self.gpio.isr(mraa.EDGE_RISING, pluviometer_interrupt,
                      pluviometer_interrupt)
        while True:
            time.sleep(1)
    def thread_write(self, args):
        print 'time: {}'.format( self.timeint)
        while True:
            lcounter = pluviometer_value.value
            with pluviometer_lock:
                print "write: unlocked"
                #pluviometer_value.value = 0
            measure = lcounter * self.conv_ratio
            print "write: {0}, {1} mm".format(lcounter, measure)
            if self.file <> '' : 
                with open(self.file, 'w') as file :
                    file.write('{0}\n'.format(measure))
            time.sleep(self.timeint)

# Pluviometer Global definitions

pluviometer_value= Value('i',0)
pluviometer_lock = Lock()

def pluviometer_interrupt(args):
    print 'Touched!!!'
    with pluviometer_lock:
        pluviometer_value.value += 1
    print "interrupt: {0}".format(pluviometer_value.value)

 
if __name__ == '__main__':
    pluviometer = Pluviometer('pluviometer','mm',1,'pluviometer', 10) 
    pluviometer_thread = Process(target=pluviometer.thread, args=(None,))
    pluviometer_write = Process (target=pluviometer.thread_write, 
                                 args=(None,))
    pluviometer_thread.start()
    pluviometer_write.start()
    try: 
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print "Good Bye! :)"
        pluviometer_thread.terminate()
        pluviometer_write.terminate()

