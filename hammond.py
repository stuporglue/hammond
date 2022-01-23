#!/usr/bin/env python3
import datetime
import asyncio
import signal
import time
import random
import schedule

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

    shows = [
            Shows.Adventure,
            Shows.Clouds,
            Shows.JurrasicPark,
            Shows.Roar,
            Shows.Roar2,
            Shows.Volcano,
            Shows.Waves
            ]

    # Initialize Hammond. Set up signal handlers and start the park
    def __init__(self):
        self.p = park.Park()

        signal.signal(signal.SIGTERM,self.shutdown)
        signal.signal(signal.SIGINT,self.shutdown)
        signal.signal(signal.SIGUSR1,self.button_press)
        signal.signal(signal.SIGUSR2,self.testfunc)

        self.setup_crons()

    # List all our cron jobs here
    def setup_crons(self):
        schedule.every().day.at("22:00").do(self.p.close)
        schedule.every().day.at("23:00").do(self.p.close)
        schedule.every().day.at("00:00").do(self.p.close)
        schedule.every().day.at("06:00").do(self.p.open)

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
                    asyncio.shield(self.p.open_gates()),
                    asyncio.shield(self.cron())
                )
        except asyncio.exceptions.CancelledError:
            # Exception will be thrown when we cancel in sigterm/sigint
            pass

        self.p.close()


    # Run periodic tasks (eg. startup)
    async def cron(self):
        while True:
            schedule.run_pending()
            await asyncio.sleep(5)

    # Handle shutdown, kill signal, etc
    def shutdown(self,signo,stackframe):
        for t in asyncio.all_tasks():
            t.cancel()

    # Handle case button press
    def button_press(self,signo,stackframe):
        if ( datetime.datetime.now() - self.button_last_click > datetime.timedelta(seconds=self.button_debounce_time) ):
            self.button_last_click = datetime.datetime.now()
            self.enqueue_show(random.choice(self.shows))
        else:
            pass

    # Enqueue one
    def enqueue_show(self,show=None):
        return self.p.enqueue(show)

    def demo(self):
        for s in self.shows:
            print("Trying to demo " + str(s))
            while not self.enqueue_show(s):
                print("Couldn't enqueue, sleeping")
                time.sleep(1)

    # Function to do testing
    def testfunc(self,signo,stackframe):

        import pdb
        import rlcompleter
        myvars = globals()
        myvars.update(locals())
        pdb.Pdb.complete=rlcompleter.Completer(myvars).complete
        pdb.set_trace()


h = Hammond()
h.clock_in() # Clock in and start working
