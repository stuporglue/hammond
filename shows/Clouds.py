from shows.Show import *
import random

class Clouds(Show):
    audiofile = 'thunderstorm.wav'

    async def light_show():
        c = Features.Clouds.get_instance()

        # 15 seconds of dapple
        for i in range(0,30):
            colors = random.choices(c.base_colors,k=c.len())
            c.set_colors(colors,fast=True)
            await asyncio.sleep(0.05)


        # 15 seconds of lightning
        for i in range(0,30):
            colors = random.choices(c.lightning,k=c.len())
            c.set_colors(colors,fast=True)
            await asyncio.sleep(0.05)

        # wrapup till we're done
        while True:
            colors = random.choices(c.wrapup,k=c.len())
            c.set_colors(colors,fast=True)
            await asyncio.sleep(0.05)
