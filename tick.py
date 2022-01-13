import bucket, units
import time
from connection import Connection
from bucket import Bucket, ConstantBucket

i = ConstantBucket(10000)
a = Bucket()
b = Bucket()
a.val = 1000

connections = []
connections.append(Connection(i,a,1))
connections.append(Connection(a,b,0.1))
connections.append(Connection(b,a,0.1))

lastTime = time.time()
while(True):
    time.sleep(.1)
    for conn in connections:
        conn.fro.ticked = True
        conn.to.tick()
    for conn in connections:
        conn.calcTake()
    nowTime = time.time()
    for conn in connections:
        conn.transfer(nowTime-lastTime)
    lastTime = time.time()
    print(a.val)