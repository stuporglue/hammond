from shows.Show import *

class Waves(Show):
    audiofile = 'waves.wav'

    async def light_show():
        w = Features.Waves.get_instance()
        while True:
            w.shuffle_colors()
            await asyncio.sleep(0.1)


