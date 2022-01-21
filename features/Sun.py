import openrgb
from openrgb.utils import RGBColor
from features.Feature import Feature

class Sun(Feature):
    base_colors = [
            RGBColor(255,255,0)
            ]

    device = 'Razer Chroma Addressable RGB Controller'
    zone = 4
