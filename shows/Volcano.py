from shows.Show import *

class Volcano(Show):
    audiofile = 'explosion4.wav'

    async def light_show():
        v = Features.Volcano.get_instance()
        while True:
            v.shuffle_colors()
            await asyncio.sleep(0.1)


