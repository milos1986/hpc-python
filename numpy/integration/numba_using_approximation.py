# adapted from:
# https://github.com/dmonkoff/hpc-python/blob/master/numpy/integration/numbaTest.py
'''
It's pure numpy implementation, numba normal and numba vectorized. Non-vectorized
numba seems quite slow (don't know why, not that good with numba), but vectorized
and parallized version is 3-5 times faster than numpy implementation on my computer
'''
import numpy as np
import math
from time import time
from numba import vectorize,njit
from functools import wraps

def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            return func(*args, **kwargs)
        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Total execution time: {end_ if end_ > 0 else 0} ms")
    return _time_it

@vectorize('float64(float64)',target='parallel')
def computeRiemanNumbaVec(dx):
    x = np.arange(dx/2,np.pi/2-dx/2,dx)
    S = np.sum(np.sin(x))*dx
    return S

@njit(parallel = True)
def computeRiemanNumbaJit(dx):
    x = np.arange(dx/2,np.pi/2-dx/2,dx)
    S = np.sum(np.sin(x))*dx
    return S

def computeRieman(dx):
    x = np.arange(dx/2,np.pi/2-dx/2,dx)
    S = np.sum(np.sin(x))*dx
    return S

@measure
def func1():
    for dx in np.geomspace(0.001,1,200):
        computeRieman(dx)
@measure
def func2():
    for dx in np.geomspace(0.001,1,200):
        computeRiemanNumbaJit(dx)
@measure
def func3():
   dx = np.geomspace(0.001,1,200)
   computeRiemanNumbaVec(dx)

computeRiemanNumbaJit(1.0)
print('computeRiemanNumbaJit(1.0) done')

func1()
# end2 = time.time()
# print('Elapsed time:', end2 - end)
print('func1() done')
func2()
# end3 = time.time()
# print('Elapsed time:', end3 - end2)
print('func2() done')
func3()
# end4 = time.time()
# print('Elapsed time:', end4 - end3)
print('func3() done')