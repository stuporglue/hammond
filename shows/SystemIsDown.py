from shows.Show import *
from openrgb.utils import RGBColor
import random
from lib.colors import set_alphas
import time

class SystemIsDown(Show):
    audiofile = 'system.wav'

    @staticmethod
    async def light_show():
        v = Features.Volcano.get_instance()
        t = Features.Tree.get_instance()
        w = Features.Waves.get_instance()
        c = Features.Clouds.get_instance()
        s = Features.Sun.get_instance()

        features = [w,v,c,t,s]

        colors = [
            RGBColor(72,19,4),
            RGBColor(244,213,141),
            RGBColor(240,108,61),
            RGBColor(191,6,3),
            RGBColor(141,8,1),
            RGBColor(238,238,238),
            RGBColor(204,0,0),
            RGBColor(219,212,212),
            RGBColor(243,246,244)
        ]

        # Bass line
        blue = RGBColor(0,0,255)
        white = RGBColor(255,255,255)
        purple = RGBColor(255,0,255)
        green = RGBColor(0,255,175)

        start_time = time.time() * 1000.0

        t.set_color(RGBColor(0,255,0),fast=True)
        v.set_color(RGBColor(255,0,0),fast=True)

        while time.time()*1000.0 - start_time < 6500:
            w.set_color(blue,fast=True)
            c.blank()
            s.set_color(purple,fast=True)
            await asyncio.sleep(0.2)
            w.set_color(green,fast=True)
            c.set_color(white,fast=True)
            s.blank()
            await asyncio.sleep(0.2)

        w.set_color(blue,fast=True)
        c.set_color(white,fast=True)
        s.set_color(purple,fast=True)

        # Tree and volcano dance

        #while time.time()*1000.0 - start_time < 9500:
        for i in range(0,14):
            t.set_color(RGBColor(0,255,0),fast=True)
            v.set_color(RGBColor(255,0,0),fast=True)
            await asyncio.sleep(0,2)
            t.blank()
            v.blank()
            t.set_color(RGBColor(255,0,0),fast=True)
            v.set_color(RGBColor(0,255,0),fast=True)
            await asyncio.sleep(0,2)

        t.set_color(RGBColor(0,0,255),fast=True)
        v.set_color(RGBColor(0,0,255),fast=True)


        # Explode
        for f in features:
            f.set_color(white,fast=True)
        await asyncio.sleep(0.1)

        for i in range(360,0,-1):
            for f in features:
                colors = random.choices(colors,k=f.len())
                colors = set_alphas(colors,i/360)
                f.set_colors(colors,fast=True)
            await asyncio.sleep(0.1)

        for f in features:
            f.blank()

        w.off()

