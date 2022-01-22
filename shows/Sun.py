from shows.Show import *

class Sun(Show):
    audiofile = 'explosion4.wav'

    async def light_show():
        s = Features.Sun.get_instance()
        while True:
            s.shuffle_colors()
            await asyncio.sleep(0.1)


