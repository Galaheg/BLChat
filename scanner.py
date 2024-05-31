# bluetooth low energy scan
from bluetooth import *

def search_devices():
     nearby_devices = discover_devices(lookup_names=True)

     print ("found %d devices" % len(nearby_devices))

#     for addr, name in nearby_devices:
#          print(" %s - %s" % (addr, name))

     return nearby_devices

