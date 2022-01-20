from features import Features
import subprocess
import asyncio
import os
import errno
from contextlib import suppress

class Show:
    # I can't get my asla devices to show up in the same order after every boot :-(
    # Yes, I tried /etc/modprobe.d/alsa-base.conf
    audio_device = subprocess.check_output("cat /proc/asound/cards | grep -B1 Jieli | head -1 | sed 's/.\?\([0-9]\) \[.*/\\1/g'",shell=True).rstrip().decode('UTF-8')

    """ 
    A show can have an audiofile, a light_show and an executable
    The audiofile and executable will fork. 
    The light_show will run until they both come back
    """
    audiofile = None
    executable = None

    # Play a music file
    @staticmethod
    async def play_music(audiofile):
        pid = os.fork()
        if ( pid == 0 ): 
            audiopath = os.path.dirname(os.path.realpath(__file__)) + '/../audio/' + audiofile
            os.system("aplay -q -D plughw:" + __class__.audio_device + ",0 " + audiopath)
            os._exit(0)

        
        while True:
            try:
                wpid,status = os.waitpid(-1,os.WNOHANG)
            except OSError as e:
                if e.errno != errno.ECHILD:
                    raise e
                else:
                    return

            await asyncio.sleep(0.25)


    # Play a music file
    @staticmethod
    async def exec_something(execthis):
        pid = os.fork()
        if ( pid == 0 ): 
            execpath = os.path.dirname(os.path.realpath(__file__)) + '/../scripts/' + execthis
            os.system(execpath)
            os._exit(0)
        
        while True:
            try:
                wpid,status = os.waitpid(-1,os.WNOHANG)
            except OSError as e:
                if e.errno != errno.ECHILD:
                    raise e
                else:
                    return

            await asyncio.sleep(0.25)




    @classmethod
    def start(cls):
        # New async loop
        loop = asyncio.get_event_loop()

        light_io = None
        run_complete_tasks = []

        # Start light show, if present
        if hasattr(cls,'light_show'):
            light_io = asyncio.ensure_future(cls.light_show())

        # Enqueue audio, if present
        if cls.audiofile is not None:
            run_complete_tasks.append(cls.play_music(cls.audiofile))

        # Enqueue script, if present
        if cls.executable is not None:
            run_complete_tasks.append(cls.exec_something(cls.executable))

        loop.run_until_complete(asyncio.wait(run_complete_tasks))

        # Cancel the lights and wait for cancel to complete
        if light_io is not None:
            light_io.cancel()
            with suppress(asyncio.CancelledError):
                loop.run_until_complete(task)
        
        # Stop it all!
        loop.stop()

        # Close the loop
        loop.close()

