#!/usr/bin/env python

import sys
import rospy

from client_functions import *


def usage():
    return "%s [robot_model='PRob1R' use_existing=True]"%sys.argv[0]

if __name__ == "__main__":
    arg_length = len(sys.argv)
    model = 'PRob1R'
    existing = True
    if 1 <= arg_length <= 3:
	if arg_length > 1:
	    model = str(sys.argv[1])
	if arg_length > 2:
	    existing = bool(sys.argv[2])
	else:
	    print usage()
	    sys.exit(1)
    # initialize and calibrate robot
    initialize(model, "real")
    wait_for_robot()
    calibrate(existing)
    wait_for_robot()
    print("Connected to PRob.")
    print("Robot Status:")
    print("_______________________________________________________")
    print("For Connection Status:               | For Status Info:")
    print("0: not Initialized, not Calibrated   | None")
    print("1: Initializing, not Calibrated      | Ready")
    print("2: Initialized, not Calibrated       | Stopped")
    print("3: Initialized, Calibrating          | Paused")
    print("4: Initialized, Calibrated           | Running")
    print("5:                                   | Released")
    print("6:                                   | Error")
    print "Connection: ",get_connection_info()
    print "Status: ", get_status_info()
