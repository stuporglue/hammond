# Service required
import datetime
import asyncio
import queue
import time

# Setup for features
import openrgb
from openrgb import OpenRGBClient
#from openrgb.utils import RGBColor, DeviceType
from features import Features
from shows import Shows
import random

# Features
class Park:
    attractions = {}
    show_queue = queue.Queue()

    park_status = 'closed'

    orgb_client = None

    __instance = None

    # Set things up
    def __init__(self):
        self.__class__.__instance = self

    @classmethod
    def get_instance(cls):
        if cls.__instance == None:
            c = cls()
            c.connect_all()

        return cls.__instance

    @classmethod
    def get_orgb(cls):
        c = cls.get_instance()
        return cls.__instance.orgb_client



    # Open the park!
    async def open_gates(self):

        just_opened = True

        # TODO: Creaky door noise
        self.open()
        while True:

            if (just_opened or self.show_queue.qsize() > 0):

                if just_opened:
                    dothis = Shows.Adventure
                else:
                    dothis = self.show_queue.get()

                if not self.connected():
                    self.connect_all()

                if self.connected():
                    await dothis.start()
                    just_opened = False
                else:
                    await Shows.Testing_The_Fences.start()
            else:
                # Do a usual light show thing as needed
                pass
            await asyncio.sleep(1)

    # Pause park operations to run a special thing
    def enqueue(self,show):
        if (self.show_queue.qsize() < 3):
            self.show_queue.put(show)
            return True
        else:
            return False

    # Open the park, turn all the lights on
    def open(self):
        for k,v in self.attractions.items():
            v.unblank()
        self.park_status = 'opened'

    # Close park, shut things down
    def close(self):
        self.show_queue.queue.clear()
        for k,v in self.attractions.items():
            v.blank()
        self.park_status = 'closed'

    def connected(self):
        return self.orgb_client is not None and self.orgb_client.comms.connected

    # Connect to Orgb and set up the devices
    def connect_all(self):

        # Initial connection case
        if self.orgb_client is None:
            try: 
                self.orgb_client = OpenRGBClient()

                # On first connection get instances
                self.attractions['v'] = Features.Volcano.get_instance()
                self.attractions['c'] = Features.Clouds.get_instance()
                #self.attractions['m'] = Features.Mobo.get_instance()
                self.attractions['ro'] = Features.RAMOne.get_instance()
                self.attractions['rt'] = Features.RAMTwo.get_instance()
                self.attractions['w'] = Features.Waves.get_instance()
                self.attractions['t'] = Features.Tree.get_instance()
                self.attractions['s'] = Features.Sun.get_instance()

            except ConnectionRefusedError as e:
                pass

        # Reconnect case
        else:
            try: 
                self.orgb_client.connect()
            except Exception as e:
                pass

    # Enqueue a random
    def random_gentle(self):
        gentle_shows = [
            Shows.Clouds,
            Shows.Volcano,
            Shows.Waves
        ]

        if self.park_status == 'closed':
            print("Closed up")
            return

        self.enqueue(random.choice(gentle_shows))

