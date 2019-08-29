# zmq-controller
Listens for PI's writes to disk and legend-live API


We're probably looking at a [0MQ push/pull model](http://zguide.zeromq.org/page:all). (this thing is a book, don't hurt yourself.)


## pyzmq
https://zeromq.org/languages/python/

## virtualenv
Virtualenv allows us to manage python versions and libraries in userland. Decoupling it from the OS and its package manager. This is good.

### create a virtual environment for python
You only do this one time.
``` bash
git clone git@github.com:legendenergy/zmq-controller.git
cd zmq-controller
python3 -m venv .
```

### activate your virtual environment

Activate your project python environment for your current terminal.
``` bash
source bin/activate
# Check that it worked
which python
which pip
```

### install the python packages you need

``` bash
# first make sure pip is up to date
pip install pip --upgrade
pip install -r requirements.txt
```

## Handy Pip commands

``` bash
# install something
pip install <whatev>
# find something
pip search zmq
# install everything required by requirements.txt
pip install -r requirements.txt
# see what's installed
pip freeze
# save what pip installed to requirements.txt
pip freeze > requirements.txt
```
