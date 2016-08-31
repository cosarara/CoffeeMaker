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

#print("starting - mid")
#pi.set_servo_pulsewidth(SERVO, MID_PW)
#time.sleep(3)
print("max", SERVO)
pi.set_servo_pulsewidth(SERVO, MAX_PW)

#for i in range(10):
#    pi.set_servo_pulsewidth(SERVO, MIN_PW+(MAX_PW-MIN_PW)/10*i)
#    time.sleep(3)
#
#print("min")
#pi.set_servo_pulsewidth(SERVO, MIN_PW)

