import openrgb
from openrgb.utils import RGBColor
import random

class Feature:

    __instance = None
    __features = {}

    orgb_client = None
    device = None # Eg. the LED controller
    zone = None # Eg. the specific ARGB device

    base_colors = [RGBColor(100,0,100)]

    def __init__(self,orgb_client):
        self.orgb_client = orgb_client
        self.device = self.orgb_client.get_devices_by_name(self.device)[0]
        self.zone = self.device.zones[self.zone]
        self.__class__.__instance = self
        __class__.__features[str(self.__class__)] = self

    @classmethod
    def get_instance(cls):
        if cls.__instance == None:
            raise FeatureNotReadyException
        else:
            return cls.__instance

    def off(self):
        self.device.off()

    def blank(self):
        self.zone.set_color(RGBColor(0,0,0))

    # The first thing that happens when the lights are turned on
    # Default is shuffle_colors
    def unblank(self):
        self.shuffle_colors()

    def shuffle_colors(self):
        c = random.choices(self.base_colors,k=self.len())
        self.zone.set_colors(c,fast=True)

    def len(self):
        return len(self.zone.leds)

    def set_colors(self,colors,fast=False):
        return self.zone.set_colors(colors,fast)

class FeatureNotReadyException(Exception):
    pass
