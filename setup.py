#!/usr/bin/env python3

# some_file.py
import random
import sys
import os
import errno
import time

import openrgb
import time

from openrgb import OpenRGBClient
from openrgb.utils import RGBColor, DeviceType

client = OpenRGBClient()
mobo = client.get_devices_by_name('ASRock B550 Phantom Gaming-ITX/ax')[0]
meter = mobo.zones[4]

razer = client.get_devices_by_name('Razer Chroma Addressable RGB Controller')[0]
ocean = razer.zones[0]
trees = razer.zones[2]
cloud = razer.zones[3]
sun = razer.zones[4]
volcano = razer.zones[5]


def reset_colors():
	o_colors = [
		RGBColor(0,0,255),
		RGBColor(153,193,255),
		RGBColor(250,111,113),
		RGBColor(153,193,255),

		RGBColor(100,100,255),
		RGBColor(217,255,74),
		RGBColor(217,255,74),
		RGBColor(217,255,74),

		RGBColor(0,0,255),
		RGBColor(0,142,255),
		RGBColor(36,100,0),
		RGBColor(255,255,0),

	]*2 + [RGBColor(0,0,255)]

	t_colors = [RGBColor(0,0,0)]*3


	v_colors = [RGBColor(255,0,0)]*30

	c_colors = [RGBColor(255,255,255)]*30

	s_colors = [RGBColor(255,255,0)]*6

	sun.set_colors(s_colors,fast=True)
	ocean.set_colors(o_colors,fast=True)
	volcano.set_colors(v_colors,fast=True)
	cloud.set_colors(c_colors,fast=True)
	trees.set_colors(t_colors,fast=True)
