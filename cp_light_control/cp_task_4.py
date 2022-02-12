import board
from analogio import AnalogOut, AnalogIn

led = AnalogOut(board.A0)
lightSensor = AnalogIn(board.A1)

while True:
  led.value = (65535/lightSensor.value)
