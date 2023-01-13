import openrgb
from openrgb.utils import RGBColor
import random
import park
from lib.error_wrap import decorate_all_methods
from lib.error_wrap import ORGBServerReconnect
from lib.colors import colorstr

# https://stackoverflow.com/questions/24024966/try-except-every-method-in-class


@decorate_all_methods(ORGBServerReconnect)
class Feature:

    __instance = None
    __features = {}

    orgb_client = None
    device = None # Eg. the LED controller
    device_index = 0 # Default to first device of name. 
    zone = None # Eg. the specific ARGB device

    base_colors = [RGBColor(100,0,100)]

    def __init__(self):
        self.orgb_client = park.Park.get_orgb()
        self.device = self.orgb_client.get_devices_by_name(self.device)[self.device_index]
        print("Using device index " + str(self.device_index) + " for " + str(self))
        self.zone = self.device.zones[self.zone]
        self.__class__.__instance = self
        __class__.__features[str(self.__class__)] = self

    @classmethod
    def get_instance(cls):
        if cls.__instance == None:
            cls.__instance = cls()
        return cls.__instance

    # Turns off the whole device (all zones connected to device)
    def off(self):
        self.device.off()

    # Turns off the specific zone for the device
    def blank(self):
        self.zone.set_color(RGBColor(0,0,0))

    # The first thing that happens when the lights are turned on
    # Default is shuffle_colors
    def unblank(self):
        self.shuffle_colors()

    def shuffle_colors(self,colors=None):
        if colors == None:
            colors = self.base_colors
        c = random.choices(colors,k=self.len())

        for i in range(0,len(self.zone.colors)):
            self.zone.colors[i] = random.choice(colors)
        return self.zone.show()

    def len(self):
        return len(self.zone.leds)

    def set_colors(self,colors,fast=False):
        self.zone.colors = colors;
        return self.zone.show()

    def set_color(self,color,fast=False):
        return self.zone.set_color(color,fast)


    def color_str_array(self):
        retthis = []
        for i in range(0,len(self.zone.colors)):
            retthis.append(("[" + str(i).zfill(2) + "/" + colorstr(self.zone.colors[i],pad=3)) + "]")
        return retthis

    def print_shape(self):
        for i in self.color_str_array():
            print(i,end="")
