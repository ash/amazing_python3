# Using C functions
import ctypes

mod = ctypes.CDLL('func.so')
res = mod.func(10, 20)
print(res) # 30