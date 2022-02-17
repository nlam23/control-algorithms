import board
from analogio import AnalogOut, AnalogIn
import time

lightSensor = AnalogIn(board.A1)
led = AnalogOut(board.A0)
led.value = 0
k = 0.1
tolerance = 1000
error = 0

while True:
  error = 30000 - lightSensor.value
  if abs(error) < tolerance:
    pass
  else:
    led.value -= error*k
    
  print(led.value)
  time.sleep(0.1)
