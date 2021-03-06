import logging
import numpy as np
import matplotlib.pyplot as plt

import theano.tensor as T

from data_generation.gaussian_mixtures import generate_random_clouds
from deep_learning.nets.mlp import MLP
from deep_learning.training.gradient_descent import StochasticGradientDescent
from deep_learning.training.losses import cross_entropy
from deep_learning.training.updates.vanilla_update import VanillaUpdate
from deep_learning.units.activation.tanh_activation import TanhActivation

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

learning_parameters = {
    "minibatch": 10,
    "max_iter": 500,
    "learning_rate": 0.1,
}

n_classes = 3
mlp = MLP("mlp", 2, 10, n_classes, activation=TanhActivation())

sgd = StochasticGradientDescent(loss=cross_entropy,
                                learning_parameters=learning_parameters)

np.random.seed(12)
X, Y = generate_random_clouds(1000, n_classes, 2, 2)

sgd.fit(mlp, X, Y.astype(np.int32))

""" Drawing stuff """

xmin = np.min(X[:, 0]) - 0.5
xmax = np.max(X[:, 0]) + 0.5
ymin = np.min(X[:, 1]) - 0.5
ymax = np.max(X[:, 1]) + 0.5

h = 0.02
xx, yy = np.meshgrid(np.arange(xmin, xmax, h),
                     np.arange(ymin, ymax, h))

predict = mlp.predict(np.column_stack((xx.ravel(), yy.ravel())))
Z = np.argmax(predict, axis=1)
Z = np.reshape(Z, xx.shape)

plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8, interpolation='nearest')
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)
plt.xlim([xmin, xmax])
plt.ylim([ymin, ymax])
plt.show()