import openrgb
from openrgb.utils import RGBColor
from features.Feature import Feature

class Volcano(Feature):
    base_colors = [
        RGBColor(255,0,0),
        RGBColor(255,255,0),
        RGBColor(255,125,0),
        RGBColor(255,200,0),
    ]

    device = 'Razer Chroma Addressable RGB Controller'
    zone = 5
