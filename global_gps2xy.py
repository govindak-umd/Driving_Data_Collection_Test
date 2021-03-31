import numpy as np
from utils import test_name

# Read the original gps file coordinates

orig_gps_file = open(test_name+"gps_data.txt", "r")

# Open a new file that stores the converted file coordinates

converted_gps_file = open(test_name + "gps_to_xy" + ".txt", "w+")


def readAndSave(lat=None, lon=None, init_lat=None, init_lon=None, ):
    """
    Convert latitudes and longitudes to
    x,y and z coords in the local frame
    :param lat: Float
    :type lat: Float
    :param lon: Float
    :type lon: Float
    :param init_lat: Float
    :type init_lat: Float
    :param init_lon: Float
    :type init_lon: Float
    :return: Float
    :rtype: Float
    """

    lat, lon = np.deg2rad(lat), np.deg2rad(lon)
    R = 6378  # radius of the earth
    x = R * np.cos(lat) * np.cos(lon)
    y = R * np.cos(lat) * np.sin(lon)
    z = R * np.sin(lat)

    if init_lon is not None and init_lat is not None:
        init_lat, init_lon = np.deg2rad(init_lat), np.deg2rad(init_lon)
        x_init = R * np.cos(init_lat) * np.cos(init_lon)
        y_init = R * np.cos(init_lat) * np.sin(init_lon)
        z_init = R * np.sin(init_lat)
        return x - x_init, y - y_init, z - z_init

    return x, y, z


line_count = 0
for line in orig_gps_file:
    input_line = line.split(' ')
    lat_in = float(input_line[0])
    lon_in = float(input_line[1])

    if line_count == 0:

        orig_lat = lat_in
        orig_lon = lon_in
        x_coord, y_coord, z_coord = readAndSave(lat_in, lon_in, orig_lat, orig_lon)

    else:

        x_coord, y_coord, z_coord = readAndSave(lat_in, lon_in, orig_lat, orig_lon)

    converted_gps_file.write(str(x_coord) + ' ' + str(y_coord) + ' ' + str(z_coord) + "\n")
    line_count += 1
orig_gps_file.close()
converted_gps_file.close()
print('Longitude, Latitude and Altitude saved in x,y, and z coordinates.')
