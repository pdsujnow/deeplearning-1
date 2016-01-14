import numpy as np

# type of supported initializers
from deep_learning.units.initialization.constant_initializer import ConstantInitializer
from deep_learning.units.initialization.random_initializers import FanInOutInitializer
from deep_learning.units.initialization.random_initializers import RandomInitializer


class ParametersInitializers:
    ConstantInitializer = "constant"
    RandomInitializer = "random"
    FanInOutInitializer = "faninout"

def create_constant_initializer(name, shape, **kwargs):
    return ConstantInitializer(name, shape, kwargs["value"])


def create_random_initializer(name, shape, **kwargs):
    return RandomInitializer(name, shape, kwargs["distribution"])


def create_faninout_initializer(name, shape, **kwargs):
    return FanInOutInitializer(name, shape)

param_to_init = {
    ParametersInitializers.ConstantInitializer: create_constant_initializer,
    ParametersInitializers.RandomInitializer: create_random_initializer,
    ParametersInitializers.FanInOutInitializer: create_faninout_initializer
}

def create_initializer(name, shape, **kwargs):
    if isinstance(shape, int):
        shape = np.array((shape,))
    elif isinstance(shape, np.ndarray):
        assert np.issubdtype(shape.dtype, int), "Array should contain integer types"
    elif isinstance(shape, (list, tuple)):
        # check all integers
        assert np.all([np.issubdtype(type(x), int) for x in shape]), "All elements should be integers"
    else:
        raise ValueError("Unknown type for shape")

    assert "initializer" in kwargs, "You need an 'initializer' in the parameters"

    return param_to_init[kwargs["initializer"]](name, shape, **kwargs)
