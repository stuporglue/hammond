import openrgb
from openrgb.utils import RGBColor

class Feature:

    __instance = None
    __features = {}

    def __init__(self,orgb_client):
        self.orgb_client = orgb_client
        self.device = self.orgb_client.get_devices_by_name(self.device)[0]
        self.zone = self.device.zones[self.zone]
        self.__class__.__instance = self
        __class__.__features[str(self.__class__)] = self

    def __del__(self):
        self.device.off()

    def off(self):
        self.device.off()

    def blank(self):
        self.zone.set_color(RGBColor(0,0,0))

    @classmethod
    def get_instance(cls):
        if cls.__instance == None:
            raise FeatureNotReadyException
        else:
            return cls.__instance

class FeatureNotReadyException(Exception):
    pass
