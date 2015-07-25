#!/usr/bin/env python

import mraa
import time

class Counter:
  count = 0

c = Counter()

# inside a python interupt you cannot use 'basic' types so you'll need to use
# objects
def test(args):
  print("wooo")
  c.count+=1
  print c.count

x = mraa.Gpio(4)
x.dir(mraa.DIR_IN)

while True:
    x.isr(mraa.EDGE_BOTH, test, test)

