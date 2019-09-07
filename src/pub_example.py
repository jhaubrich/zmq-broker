import zmq
import time
from random import randint

if __name__ == "__main__":
    ctx = zmq.Context.instance()
    p = ctx.socket(zmq.PUB)
    # p.connect("tcp://45.79.47.159:5555")
    p.connect("tcp://localhost:5555")

    while True:
        msg = '0000 ' + str(randint(1000,4095)) # 500 kbps
        msg = '0 ' + str(randint(1,9)) # 430 kbps
        msg = 'sensor1 ' + str(randint(0,4095))
        p.send(msg.encode('utf-8'))
        time.sleep(.1)
