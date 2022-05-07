#!/usr/bin/env python3

import park
import time
from shows import Shows
from features import Features
from openrgb.utils import RGBColor
import random

# Initialize stuff
park.Park.get_instance()

Shows.SystemIsDown.set_audio_device(1)

w = Features.Clouds.get_instance()

r = random.randint(0,255)
g = random.randint(0,255)
b = random.randint(0,255)
sleep = 0.5

w.set_color(RGBColor.fromRGBA(r,g,b,1))
time.sleep(sleep)
w.set_color(RGBColor.fromRGBA(r,g,b,0.8))
time.sleep(sleep)
w.set_color(RGBColor.fromRGBA(r,g,b,0.6))
time.sleep(sleep)
w.set_color(RGBColor.fromRGBA(r,g,b,0.4))
time.sleep(sleep)
w.set_color(RGBColor.fromRGBA(r,g,b,0.2))
time.sleep(sleep)
w.set_color(RGBColor.fromRGBA(r,g,b,0))

import pdb
pdb.set_trace()
