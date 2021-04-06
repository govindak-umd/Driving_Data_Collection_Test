"""Code to read GPS Data through pyserial

Attributes:
    ser (TYPE): Serial
"""
import serial
from utils import test_name

# For Linux systems

# ser = serial.Serial('/dev/ttyUSB0')

# For Windows

ser = serial.Serial('COM4')

ser.baudrate = 9600

f = open(test_name + "gps_data.txt", "w+")

try:

    while ser.isOpen():

        # Convert from ascii encoding

        imu_data = ser.readline().decode("ascii")

        data_code = imu_data[0:3]

        # Getting the Lattitude data and split it at the right
        # parsing points

        if data_code == 'Lat':
            lat_data = ((imu_data.split(': ')[1]).split('\r\n'))[0]
            f.write(str(lat_data) + ' ')
            print(lat_data)

        # Getting the Longitude data and split it at the right
        # parsing points

        if data_code == 'Lon':
            lon_data = ((imu_data.split(': ')[1]).split('\r\n'))[0]
            f.write(str(lon_data) + ' ')
            print(lon_data)

        # Getting the Altitude data and split it at the right
        # parsing points

        if data_code == 'Alt':
            alt_data = ((imu_data.split(': ')[1]).split('\r\n'))[0]
            f.write(str(alt_data) + ' ')
            print(alt_data)

        # Getting the TimeStamp data and split it at the right
        # parsing points

        if data_code == 'Tim':

            tim_data = ((imu_data.split(': ')[1]).split('\r\n'))[0]
            f.write(str(tim_data) + " \n")
            print(tim_data)

        else:

            print('Waiting for Lock .. ')
# Save when the user exits

except KeyboardInterrupt:

    print('File closed and saved upon user request')
    f.close()
