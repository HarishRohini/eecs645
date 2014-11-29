__author__ = 'harishrohini'
from ..instructionstages.IF import *
from ..instructionstages.ID import *
from ..instructionstages.A1 import *
from ..instructionstages.A2 import *
from ..instructionstages.A3 import *
from ..instructionstages.A4 import *
from ..instructionstages.MEM import *
from ..instructionstages.WB import *


class Add:
    def __init__(self):
        self.IF = IF()
        self.ID = ID()
        self.A1 = A1()
        self.A2 = A2()
        self.A3 = A3()
        self.A4 = A4()
        self.MEM = MEM()
        self.WB = WB()

if __name__ == '__main__':
    ad = Add()
