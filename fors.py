def process(a: int):
    print(a)

# Use **kwargs to cleanly accept any dynamic dictionary arguments
def fors(_restarts, procs):
    frommm = _restarts['frommm']
    intos = _restarts['intos']
    steeps = _restarts['steeps']
    while frommm < intos:
        procs(frommm)
        frommm += steeps

_restarts = {'frommm': 0, 'intos': 10, 'steeps': 1}

# Explicitly unpack the dictionary using **
fors(_restarts,process)