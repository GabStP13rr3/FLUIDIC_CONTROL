# Code use to calculate flow rate (uL/min) output by pump1 & pump2 with driving frequency between 50-800Hz.

import time
import RPi.GPIO as GPIO


# VARIABLES 
freq_p1 = 100 # Hz RED
freq_p2 = 500# Hz BLUE
T = 10 # Sec
duty = 50 # %

# PINS ASSIGNMENT
GPIO.setmode(GPIO.BCM)
power_pin = 17 #Switch Logic Pin (GPIO17 - Hardware pin 11)
p1_freq_pin = 13 #Frequency Pin Pump1 (GPIO13 - Hardware pin 33)
p2_freq_pin = 12#Frequency Pin Pump2 (GPIO12 -Hardware pin 32)

# PIN STATE ASSIGNMENT
GPIO.setup(p1_freq_pin, GPIO.OUT)
GPIO.setup(p2_freq_pin, GPIO.OUT)
GPIO.setup(power_pin, GPIO.OUT) 

#=====================================#



## CHANGE SWITCH STATE = POWER DRIVERS ON
GPIO.output(power_pin, GPIO.HIGH)



# SET + START PUMP FREQUENCY INPUT
Pump1 = GPIO.PWM(p1_freq_pin, freq_p1)
Pump2 = GPIO.PWM(p2_freq_pin, freq_p2)

#Start Duty Cycle
Pump1.start(duty)
Pump2.start(duty)

# Set Run Time
time.sleep(T)

# TURN OFF FREQUENCY INPUT
Pump1.stop()
Pump2.stop()


# CHANGE SWITCH LOGIC = POWER DRIVER OFF
GPIO.output(power_pin, GPIO.LOW)
GPIO.cleanup()

print('Calibration Completed!')