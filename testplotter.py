import matplotlib.pyplot as plt
import numpy as np
import csv

import pandas
df = pandas.read_csv('book2.csv')
print(type(df))
# # generate 2 2d grids for the x & y bounds
# y, x = np.meshgrid(np.linspace(0, 3, 1000), np.linspace(0, 3, 1000))


# z = (1 - x / 2. + x ** 5 + (y) ** 3) * np.exp(-x ** 2 - y ** 2)
# # x and y are bounds, so z should be the value *inside* those bounds.
# # Therefore, remove the last value from the z array.




# z = z[:-1, :-1]
# z_min, z_max = -np.abs(z).max(), np.abs(z).max()

fig, ax = plt.subplots()

c = ax.pcolormesh(df, cmap='RdYlGn', vmin=0, vmax=0.25)
ax.set_title('Data Collected at Scan Area A-1')
# # set the limits of the plot to the limits of the data
#ax.axis([x.min(), x.max(), y.min(), y.max()])

fig.colorbar(c, ax=ax)
#fig.set_label('Thickness (unit)')
ax.set_xlabel('Transducter Displacement (unit)')
ax.set_ylabel('Machine Displacement (unit)')
plt.show()