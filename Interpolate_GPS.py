import numpy as np
from utils import test_name

# Read the gps file coordinates

converted_gps_file = open(test_name + "gps_to_xy" + ".txt", "r")
# converted_gps_file = open("sample_5.txt", "r")
saved_imu_file = open(test_name + "quaternion_data" + ".txt", "r")

gps_lines = 0
gps_data_read = converted_gps_file.read()
for line in gps_data_read.split("\n"):
    if line:
        gps_lines += 1

imu_lines = 0
imu_data_read = saved_imu_file.read()
for line in imu_data_read.split("\n"):
    if line:
        imu_lines += 1

print('GPS Data Collected: ', gps_lines, '|| IMU Data Collected: ', imu_lines)

diff_factor = round(imu_lines / gps_lines)
print('Diff Factor is : ', diff_factor)
new_interpolated_gps_file = open(test_name + "INTERPOLATED_gps_data" + ".txt", "w+")

line_count = 0
last_x = []
last_y = []
last_z = []

for line in gps_data_read.split("\n"):

    input_line = line.split(" ")

    x = float(input_line[0])
    y = float(input_line[1])
    z = float(input_line[2])

    new_line_x = []
    new_line_y = []
    new_line_z = []
    if line_count != 0:
        prev_x = last_x[-1]
        x_linspace = np.linspace(prev_x, x, diff_factor, endpoint=True)

        for i in x_linspace:
            new_line_x.append(i)

        prev_y = last_y[-1]
        y_linspace = np.linspace(prev_y, y, diff_factor, endpoint=True)

        for i in y_linspace:
            new_line_y.append(i)

        prev_z = last_z[-1]
        z_linspace = np.linspace(prev_z, z, diff_factor, endpoint=True)

        for i in z_linspace:
            new_line_z.append(i)

        for idx in range(1,len(new_line_x)):
            new_interpolated_gps_file.write(
                str(x_linspace[idx]) + ' ' + str(y_linspace[idx]) + ' ' + str(z_linspace[idx]) + "\n")

        last_x.append(x)
        last_y.append(y)
        last_z.append(z)
        line_count += 1

    if line_count == 0:
        last_x.append(x)
        last_y.append(y)
        last_z.append(z)
        new_interpolated_gps_file.write(str(x) + ' ' + str(y) + ' ' + str(z) + "\n")
        line_count += 1
print("Interpolated file written : " + test_name + "INTERPOLATED_gps_data" + ".txt")