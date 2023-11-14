from .paceENSDF import *
from .base_ensdf import *
from .normalization import Normalization
from .parent import Parent
from .daughter import Daughter
from .beta_minus import BetaMinus
from .electron_capture_beta_plus import ElectronCaptureBetaPlus
from .alpha import Alpha
from .gamma_gamma import GammaGamma
from .gamma_x import GammaX

__version__="0.4.0"
__author__="Aaron M. Hurst"

import os
_ROOT = os.path.abspath(os.path.dirname(__file__))
def get_data(path):
    """Function to return absolute path of the data files inside the root of 
    the Python package."""
    return os.path.join(_ROOT, path)

print("The JSON-formatted ENSDF-decay data sets live in directory:\n {0}".format(get_data('ENSDF_JSON')))
print("The JSON-formatted coincidence decay-data sets live in directory:\n {0}".format(get_data('PACE_JSON')))
