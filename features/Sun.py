import openrgb
from openrgb.utils import RGBColor
from features.Feature import Feature

# Channel 5 - 6 LEDs

class Sun(Feature):
    base_colors = [
            RGBColor(255,255,0),
            RGBColor(255,100,0)
            ]

    device = 'Razer Chroma Addressable RGB Controller'
    zone = 4
