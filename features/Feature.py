import openrgb
from openrgb.utils import RGBColor

class Feature:

    def __init__(self,orgb_client):
        self.orgb_client = orgb_client
        self.device = self.orgb_client.get_devices_by_name(self.device)[0]
        self.zone = self.device.zones[self.zone]

    def __del__(self):
        self.device.off()

    def off(self):
        self.device.off()

    def blank(self):
        self.zone.set_color(RGBColor(0,0,0))
