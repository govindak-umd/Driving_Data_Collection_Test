"""Code to save quaternion data to a txt file without plotting

Attributes:
    ser (TYPE): Serial
"""
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
import math
from utils import test_name

# For Linux systems

# ser = serial.Serial('/dev/ttyUSB1')

# For Windows

ser = serial.Serial('COM12')

ser.baudrate = 9600


f = open(test_name +"quaternion_data.txt", "w+")


try:

    while True:

        # Convert from ascii encoding

        imu_data = ser.readline().decode("ascii")

        # Split at the tab

        imu_data_list = imu_data.split('\t')

        # Remove off the '\r\n' at the end of the line

        imu_data_list.pop()

        # Show in the terminal
        print('Quaternion data : ', imu_data_list)
        f.write(str(time.strftime('%H:%M:%S')) + ' ' + str(imu_data_list[0]) + ' ' + str(imu_data_list[1]) + ' ' + str(
            imu_data_list[2]) + ' ' + str(
            imu_data_list[3]) + "\n")

# Save when the user exits
except KeyboardInterrupt:
    print('File closed and saved upon user request')
    f.close()
