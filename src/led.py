import mraa
import time

x = mraa.Gpio(13)
x.dir(mraa.DIR_OUT)

while True:
    for i in (1, 2, 3, 4):
	x.write(1)
        time.sleep(i)
        x.write(0)
        time.sleep(0.5)
