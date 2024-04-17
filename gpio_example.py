#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Use the Broadcom SOC channel
GPIO.setmode(GPIO.BCM)

# Set up GPIO27 as an output
GPIO.setup(27, GPIO.OUT)

# Set GPIO27 to high (3.3V)
GPIO.output(27, GPIO.HIGH)
time.sleep(1)  # Wait for 1 second

# Set GPIO27 to low (0V)
GPIO.output(27, GPIO.LOW)

# Clean up the GPIO state
GPIO.cleanup()



