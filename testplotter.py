import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
from tkinter.filedialog import askopenfilename

# def plotter():
file_name = askopenfilename()
df = pd.read_csv(file_name)

print(df)

scan = df.scan_area   # this is where the AttributeError is flagged
X = df.x_coor
Y = df.y_coor
Z = df.thickness

previous_scan_unit = df.units[1]
previous_scan_name = df.scan_area[1]
print(previous_scan_name)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')       #     https://stackoverflow.com/questions/51891538/create-a-surface-plot-of-xyz-altitude-data-in-python
ax.plot_trisurf(X, Y, Z, cmap='RdYlGn')#, edgecolors='grey', alpha=0.5)
ax.scatter(X, Y, Z, c='black')
ax.set_title('Data Collected from Scan ' + previous_scan_name)
ax.set_xlabel('Transducer Displacement (' + previous_scan_unit +')')
ax.set_ylabel('Machine Displacement (' + previous_scan_unit +')')
ax.set_zlabel('Material Thickness (' + previous_scan_unit +')')

plt.show()


# plotter()