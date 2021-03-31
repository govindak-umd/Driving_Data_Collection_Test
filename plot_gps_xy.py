import numpy as np
from utils import test_name
from matplotlib import pyplot as plt

# Open a new file that stores the converted file coordinates

# gps_file = open(test_name + "gps_to_xy" + ".txt", "r")
gps_file = open(test_name + "INTERPOLATED_gps_data" + ".txt", "r")

print("Reading from " + test_name + "INTERPOLATED_gps_data" + ".txt" )
x_list = []
y_list = []

for line in gps_file:
    input_line = line.split(' ')
    x_coord = float(input_line[0])
    y_coord = float(input_line[1])
    x_list.append(x_coord)
    y_list.append(y_coord)

plt.plot(x_list, y_list)
# plt.savefig('Images/'+ str(test_name) + 'plot.png')
plt.show()
