# Service required
import signal
import time
import datetime

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

class Park:
    last_cron = datetime.datetime.now()
    crons = []
    attractions = {}
    audio_device = 'hw:3,0'

    # Handle button debounce
    button_debounce_time = 0.05
    button_last_click = datetime.datetime.now()

    # Set things up
    def __init__(self):
        signal.signal(signal.SIGTERM,self.shutdown)
        signal.signal(signal.SIGINT,self.shutdown)
        signal.signal(signal.SIGUSR1,self.button_press)

        self.connect_all()




    def connect_all(self):
        self.orgb_client = OpenRGBClient()

        self.attractions['v'] = Volcano(self.orgb_client)
        self.attractions['c'] = Clouds(self.orgb_client)
        self.attractions['m'] = Mobo(self.orgb_client)
        self.attractions['w'] = Waves(self.orgb_client)
        self.attractions['t'] = Tree(self.orgb_client)


    # Main loop
    def run(self):
        while True:
            print("Main thread")
            self.do_cron()
            time.sleep(5)

    # Run periodic tasks (eg. startup)
    def do_cron(self):
        its_now = datetime.datetime.now()
        if ( datetime.datetime.now() - self.last_cron > datetime.timedelta(minutes=5)):
            print("Checking crons")
        else:
            print("Too short for crons")
        last_cron = its_now

    # Handle shutdown, kill signal, etc
    def shutdown(self,signo,stackframe):
        print("Shutting down")
        exit()

    # Handle case button press
    def button_press(self,signo,stackframe):
        if ( datetime.datetime.now() - self.button_last_click > datetime.timedelta(seconds=self.button_debounce_time) ):
            print("button press")
            self.button_last_click = datetime.datetime.now()
        else:
            print("Debounced")

    # Play a music file
    def play_music(audiofile):
        pid = os.fork()
        if ( pid == 0 ): 
            os.system("aplay -q -D " + self.audio_device + " " + audiofile)
            os._exit(0)
        else: 
            return pid

