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

    # Tripple Check
    tripple_check = 0
    tripple_time = 1

    # Handle button debounce
    button_debounce_time = 0.05
    button_last_click = datetime.datetime.now()

    # Watch for when we come out of suspend and do something special
    last_cron_loop = datetime.datetime.now()

    shows = [
            Shows.Adventure,
            Shows.Clouds,
            Shows.GentleRain,
            Shows.JurrasicPark,
            Shows.Roar,
            Shows.Roar2,
            Shows.Volcano,
            Shows.Waves,
            Shows.SystemIsDown,
            Shows.Shark
            ]

    # Initialize Hammond. Set up signal handlers and start the park
    def __init__(self):
        self.p = park.Park.get_instance()

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
        #schedule.every(2).to(4).minutes.do(self.p.random_gentle)

    # Wrapper so we don't have to asyncio anything outside of the class
    def clock_in(self):

        self.loop = asyncio.get_event_loop()

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
            if ( datetime.datetime.now() - self.last_cron_loop > datetime.timedelta(seconds=60) ):
                # Do wakeup routine
                #self.p.open()
                pass

            schedule.run_pending()
            await asyncio.sleep(5)

    # Real shutdown
    def _shutdown(self):
        for t in asyncio.all_tasks():
            t.cancel()

    # Handle shutdown, kill signal, etc
    def shutdown(self,signo,stackframe):
        self._shutdown()

    # Handle case button press
    def button_press(self,signo,stackframe):


        # Check for a tripple click and toggle off or on
        if ( datetime.datetime.now() - self.button_last_click > datetime.timedelta(seconds=self.tripple_time) ):
            self.tripple_check = self.tripple_check + 1 

            print("Tripple now at " + str(self.tripple_check))

            if self.tripple_check >= 3: 
                print("Did a tripple")
                if self.p.park_status == 'closed':
                    self.p.open()
                else:
                    self.p.close()
        else:
            self.tripple_check = 1
 

        # Otherwise do the normal routine queueing
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
