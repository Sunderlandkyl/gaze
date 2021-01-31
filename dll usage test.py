from ctypes import *
from comtypes.automation import VARIANT
# solution found here: https://stackoverflow.com/questions/48389060/can-one-have-python-receive-a-variable-length-string-array-from-c/48481504#48481504

mydll = cdll.LoadLibrary("C:\\Users\\Sahar Abdalla\\Documents\\uoft\\capstone\\GazeFlowAPI.dll")
mydll.Coordinates.argtypes = [POINTER(VARIANT)]
v = VARIANT()
mydll.Coordinates(v)
if v:
    for x in v.value:
        print("doot\t")
        print(x)
else:
    print("val of data is NONE")