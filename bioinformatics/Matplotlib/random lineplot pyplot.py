import random as r
from matplotlib import pyplot as plt

print(plt.style.available)
plt.style.use('fivethirtyeight')

list_x = [0]
list_y = [0]
for x in range(100):
    list_x.append(r.randint(1, 100) - r.randint(1, 50))
    list_y.append(1+list_y[x])

plt.plot(list_y, list_x, color = 'b', linestyle='--',label = 'first rand', linewidth = .9)

plt.xlabel('x label')
plt.ylabel('y label')
plt.title('random graph')

for x in range(100):
    list_x[x] = (r.randint(1, 100))
    list_y[x] = (1 + list_y[x])

print(list_y)
plt.plot(list_y, list_x, color = 'g', linestyle = '-',label='second rand', linewidth = .9)
plt.show()
