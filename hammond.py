#!/usr/bin/env python3
import datetime
import asyncio
import signal
import time
import random

import park
from shows import Shows

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


    shows = [
            Shows.Adventure,
            Shows.Volcano
            ]

    # Initialize Hammond. Set up signal handlers and start the park
    def __init__(self):
        self.p = park.Park()

        signal.signal(signal.SIGTERM,self.shutdown)
        signal.signal(signal.SIGINT,self.shutdown)
        signal.signal(signal.SIGUSR1,self.button_press)

    # Wrapper so we don't have to asyncio anything outside of the class
    def clock_in(self):
        asyncio.run(self._clock_in())

    # Start working
    async def _clock_in(self):
        # Two async loops: 
        # 1) The park loop
        # 2) The cron loop

        try: 
            await asyncio.gather(
                    asyncio.shield(self.p.open()),
                    asyncio.shield(self.cron())
                )
        except asyncio.exceptions.CancelledError:
            # Exception will be thrown when we cancel in sigterm/sigint
            pass

            print("Ending clock_in")


    # Run periodic tasks (eg. startup)
    async def cron(self):
        while True:
            its_now = datetime.datetime.now()
            if ( datetime.datetime.now() - self.last_cron > datetime.timedelta(minutes=5)):
                print("Checking crons")

            last_cron = its_now
            await asyncio.sleep(1)

    # Handle shutdown, kill signal, etc
    def shutdown(self,signo,stackframe):
        for t in asyncio.all_tasks():
            t.cancel()


    # Handle case button press
    def button_press(self,signo,stackframe):
        if ( datetime.datetime.now() - self.button_last_click > datetime.timedelta(seconds=self.button_debounce_time) ):
            self.button_last_click = datetime.datetime.now()
            self.p.enqueue(random.choice(self.shows))
        else:
            print("Debounced")


h = Hammond()
h.clock_in() # Clock in and start working
