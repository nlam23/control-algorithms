"""CircuitPython Essentials Digital In Out example - modified by Evan Weinberg"""
import time
import board
from digitalio import DigitalInOut, Direction, Pull

# LED setup.
led = DigitalInOut(board.LED)

led.direction = Direction.OUTPUT

# Switch setup
switch = DigitalInOut(board.D2)
#this is saying set a digital output on pin d2
switch.direction = Direction.INPUT
#this is saying that they're looking for an ionput.
switch.pull = Pull.UP

while True:
    # We could also do "led.value = not switch.value"!
    if switch.value:
        led.value = False
    else:
        led.value = True

    time.sleep(0.01)  # debounce delay
