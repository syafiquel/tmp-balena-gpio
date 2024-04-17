#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Use the Broadcom SOC channel
GPIO.setmode(GPIO.BCM)

# This is your input pin (replace with your actual pin number)
input_pin = 26

# Set up the input pin with an initial state of DOWN
GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        # Wait for a rising edge on the input pin
        GPIO.wait_for_edge(input_pin, GPIO.RISING)
        print("Rising edge detected on pin {}".format(input_pin))
        # Debounce the switch by waiting for 0.01 seconds
        time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO settings before exiting
