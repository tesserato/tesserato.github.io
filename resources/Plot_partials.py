import numpy as np
import matplotlib.pyplot as plt

partials = 3
first_key = 1
last_key = 88

Y = []
for key in range(first_key, last_key + 1):
  f0 = np.power(2, (key - 49) / 12) * 440
  y = []
  for partial in range(1, partials + 1):
    y.append(f0 * partial)
  Y.append(y)

Y = np.array(Y).T

fig = plt.figure()
fig.set_size_inches(400 / fig.dpi, 2000 / fig.dpi)
plt.xlabel('Frequências Parciais')
# plt.ylabel('Teclas')
plt.plot(Y, 'k.-')
plt.savefig('Partials.png')
plt.show()
plt.close()
exit()