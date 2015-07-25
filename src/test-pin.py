#!/usr/bin/env python

import mraa
 
x = mraa.Gpio(3)
x.dir(mraa.DIR_IN)
print x.read()

