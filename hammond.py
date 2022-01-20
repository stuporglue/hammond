#!/usr/bin/env python3
import datetime
import asyncio
import park
import signal
import time



class Hammond:

    # The park object
    p = None

    # Asyncio objects
    loop = None

    # Handle button debounce
    button_debounce_time = 0.05
    button_last_click = datetime.datetime.now()

    # Prep for cron work
    last_cron = datetime.datetime.now()
    crons = {
            '23:30': "asdf"
            }

    # Initialize Hammond. Set up signal handlers and start the park
    def __init__(self):
        self.p = park.Park()

        signal.signal(signal.SIGTERM,self.shutdown)
        signal.signal(signal.SIGINT,self.shutdown)
        signal.signal(signal.SIGUSR1,self.button_press)

    # Start working
    def clock_in(self):
        # Two async loops: 
        # 1) The park loop
        # 2) The cron loop

        self.loop = asyncio.get_event_loop()
        asyncio.ensure_future(self.p.open())
        asyncio.ensure_future(self.cron())
        self.loop.run_forever()

        self.p.close()

        print("Ending clock_in")


    # Run periodic tasks (eg. startup)
    async def cron(self):
        while True:
            its_now = datetime.datetime.now()
            if ( datetime.datetime.now() - self.last_cron > datetime.timedelta(minutes=5)):
                print("Checking crons")
            else:
                print("Too short for crons")
            last_cron = its_now
            await asyncio.sleep(1)

    # Handle shutdown, kill signal, etc
    def shutdown(self,signo,stackframe):
        self.loop.stop()


    # Handle case button press
    def button_press(self,signo,stackframe):
        if ( datetime.datetime.now() - self.button_last_click > datetime.timedelta(seconds=self.button_debounce_time) ):
            print("button press")
            self.button_last_click = datetime.datetime.now()
        else:
            print("Debounced")



h = Hammond()
h.clock_in() # Clock in and start working
