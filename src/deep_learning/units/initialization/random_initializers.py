import logging

import numpy as np
import scipy.stats as scs
import theano

from deep_learning.units.initialization.base_initializer import BaseInitializer


class RandomInitializer(BaseInitializer):
    """
    Returns a shared variable with random coefficients
    according to a certain distribution. Distribution is a
    scipy.stats distribution
    """
    logger = logging.getLogger(__name__ + "." + "RandomInitializer")

    def __init__(self, name, shape, distribution):
        super(RandomInitializer, self).__init__(name, shape)
        self.distribution = distribution
        self.shape = shape

    def create_shared(self, **kwargs):
        return theano.shared(self.distribution.rvs(self.shape), name=self.name, **kwargs)


class FanInOutInitializer(RandomInitializer):
    """
    Initializes a shared variable according to [INSERT REF]
    """
    logger = logging.getLogger("NormalizedRandomInitializer")

    def __init__(self, name, shape):
        self.logger.debug("Initializing {0} with shape {1}".format(name, shape))
        bound = np.sqrt(6. / np.sum(shape))
        super(FanInOutInitializer, self).__init__(name, shape,
                                                  scs.uniform(-bound, bound))