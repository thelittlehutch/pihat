#!/usr/bin/env python

from sense_hat import SenseHat
sense = SenseHat()
import time

sense.set_pixel(2, 2, (0, 0, 225))
sense.set_pixel(4, 2, (0, 0, 255))
sense.set_pixel(3, 4, (0, 225, 0))
sense.set_pixel(1, 5, (225, 0, 0))
sense.set_pixel(2, 6, (225, 0, 0))
sense.set_pixel(3, 6, (225, 0, 0))
sense.set_pixel(4, 6, (225, 0, 0))
sense.set_pixel(5, 5, (255, 0, 0))

time.sleep(1)
sense.clear()
