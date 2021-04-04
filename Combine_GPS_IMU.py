import numpy as np
from utils import test_name

new_interpolated_gps_file = open(test_name + "INTERPOLATED_gps_data" + ".txt", "r")
gps_data_read = new_interpolated_gps_file.read()

saved_imu_file = open(test_name + "quaternion_data" + ".txt", "r")
imu_data_read = saved_imu_file.read()

# Prepare data for writing to a combined file

gps_data = []
for line in gps_data_read.split("\n"):
    input_line = line.split(" ")
    x = input_line[0]
    y = input_line[1]
    z = input_line[2]
    gps_data.append([x, y, z])

imu_data = []
for line in imu_data_read.split("\n"):
    input_line = line.split(" ")
    time = input_line[0]
    x = input_line[1]
    y = input_line[2]
    z = input_line[3]
    w = input_line[4]
    imu_data.append([time, x, y, z, w])

# Writes the TUM File with combined GPS and IMU Data
tum_file = open(test_name + "TUM_FORMAT" + ".txt", "w+")

dummy_time = 0.0
for i in range(len(gps_data)):
    tum_file.write(
        str(dummy_time) + ' ' + str(gps_data[i][0]) + ' ' + str(gps_data[i][1]) + ' ' + str(gps_data[i][2]) + ' ' \
        + str(imu_data[i][1]) + ' ' + str(imu_data[i][2]) + ' ' + str(imu_data[i][3]) + ' ' + str(
            imu_data[i][4]) + "\n")
    dummy_time+=0.2
saved_imu_file.close()
new_interpolated_gps_file.close()
tum_file.close()

print("Combined GPS + IMU file written : " + test_name + "TUM_FORMAT" + ".txt")
