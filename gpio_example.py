#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Use the physical pin numbers
GPIO.setmode(GPIO.BOARD)

# This is your input pin (replace with your actual pin number)
input_pin = 4

# Set up the input pin with an initial state of HIGH
GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        # Wait for a falling edge on the input pin
        GPIO.wait_for_edge(input_pin, GPIO.FALLING)
        print("Falling edge detected on pin {}".format(input_pin))
        # Debounce the switch by waiting for 0.01 seconds
        time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO settings before exiting
