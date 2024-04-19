#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Use the Broadcom SOC channel
GPIO.setmode(GPIO.BCM)

# This is your output pin (replace with your actual pin number)
output_pin = 26

# Set up the output pin
GPIO.setup(output_pin, GPIO.OUT)

# Initialize the pin to LOW
GPIO.output(output_pin, GPIO.LOW)

try:
        GPIO.output(output_pin, GPIO.HIGH)
        # Wait for 1 second
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO settings before exiting

