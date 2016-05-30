__author__ = 'tanghan'
import matlab.engine
eng = matlab.engine.start_matlab()
t = eng.gcd(100.0, 80.0, nargout=3)
print (t)