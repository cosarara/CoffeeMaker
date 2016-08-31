#!/usr/bin/env python3
import pigpio
import time
import sys

SERVO = 4

if len(sys.argv) > 1:
    SERVO = int(sys.argv[1])

MIN_PW = 1100
MID_PW = 1450
MAX_PW = 2000
pi = pigpio.pi()

print("min", SERVO)
pi.set_servo_pulsewidth(SERVO, MIN_PW)

