#!/usr/bin/env python3
import pigpio
import time
import sys

SERVO = 4

if len(sys.argv) > 1:
    SERVO = int(sys.argv[1])

MIN_PW = 1000
MID_PW = 1600
MAX_PW = 2500
pi = pigpio.pi()

print("mid")
while True:
    pi.set_servo_pulsewidth(4, MID_PW)
    pi.set_servo_pulsewidth(3, MID_PW)
    pi.set_servo_pulsewidth(17, MID_PW)
    time.sleep(0.1)
    pi.set_servo_pulsewidth(4, MID_PW+100)
    pi.set_servo_pulsewidth(3, MID_PW-100)
    pi.set_servo_pulsewidth(17, MID_PW+50)
    time.sleep(10)

