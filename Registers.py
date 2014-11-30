__author__ = 'harishrohini'


class Registers:
    r = {'R'+str(n): {'used': False, 'contents': 0} for n in range(0, 32)}
    f = {'F'+str(n): {'used': False, 'contents': 0} for n in range(0, 32)}