import numpy as np
from numpy import sort
from numpy import argsort
import matplotlib.pyplot as plt

from waterfilling import GWF

power = 6
a = np.array([1,1/3,1/4,1/2])
w = np.ones(4)

water_level, index, value, si, height = GWF(power, a, w)

print('water_level = ' + str(water_level))
print('index = ' + str(index))
print('value = ' + str(value))
print('si = ' + str(si))
print('height = ' + str(height))


# plot

plt.figure(figsize=(8,6))

axes = plt.axes()
axes.set_xlim([0,5])
axes.set_ylim([0,np.max(1/a)])

left = np.arange(1,5)
plt.xlabel('Channels', fontsize=16)
plt.bar(left,height,width=1.0,linewidth=2,color="#1E7F00",edgecolor='black',label='1/ai')
plt.bar(left,si/w,width=1.0,bottom=height,linewidth=2,color='r',edgecolor='black',label='si'
)
plt.legend(loc='upper right', borderaxespad=1, fontsize=14)

plt.savefig('result.png')