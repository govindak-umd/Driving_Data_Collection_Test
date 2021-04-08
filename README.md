# Driving_Data_Collection_Test
This repository shows how to get combined IMU, GPS, and Video data for ORB-SLAM2 and ORB-SLAM3 verification testing

## Steps to run

Attached the ```IMU +  GPS``` Module onto the vehicle as shown below:

Attach the camera to face forwards in such an angle as to grab features

### There are three main scripts to run:

#### Video Capture:

        conda activate tf_env1
        python capture_video.py (Windows)
        python capture_video_linux.py (Linux)


#### IMU Data:

- Check for ```COM Ports``` (Windows), or ```/dev/tty``` ports on Linux.
- Ensure correct code is flashed onto the micro-controller
- If on Windows, Run anaconda as admin. On Linux, make the port executable by typing the following:
        
        sudo chmod a+rw /dev/ttyUSB0
        OR
        sudo chmod a+rw /dev/ttyUSB1

- Enter the respective test number in utils.py

        python imu_read.py

#### GPS:

- Check for ```COM Ports``` (Windows), or ```/dev/tty``` ports on Linux.
- If on Windows, Run anaconda as admin. On Linux, make the port executable by typing the following:
        
        sudo chmod a+rw /dev/ttyUSB0
        OR
        sudo chmod a+rw /dev/ttyUSB1
        
- Ensure correct code is flashed onto the micro-controller
- Enter the respective test number in utils.py

        python gps_read.py

## Hardware Setup

The setup is shown below:

IMU and GPS Setup

<p align="center">
  <img height="500" src="Images/car_img_2.jpeg">
</p>

IMU and GPS Setup
<p align="center">
  <img height="500" src="Images/car_img_3.jpeg">
</p>

Camera Setup

<p align="center">
  <img height="500" src="Images/car_img_5.jpeg">
</p>

Robot in a field, collecting the same data

<p align="center">
  <img height="500" src="Images/robot_Drive.jpeg">
</p>

Electrical Connections

<p align="center">
  <img height="500" src="Images/Electrical_Connections.png">
</p>

## Obtained Graphs

One of the obtained plot is shown below:

<p align="center">
  <img height="500" src="Images/Test_3_plot.png">
</p>


## PYTHON CODE LOOKUP TABLE

| Serial Number| Code  | Function | Arduino Code Flashed |
| ------------- | ------------- | ------------- |------------- |
| 1 |  *capture_video.py*| To capture the video |- |
| 2 | *capture_video_linux.py* | To capture video for Linux and straight away convert to image sequences | - |
| 3 |  *imu_read.py*| To save the IMU Data in quaternion format | IMU_QUATERNION |
| 4 |  *save_and_plot_imu.py*| To save & Plot the IMU Data in quaternion format | IMU_QUATERNION |
| 5 |  *gps_read.py*| To read the GPS Data | GPS_LONGITUDE_LATITUDE_TEST |
| 6 |  *global_gps2xy.py*| To convert the raw GPS data from Text file to XY Coordinates |- |
| 7 | *Interpolate_GPS.py*| To interpolate the GPS Data to match with IMU Data lines |- |
| 8 | *plot_gps_xy.py*| To plot the gps to get the map |- |
| 8 | *utils.py* | Contains utility variables | - |

The order to run these files ```on Windows``` would be 1->3-> 5->6->7->8.

The order to run these files ```on Linux``` would be 2-> 3-> 5->6->7->8.

The TUM format files can be run using the command

        evo_traj tum Test_3_TUM_FORMAT.txt --plot_mode xz --plot
