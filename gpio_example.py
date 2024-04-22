#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin for PWM output
PWM_PIN = 4
GPIO.setup(PWM_PIN, GPIO.OUT)

# Set the frequency and duty cycle
FREQUENCY = 50  # Frequency in Hz
DUTY_CYCLE = 50  # Duty cycle in %

# Create a PWM instance
pwm = GPIO.PWM(PWM_PIN, FREQUENCY)

# Start the PWM output
pwm.start(DUTY_CYCLE)

# Run for a while
time.sleep(10)

# Stop the PWM output
pwm.stop()

# Clean up the GPIO
GPIO.cleanup()


