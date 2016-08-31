#!/bin/sh

BASE=2
SHOULDER=3
ELBOW=4
WRIST=17
WRIST2=27
GRIP=22

while true; do
	./mid.py $SHOULDER
	./mid.py $ELBOW
	./mid.py $WRIST
	./mid.py $WRIST2
	./mid.py $GRIP
	sleep 2
	./max.py $SHOULDER
	./max.py $ELBOW
	./min.py $WRIST
	./min.py $WRIST2
	./max.py $GRIP
	sleep 2
	./min.py $SHOULDER
	./min.py $ELBOW
	./min.py $WRIST
	./max.py $WRIST2
	./min.py $GRIP
	sleep 2
done
