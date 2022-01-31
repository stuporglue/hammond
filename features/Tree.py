import openrgb
from openrgb.utils import RGBColor
from features.Feature import Feature

class Tree(Feature):
    base_colors = [
        RGBColor(0,100,0)
    ]

    device = 'Razer Chroma Addressable RGB Controller'
    zone = 2

    #def __init__(self,orgb_client):
    #    Feature.__init__(self,orgb_client)
