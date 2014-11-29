__author__ = 'harishrohini'
from ..instructionstages.IF import *
from ..instructionstages.ID import *
from ..instructionstages.M1 import *
from ..instructionstages.M2 import *
from ..instructionstages.M3 import *
from ..instructionstages.M4 import *
from ..instructionstages.M5 import *
from ..instructionstages.M6 import *
from ..instructionstages.M7 import *
from ..instructionstages.MEM import *
from ..instructionstages.WB import *


class Mul:
    def __init__(self):
        self.IF = IF()
        self.ID = ID()
        self.M1 = M1()
        self.M2 = M2()
        self.M3 = M3()
        self.M4 = M4()
        self.M5 = M5()
        self.M6 = M6()
        self.M7 = M7()
        self.MEM = MEM()
        self.WB = WB()
