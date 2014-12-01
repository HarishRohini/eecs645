__author__ = 'harishrohini'


class Registers:
    r = {'R'+str(n): {'used': False, 'contents': 0, 'execution': False, 'is_mul': False,
                      'is_add': False, 'is_store': False} for n in range(0, 32)}
    f = {'F'+str(n): {'used': False, 'contents': 0, 'execution': False, 'is_mul': False,
                      'is_add': False, 'is_store': False} for n in range(0, 32)}