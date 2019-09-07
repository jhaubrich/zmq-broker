import zmq
import time
from random import randint

if __name__ == "__main__":
    ctx = zmq.Context.instance()
    p = ctx.socket(zmq.PUB)
    p.connect("tcp://localhost:5555")
    i = 0

    while True:
        msg = 'sensor1 ' + str(randint(0,4095))
        p.send(msg.encode('utf-8'))
        time.sleep(.1)
