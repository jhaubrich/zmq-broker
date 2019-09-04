import zmq


if __name__ == "__main__":
    ctx = zmq.Context.instance()

    subscriber = ctx.socket(zmq.SUB)
    subscriber.connect("tcp://localhost:6666")
    subscriber.setsockopt(zmq.SUBSCRIBE, b"")

    while True:
        print(subscriber.recv())
