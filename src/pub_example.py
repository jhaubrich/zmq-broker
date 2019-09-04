import zmq
import time

if __name__ == "__main__":
    ctx = zmq.Context.instance()
    p = ctx.socket(zmq.PUB)
    p.connect("tcp://localhost:5555")
    i = 0
    while True:
        i += 1
        msg = "hello!! #" + str(i)
        p.send(msg.encode('utf-8'))
        time.sleep(1)
