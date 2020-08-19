from ctypes import *

flib = cdll.LoadLibrary("../bin/libsimulation.dll")
prototype = CFUNCTYPE(c_double,c_double,c_double)

def estPi(a,b):
    f=prototype(("estPi",flib))
    result=f(a,b)
    return result
    
