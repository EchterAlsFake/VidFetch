"""
Copyright (C) 2023  EchterAlsFake | Johannes Habel

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

"""
Vid Fetch (CLI) is a YouTube Downloader which supports up to 8K resolution with
ffmpeg mixing and converting between codecs.

This application is open-source which means, you can view and modify the complete code!
The code will always be available at:

https://github.com/EchterAlsFake/VidFetch

Thanks :) """

data = """

[VidFetch]

output_path_music = music/
output_path_video = video/


"""



import sys
import os
import socket
import requests
import random

from colorama import *
from pytube import *
from tqdm import tqdm
