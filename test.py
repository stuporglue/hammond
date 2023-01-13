#!/usr/bin/env python3

import park
import asyncio
from shows import Shows
from features import Features
from openrgb.utils import RGBColor
import time

# Initialize stuff
thepark = park.Park.get_instance()
thepark.open()

#p.random_gentle()




# Headphones
Shows.SystemIsDown.set_audio_device(1)


waves = Features.Waves.get_instance()
waves.dark_water()
#w.print_shape()

#import pdb
#pdb.set_trace()

async def doit():
    #await Shows.Adventure.start()
    #await Shows.SystemIsDown.start()
    await Shows.Shark.start()

print("Loaded")
time.sleep(2)
asyncio.run(doit())
#asyncio.run(p.open_gates())
