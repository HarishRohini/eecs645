__author__ = 'harishrohini'
from ..instructionstages.IF import *
from ..instructionstages.ID import *
from ..instructionstages.EX import *
from ..instructionstages.MEM import *
from ..instructionstages.WB import *


class Store:
    def __init__(self):
        self.IF = IF()
        self.ID = ID()
        self.EX = EX()
        self.MEM = MEM()
        self.WB = WB()
