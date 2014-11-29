__author__ = 'harishrohini'


class Registers:
    def __init__(self):
        self.r = {'R'+str(n): {'used': 0, 'contents': 0} for n in range(0, 32)}
        self.f = {'F'+str(n): {'used': 0, 'contents': 0} for n in range(0, 32)}


