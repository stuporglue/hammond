from shows.Show import *
import random
from openrgb.utils import RGBColor

class GentleRain(Show):
    audiofile = 'gentle_rain.wav'

    async def light_show():
        c = Features.Clouds.get_instance()
        s = Features.Sun.get_instance()
        w = Features.Waves.get_instance()
        s.blank()
        w.dark_water()

        colors = random.choices(c.base_colors,k=c.len())
        c.set_colors(colors,fast=True)

        dark_water = random.choices(w.dark_water_colors,k=w.len())

        # 15 seconds of dapple
        for i in range(0,170):
            # Which light to change        # What color to set it to
            colors[random.randint(0,len(colors) - 1)] = random.choice(c.base_colors)
            c.set_colors(colors,fast=True)

            dark_water[random.randint(0,len(dark_water) - 1)] = random.choice(w.dark_water_colors)
            w.set_colors(dark_water,fast=True)

            await asyncio.sleep(0.05)
