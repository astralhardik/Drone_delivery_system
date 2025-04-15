# 🚁 Autonomous Drone Delivery System

A full-stack autonomous drone delivery project developed as a part of the final year coursework at **The LNM Institute of Information Technology, Jaipur**. This system integrates UAV design, autonomous mission planning, Aruco-based marker landing, web integration, and real-time database communication using Raspberry Pi and Pixhawk.

---

## 📚 Table of Contents

- [Project Overview](#project-overview)
- [System Architecture](#system-architecture)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Components Used](#components-used)
- [How It Works](#how-it-works)
- [Simulation](#simulation)
- [Additional Features](#additional-features)
- [Website Integration](#website-integration)
- [Results & Testing](#results--testing)
- [Video Demonstration](#video-demonstration)
- [Team & Credits](#team--credits)
- [Future Work](#future-work)
- [References](#references)

---

## 📌 Project Overview

This project aims to develop an autonomous **drone delivery system** capable of transporting payloads efficiently and accurately between predefined locations using **GPS navigation**, **Aruco-based marker detection**, and **web-based mission input**. The drone is assembled using Pixhawk for flight control and Raspberry Pi for high-level automation and communication with cloud systems.

---

## ⚙️ System Architecture

text
User Input (Web Interface) 
         ↓
MongoDB (Order & Location DB)
         ↓
Raspberry Pi (Mission Control via DroneKit)
         ↓
Pixhawk Flight Controller (UAV)
         ↓
Drone (With Camera, Payload Box, GPS, ESCs)
---

##🚀 Features
Autonomous drone navigation using MAVLink + DroneKit

Real-time video stream & Aruco Marker-based landing

Web application for pickup/delivery location input

GPS and compass-based navigation

Integrated with MongoDB database

Simulated via Gazebo

Emergency user override using hardware switch

Lightweight payload delivery box (up to 500g)

##💻 Technologies Used
Raspberry Pi 3B

Pixhawk Flight Controller

MAVLink Protocol

DroneKit (Python API)

MongoDB Atlas

Next.js (Frontend + API)

Gazebo + ArduPilot

OpenCV + Aruco Marker Detection

##🧰 Components Used

Component	Description
Pixhawk	Flight controller for low-level control
BLDC Motors (1000KV)	Propulsion motors for quadcopter
S500 Frame	Durable quadcopter chassis
ESCs	Electronic speed controllers
M8N GPS & Compass	For global positioning and direction
Raspberry Pi 3	Companion computer for logic, API calls
2400mAh LiPo Battery	Power source for motors and logic
Camera (Raspberry Pi)	Visual feed for Aruco detection
Aruco Markers	Used for precise landing detection
Payload Box (Cardboard)	Holds lightweight delivery items
📥 How It Works
User selects pickup and delivery points on a custom-built Next.js web interface

Locations are stored in a MongoDB Atlas database

The Raspberry Pi fetches delivery requests via API and plans the mission using DroneKit

The drone takes off to the pickup point

On landing, the user loads the payload and triggers the hardware switch

Drone continues to delivery point, uses Aruco Marker for final alignment

Returns to home base and updates the delivery status to Delivered

##🧪 Simulation
Simulated in Gazebo using a virtual quadcopter

Used for testing mission scripts before real flight

ArduPilot plugin was not functional; only Gazebo visualization used

##🎯 Additional Features
A. Aruco Marker Detection
Enabled precise landing using computer vision

Detected Aruco marker center and aligned drone using roll and pitch channel overrides

B. Payload Box
Lightweight cardboard structure used to transport up to 500g

Tested using a packet of biscuits to validate center of mass and stability

C. Website Integration
Frontend: Next.js

Backend: API to MongoDB

Mapped locations with predefined GPS coordinates

Order status updated in real time via the RPi

##✅ Results & Testing
Successfully navigated between locations with 95% accuracy

Real-time adjustments enabled through user hardware input

Visual confirmation using camera + Aruco

Flight time ~10 mins per mission with 2400 mAh battery

##📺 Video Demonstration
Watch the working prototype in action:
🎥 YouTube Demo – Drone Delivery System

##👥 Team & Credits
Garvit Goyal – 21dec004

Akul Khandelwal – 21uec020

Labhesh Mundhada – 21uec156

Hardik Agrawal – 22uec045 (Assisted)

Advisors: Dr. Atul Mishra & Dr. Mohit Makkar

Support: Udayveer Singh, Robotics Lab Team – LNMIIT

##🔮 Future Work
Improve simulation pipeline with full ArduPilot + SITL integration

Add autonomous payload drop mechanism using servo

Implement real-time obstacle avoidance

Expand web UI for live drone tracking and fleet control

Enable multi-drone coordination

##📚 References
DroneKit-Python Docs

OpenCV Aruco Guide

Pixhawk Overview

Raspberry Pi Documentation

Quadcopter Frame & ESCs

##📄 License
This project is part of a university academic submission and is intended for educational and research purposes. For use or adaptation, please provide credit to the original authors and contributors.
