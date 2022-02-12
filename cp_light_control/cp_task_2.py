import time
import board
from analogio import AnalogOut

led = AnalogOut(board.A0)

while True:
#counts up from 0 to 65535, with 64 increments, ends up corresponding to the DAC's 10-bit range
  for i in range(0, 65535, 64):
    led.value = i
    time.sleep(0.1)
