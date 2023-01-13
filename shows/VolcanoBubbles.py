from shows.Show import *
from openrgb.utils import RGBColor

class VolcanoBubbles(Show):
    audiofile = 'lavabubbles.wav'

    async def light_show():
        v = Features.Volcano.get_instance()
        for i in range(0,8):
            v.shuffle_colors()
            await asyncio.sleep(0.1)

        v.set_color(RGBColor(255,255,255))
        await asyncio.sleep(0.5)
        v.set_color(RGBColor(255,150,150))
        await asyncio.sleep(0.5)
        v.set_color(RGBColor(255,50,50))
        await asyncio.sleep(0.5)
        v.set_color(RGBColor(255,0,0))




