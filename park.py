# Service required
import subprocess
import datetime
import asyncio
import queue

# Setup for features
import openrgb
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType

# Features
from features.Volcano import Volcano
from features.Clouds import Clouds
from features.Mobo import Mobo
from features.Waves import Waves
from features.Tree import Tree
from features.Sun import Sun

class Park:
    attractions = {}
    audio_device = None
    show_queue = queue.Queue()

    # Set things up
    def __init__(self):
        self.audio_device = subprocess.check_output("cat /proc/asound/cards | grep -B1 Jieli | head -1 | sed 's/.\?\([0-9]\) \[.*/\\1/g'",shell=True).rstrip().decode('UTF-8')
        self.connect_all()
        print("Using audio device '" + self.audio_device + "'")

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

        # TODO: Make attractions singletons?
        self.attractions['v'] = Volcano(self.orgb_client)
        self.attractions['c'] = Clouds(self.orgb_client)
        self.attractions['m'] = Mobo(self.orgb_client)
        self.attractions['w'] = Waves(self.orgb_client)
        self.attractions['t'] = Tree(self.orgb_client)
        self.attractions['s'] = Sun(self.orgb_client)

    # Play a music file
    def play_music(audiofile):
        pid = os.fork()
        if ( pid == 0 ): 
            os.system("aplay -q -D " + self.audio_device + " " + audiofile)
            os._exit(0)
        else: 
            return pid
