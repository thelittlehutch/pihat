#!/usr/bin/env python

from sense_hat import SenseHat

import time
import random

sense = SenseHat()

r = random.randint(0,255)
sense.set_pixel(1, 1, (0, r, 0))
sense.set_pixel(1, 2, (r, 0, 0))
sense.set_pixel(1, 3, (r, 0, 0))
sense.set_pixel(1, 4, (0, r, 0))
sense.set_pixel(
time.sleep(1)
sense.clear()

