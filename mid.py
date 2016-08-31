#!/usr/bin/env python3
import pigpio
import time
import sys

SERVO = 4

if len(sys.argv) > 1:
    SERVO = int(sys.argv[1])

MIN_PW = 1000
MID_PW = 1450
MAX_PW = 2500
pi = pigpio.pi()

print("mid", SERVO)
pi.set_servo_pulsewidth(SERVO, MID_PW)

