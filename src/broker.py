"""

   Simple message queuing broker

"""

import zmq


def main():
    """ main method """

    context = zmq.Context()

    # Socket facing clients
    frontend = context.socket(zmq.XSUB)
    frontend.bind("tcp://*:5555")

    # Socket facing services
    backend  = context.socket(zmq.XPUB)
    backend.bind("tcp://127.0.0.1:6666")

    zmq.proxy(frontend, backend)


if __name__ == "__main__":
    main()
