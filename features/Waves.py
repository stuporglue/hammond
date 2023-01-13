import openrgb
from openrgb.utils import RGBColor
from features.Feature import Feature
from lib.colors import colorstr

# Channel 0 - 25 LEDs

class Waves(Feature):

    base_colors = [
        RGBColor(0,0,255),
        RGBColor(153,193,255),
        RGBColor(250,111,113),
        RGBColor(153,193,255),
        RGBColor(100,100,255),
        RGBColor(217,255,74),
        RGBColor(217,255,74),
        RGBColor(217,255,74),
        RGBColor(0,0,255),
        RGBColor(0,142,255),
        RGBColor(36,100,0),
        RGBColor(255,255,0),
        RGBColor(0,0,255),
        RGBColor(250,19,113),
        RGBColor(36,138,0),
        RGBColor(4,0,138)
    ]

    dark_water_colors = [
        RGBColor(0,0,144),
        RGBColor(0,0,71),
        RGBColor(0,0,200)
    ]

    device = 'Razer Chroma Addressable RGB Controller'
    zone = 0

    def dark_water(self):
        self.shuffle_colors(colors=self.dark_water_colors)

    def print_shape(self):
        color_str_ar = self.color_str_array()

        for i in range(12,0,-1):
            print(color_str_ar[i],end="")

        print("")
        print("        ",end="")

        for i in range(24,13,-1):
            print(color_str_ar[i],end="")

        print("")

