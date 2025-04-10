#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image, CompressedImage, Range, Imu
from geometry_msgs.msg import Twist, Pose

import miro_msgs
from miro_msgs.msg import platform_config, platform_sensors, platform_state, platform_mics, platform_control, core_state, core_control, core_config, bridge_config, bridge_stream

import opencv_apps
from opencv_apps.msg import CircleArrayStamped

import math
import numpy
import time
import sys
from miro_constants import miro

from datetime import datetime

"""
fetch.py implements the action corresponding to the "fetch" command
MiRo responds by identifying a nearby object and then moving towards it until it touches it
"""

class Fetch():

    def __init__(self):
        ## Node rate
        self.rate = rospy.get_param('rate',200)
