from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time
import os
import cv2
import argparse
import requests

'''import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
'''


def arm_and_takeoff(aTargetAltitude):
    print("Basic pre-arm checks")
    # Don't let the user try to arm until autopilot is ready
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialise...")
        time.sleep(1)

    print("Arming motors")
    # Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)  # Take off to target altitude

    # Check that vehicle has reached takeoff altitude
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break and return from function just below target altitude.
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)


def main():
    # GPIO.setup(1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    ############################# order_receive_from_website #######################

    while (True):

        r = requests.get("https://automated-drone-delivery-vha4.vercel.app/api/location")
        response_dict = r.json()
        customer_id = None
        loc1 = None
        loc2 = None
        if (response_dict['message']['success'] == True):
            if (len(response_dict['response']) != 0):
                customer_id = response_dict['response']['_id']
                loc1 = response_dict['response']['start']
                loc2 = response_dict['response']['end']
                print('order received for ', customer_id)
                print("going from", loc1, " to ", loc2)
                break
            else:
                print("no new order")
                time.sleep(3)

    # Function to arm and then takeoff to a user specified altitude

    # Initialize the takeoff sequence to 2m
    arm_and_takeoff(2)

    print("Take off complete")

    print("Set default/target airspeed to 3")
    vehicle.airspeed = 3

    campuslocations = {"BH2": (26.9348280, 75.9238479, 4), "canteen": (26.9345781, 75.9239052, 4),
                       "home": (26.9345718, 75.9237674, 4)}
    (x, y, h) = campuslocations[loc1]

    target1 = LocationGlobalRelative(x, y, h)
    vehicle.simple_goto(target1, groundspeed=3)
    time.sleep(15)

    # curstate=GPIO.input(1)
    vehicle.mode = "LAND"
    time.sleep(10)
    while (vehicle.armed == True):
        time.sleep(2)
        '''while(GPIO.input(1)==curstate):
            time.sleep(1)
           time.sleep(10)
    '''
    ################# landed at pickup loc ##########################

    vehicle.mode = "GUIDED"
    if (vehicle.armed == False):
        vehicle.armed = True
        while not vehicle.armed:
            print('arming...')

    time.sleep(1)
    print("....armed.....again")
    print(vehicle.mode.name)
    vehicle.simple_takeoff(3)
    while True:
        if (vehicle.location.global_relative_frame.alt) >= 2 * 0.95:
            break
        time.sleep(1)

    (x, y, z) = campuslocations[loc2]
    target2 = LocationGlobalRelative(x, y, z)
    vehicle.simple_goto(target2, groundspeed=3)
    time.sleep(10)

    # curstate=GPIO.input(1)
    vehicle.mode = "LAND"
    time.sleep(10)
    while (vehicle.armed == True):
        time.sleep(2)

    vehicle.mode = "GUIDED"
    if (vehicle.armed == False):
        vehicle.armed = True
    while not vehicle.armed:
        print('arming...')

    time.sleep(1)
    print("....armed.....again")
    print(vehicle.mode.name)
    vehicle.simple_takeoff(3)
    while True:
        if (vehicle.location.global_relative_frame.alt) >= 2 * 0.95:
            break
    time.sleep(1)
    (x, y, z) = campuslocations["home"]
    target3 = LocationGlobalRelative(x, y, z)
    vehicle.simple_goto(target3, groundspeed=3)
    time.sleep(15)
    vehicle.mode = "LAND"
    time.sleep(10)

    newAPI = baseAPI + customer_id
    print("Delivered")
    payload = {"deliveryStatus": "Delivered"}
    requests.put(newAPI, data=payload)


# Connect to the Vehicle
vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=921600)
# 921600 is the baudrate that you have set in the mission plannar or qgc


while (True):
    try:
        main()
    except Exception as e:
        print(e)
        vehicle.mode = "LAND"
        time.sleep(10)
        print("landed")
        vehicle.close()
        break
