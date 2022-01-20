import openrgb
from openrgb.utils import RGBColor
from features.Feature import Feature

class Sun(Feature):

    device = 'Razer Chroma Addressable RGB Controller'
    zone = 4

    def __init__(self,orgb_client):
        print("Volcano init")
        Feature.__init__(self,orgb_client)
