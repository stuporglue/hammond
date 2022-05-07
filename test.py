#!/usr/bin/env python3

import park
import asyncio
from shows import Shows
from openrgb.utils import RGBColor

# Initialize stuff
p = park.Park.get_instance()
p.open()

#p.random_gentle()




# Headphones
#Shows.SystemIsDown.set_audio_device(1)

# import pdb
# pdb.set_trace()

async def doit():
    #await Shows.Adventure.start()
    #await Shows.SystemIsDown.start()
    await Shows.GentleRain.start()

asyncio.run(doit())
#asyncio.run(p.open_gates())
