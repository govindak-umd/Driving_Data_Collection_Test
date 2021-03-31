# Driving_Data_Collection_Test
This repository shows how to get combined IMU, GPS, and Video data for ORB-SLAM2 verification testing

## Steps to run

Attached the ```IMU +  GPS``` Module onto the vehicle as shown below:

Attach the camera to face forwards in such an angle as to grab features

### There are three main scripts to run:

#### Video Capture:

        conda activate tf_env1
        python capture_video.py

#### IMU Data:

- Check for COM Ports
- Ensure correct code is flashed onto the micro-controller
- Run anaconda as admin
- Enter the respective test number in utils.py

        python save_tum_file.py

#### GPS:

- Check for COM Ports
- Run anaconda as admin
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

## Obtained Graphs

The obtained plots are shown below:

<p align="center">
  <img height="500" src="Images/Test_1_plot.png">
</p>

<p align="center">
  <img height="500" src="Images/Test_2_plot.png">
</p>

<p align="center">
  <img height="500" src="Images/Test_3_plot.png">
</p>


## PYTHON CODE LOOKUP TABLE

| Serial Number| Code  | Function | Arduino Code Flashed |
| ------------- | ------------- | ------------- |------------- |
| 1 |  *capture_video.py*| To capture the video |- |
| 2 |  *save_tum_file.py*| To save the IMU Data in quaternion format the video | IMU_QUATERNION |
| 3 |  *gps_read.py*| To read the GPS Data | GPS_LONGITUDE_LATITUDE_TEST |
| 4 |  *global_gps2xy.py*| To convert the raw GPS data from Text file to XY Coordinates |- |
| 5 | *Interpolate_GPS.py*| To interpolate the GPS Data to match with IMU Data lines |- |
| 7 | *utils.py* | Contains utility variables | - |