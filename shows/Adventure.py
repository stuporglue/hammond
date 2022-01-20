from shows.Show import *

class Adventure(Show):

    audiofile = 'jungle_adventure_short.wav'
    #executable = 'beep.sh'

    @staticmethod
    async def light_show():
        v = Features.Volcano.get_instance()
        c = Features.Clouds.get_instance()
        t = Features.Tree.get_instance()
        w = Features.Waves.get_instance()
        print("Doing light show")
        await asyncio.sleep(0.5)

