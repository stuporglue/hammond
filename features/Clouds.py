#!/usr/bin/env python3

import openrgb
from openrgb.utils import RGBColor
from features.Feature import Feature

class Clouds(Feature):
    dappled = [
            RGBColor(100,100,100),
            RGBColor(255,255,255),
            RGBColor(0,0,0),
            RGBColor(175,175,175)
            ]

    lightning = [
            RGBColor(255,255,0),
            RGBColor(255,152,0),
            RGBColor(221,162,0),
            RGBColor(100,100,100),
            RGBColor(255,255,255),
            RGBColor(0,0,0),
            RGBColor(175,175,175)
            ]

    wrapup = [
            RGBColor(255,255,0),
            RGBColor(255,152,0),
            RGBColor(221,162,0),
            RGBColor(100,100,100),
            RGBColor(255,255,255),
            RGBColor(0,0,0),
            RGBColor(100,100,100),
            RGBColor(100,100,100),
            RGBColor(255,255,255),
            RGBColor(0,0,0),
            RGBColor(175,175,175),
            RGBColor(255,255,255),
            RGBColor(0,0,0),
        RGBColor(175,175,175),
        RGBColor(175,175,175)
        ]

    device = 'Razer Chroma Addressable RGB Controller'
    zone = 3


    #def __init__(self,orgb_client):
    #    Feature.__init__(self,orgb_client)

     

