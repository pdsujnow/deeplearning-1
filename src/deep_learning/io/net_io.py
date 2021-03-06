import pickle

from src.deep_learning import create_net_from_dict


def save_net(filename, nnet, parameters=None, protocol=2):
    f = open(filename, "wb")
    pickle.dump(nnet.name, f, protocol=protocol)
    pickle.dump(nnet.definition(), f, protocol=protocol)
    if parameters is None:
        params = nnet.params
    else:
        params = parameters

    for param in params:
        pickle.dump(param, f, protocol=protocol)
    f.close()


def load_net(filename):
    f = open(filename, "rb")
    name = pickle.load(f)
    definition = pickle.load(f)
    nnet = create_net_from_dict(name, definition)
    for param in nnet.params:
        v = pickle.load(f)
        param.set_value(v)
    return nnet