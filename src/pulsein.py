import mraa
import time 
#x = mraa.Gpio(6)
#x.dir(mraa.DIR_IN)
#res = 0.000147
# wait for low state
def pulseIn(pin):
    while not pin.read():
#	print "High"
        continue
    # Went down, let start measure
    start = time.time()

    while pin.read():
        continue

    end = time.time()
    return (end - start) *1000000

#while True:
#    elapsed = pulseIn(x)
#    print elapsed
#    print elapsed / res
#    time.sleep(0.5)





