# Work in Python 3.9.1
# Dependences: Numpy


import numpy as np
from numpy import sort
from numpy import argsort

def GWF(power,gain,weight):
    power = power
    count = 0
    a = sort(gain)[::-1]
    w = weight
    height = sort(1/(w*a))
    # print(height)
    ind = argsort(1/(w*a))
    weight = weight[ind]
    # print(weight)

    original_size=len(a)-1 #size of gain array, i.e., total # of channels.
    channel=len(a)-1
    isdone=False

    while isdone == False:
        Ptest=0 # Ptest is total 'empty space' under highest channel under water.
        for i in range(channel):
            Ptest += (height[channel] - height[i]) * weight[i]
            # print(Ptest)
            # print(height)
        if (power - Ptest) >= 0: # If power is greater than Ptest, index (or k*) is equal to channel.
            index = channel      # Otherwise decrement channel and run while loop again.
            # print(index)
            break
        
        channel -= 1
    # print('index = ' + str(index))
    # print(height)
    value = power - Ptest        # 'value' is P2(k*)
    # print(value)
    water_level = value/np.sum([weight[range(index+1)]]) + height[index]
    # print(weight[range(index)])
    # print('sum = ' + str(np.sum(weight[range(index)])))
    si = (water_level - height) * weight
    si[si < 0] = 0
    return water_level,index,value,si,height