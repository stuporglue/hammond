from shows.Show import *
import random

class JurrasicPark(Show):

    executable = 'jurrasic_park_beep.sh'

    @staticmethod
    async def light_show():
        feats = [
                Features.Volcano.get_instance(),
                Features.Clouds.get_instance(),
                Features.Tree.get_instance(),
                Features.Waves.get_instance()
            ]
        while True:
            random.choice(feats).shuffle_colors()
            await asyncio.sleep(0.1)

