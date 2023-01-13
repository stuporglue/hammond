from openrgb.utils import RGBColor
from features.Feature import Feature

# Channel 3 - 3 LEDs

class RAMOne(Feature):
    base_colors = [
        RGBColor(0,100,0),
        RGBColor(0,100,0),
        RGBColor(0,100,0),
        RGBColor(0,100,0),
        RGBColor(0,100,0)
    ]

    device = 'ENE DRAM'
    device_index = 0
    zone = 0
