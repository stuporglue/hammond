# Service required
import datetime
import asyncio
import queue

# Setup for features
import openrgb
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType
from features import Features

# Features
class Park:
    attractions = {}
    show_queue = queue.Queue()

    # Set things up
    def __init__(self):
        self.connect_all()

    # Open the park!
    async def open(self):
        print("Opening park")
        while True:
            if (self.show_queue.qsize() > 0):
                dothis = self.show_queue.get()
                dothis()
            else:
                # Do a usual light show thing as needed
                pass
            await asyncio.sleep(1)


    # Pause park operations to run a special thing
    def enqueue(self,show):
        self.show_queue.put(show)

    # Close park, shut things down
    def close(self):
        print("Closing park")
        for k,v in self.attractions.items():
            v.blank()

    # Connect to Orgb and set up the devices
    def connect_all(self):
        self.orgb_client = OpenRGBClient()

        self.attractions['v'] = Features.Volcano(self.orgb_client)
        self.attractions['c'] = Features.Clouds(self.orgb_client)
        self.attractions['m'] = Features.Mobo(self.orgb_client)
        self.attractions['w'] = Features.Waves(self.orgb_client)
        self.attractions['t'] = Features.Tree(self.orgb_client)
        self.attractions['s'] = Features.Sun(self.orgb_client)
