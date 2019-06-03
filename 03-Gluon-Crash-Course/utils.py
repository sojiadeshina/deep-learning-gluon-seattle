import matplotlib.pyplot as plt
from matplotlib.pylab import imshow
import numpy as np
import mxnet as mx
from mxnet import nd
from mxnet import gluon
from mxnet import autograd
from notebook.services.config import ConfigManager
cm = ConfigManager()
cm.update('livereveal', {
              'width': 1000,
              'height': 800,
              'scroll': True,
})
import os
import tarfile
