from .base_ensdf import *
from .normalization import Normalization
from .parent import Parent
from .daughter import Daughter
from .beta_minus import BetaMinus
from .electron_capture_beta_plus import ElectronCaptureBetaPlus
from .alpha import Alpha
from .gamma_gamma import GammaGamma
from .gamma_x import GammaX

class ENSDF(GammaX):
    __doc__="""Class to handle ENSDF decay data sets and methods in addition 
    to the derived coincidence gamma/gamma and gamma/X-ray data sets."""

    def __init__(self):
        BaseENSDF.__init__(self)
        Normalization.__init__(self)
        Parent.__init__(self)
        Daughter.__init__(self)
        BetaMinus.__init__(self)
        ElectronCaptureBetaPlus.__init__(self)
        Alpha.__init__(self)
        GammaGamma.__init__(self)
        GammaX.__init__(self)
