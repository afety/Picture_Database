#coding:utf8
#file is used to store some const string


import sys

class _const:
    class ConstError(TypeError): pass
    class ConstCaseError(ConstError): pass

    def __setattr__(self, key, value):
        if self.__dict__.has_key(key):
            raise self.ConstError, 'cannot change const %s'% key
        if not key.isupper():
            raise self.ConstCaseError, ' const name is not all upper'
        self.__dict__[key] = value


sys.modules[__name__] = _const()
