#!/usr/bin/env python

import mraa
import time
import pulsein
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
    def __init__(self, type = 'pluviometer' , unit = 'mm' , conv_ratio = 1 ,
                 file = 'pluviometer', timeint = 60, status = 1, gpio_pin = 4,
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

class Ultrasonic(Sensor) :
    "Defines methods to read from ultrasonic sensor"
    def __init__gpio(self, echo_pin, trigger_pin):
        self.echo_pin=mraa.Gpio(echo_pin)
        self.trigger_pin = mraa.Gpio(trigger_pin)
        self.echo_pin.dir(mraa.DIR_IN)
        self.trigger_pin.dir(mraa.DIR_OUT)
    def __init__(self, type = 'ultrasonic' , unit = 'cm' , conv_ratio = 58.2 ,
                 file = 'ultrasonic', timeint = 0.5, status = 1, echo_pin = 6,
                 trigger_pin = 5, max_range = 400, min_range = 0, initial_value=46.5):
        Sensor.__init__(self, type,unit,conv_ratio,file,timeint, status)
        self.__init__gpio(echo_pin, trigger_pin)
        self.max_range = max_range
        self.min_range = min_range
        self.initial_value = initial_value
    def thread(self, args):
        while True: 
            self.trigger_pin.write(0)
            time.sleep(0.000002) #2 microseconds
            self.trigger_pin.write(1)
            time.sleep(0.00001)  #10 microseconds
            self.trigger_pin.write(0)
            duration  = pulsein.pulseIn(self.echo_pin) # microseconds 
            ultrasonic_value.value = self.initial_value - (duration / self.conv_ratio) # distance
            if ultrasonic_value.value >= self.max_range or \
                ultrasonic_value.value <= self.min_range :
                print "Out of range {0}".format(ultrasonic_value.value)
                ultrasonic_value.value = -1
            else :
                print "Distance: {0} cm".format(ultrasonic_value.value)
            time.sleep(0.2)
    def thread_write(self, args):
        print 'time: {}'.format( self.timeint)
        while True:
            print "write:"
            if self.file <> '' :
                with open(self.file, 'w') as file :
                    file.write('{0}\n'.format(ultrasonic_value.value))
            time.sleep(self.timeint)
               
ultrasonic_value = Value('d',0.0) 
        
if __name__ == '__main__':
    pluviometer = Pluviometer('pluviometer','mm',1,'pluviometer', 10) 
    pluviometer_thread = Process(target=pluviometer.thread, args=(None,))
    pluviometer_write = Process (target=pluviometer.thread_write, 
                                 args=(None,))
    ultrasonic = Ultrasonic('ultrasonic','cm', 58.2, 'ultrasonic', 0.5)
    ultrasonic_thread = Process(target = ultrasonic.thread, args=(None,))
    ultrasonic_write = Process(target = ultrasonic.thread_write, args=(None,))
    ultrasonic_thread.start()
    ultrasonic_write.start()
    pluviometer_thread.start()
    pluviometer_write.start()

    try: 
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print "Good Bye! :)"
        pluviometer_thread.terminate()
        pluviometer_write.terminate()
        ultrasonic_thread.terminate()
        ultrasonic_write.terminate()

