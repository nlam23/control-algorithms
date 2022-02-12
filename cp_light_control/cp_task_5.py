import board
from analogio import AnalogOut, AnalogIn

led = AnalogOut(board.A0)
lightSensor = AnalogIn(board.A1)
led.value = 60000

while True:
  print(lightSensor.value)
