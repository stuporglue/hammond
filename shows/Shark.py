from shows.Show import *
from openrgb.utils import RGBColor
import random

class Shark(Show):
    audiofile = 'jaws.wav'
    old_shark = [-1,-1,-1,-1,-1,-1]
    cur_shark = [12,24,11,23,10,22]
    direction = -1

    shark_color = RGBColor(0,0,0)
    min_idx = 0
    max_idx = 24

    @classmethod
    async def light_show(self):

        self.w = Features.Waves.get_instance()

        # Dark blue
        self.w.dark_water()
        self.print_shark()

        for i in range(0,100):
            self.bounce_shark()
            await asyncio.sleep(0.25)

        self.w.shuffle_colors()

    @classmethod
    def print_shark(self):
        # print(self.cur_shark)

        for i in self.old_shark:
            self.w.zone.colors[i] = random.choice(self.w.dark_water_colors)

        for i in self.cur_shark:
            self.w.zone.colors[i] = self.shark_color

        self.w.zone.show()

    @classmethod
    def bounce_shark(self):

        # import pdb
        # pdb.set_trace()

        if ( self.direction == -1 and (0 in self.cur_shark or 14 in self.cur_shark )):
            self.direction = 1

        if ( self.direction == 1 and (13 in self.cur_shark or 24 in self.cur_shark )):
            self.direction = -1

        self.shark_move()
        self.print_shark()

    @classmethod
    def shark_move(self):
        for i in range(0,len(self.cur_shark)):
            self.old_shark[i] = self.cur_shark[i]
            self.cur_shark[i] += self.direction


    @classmethod
    def light(self,num):
        for i in range(0,len(self.w.zone.colors)):
            self.w.zone.colors[i] = RGBColor(0,0,0)
        self.w.zone.colors[num] = self.shark_color
        self.w.zone.show()



