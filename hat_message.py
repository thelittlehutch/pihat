#!/usr/bin/env python
# this script will show a scrolling message on the Pi HAT 
from sense_hat import SenseHat
sense = SenseHat()

# sned the text Hello World! to the show_message() function
sense.show_message("Hello World!")
