import time
import board
from analogio import AnalogIn

input = AnalogIn(board.A1)

while True:
    print(input)
    time.sleep(0.5)
