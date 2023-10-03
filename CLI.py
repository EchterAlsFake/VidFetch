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
import random

from shared_functions.functions import *
from configparser import ConfigParser
from ffmpeg_progress_yield import FfmpegProgress
from hue_shift import reset, return_color


class CLI:
    def __init__(self):
        setup_config_file()
        self.conf = ConfigParser()
        self.conf.read("config.ini")
        self.load_user_settings()
        self.output_path = "./"
        self.main_menu()

    def main_menu(self):
        options = input(f"""
{return_color()}1) Download a video
{return_color()}2) Download an audio (mp3)
{return_color()}3) Download a playlist
{return_color()}4) Settings
{return_color()}-------------=>:""")

        if options == "1":
            url = input(f"{return_color()}Enter the video url --=>: {reset()}")
            self.download_video(url)

        elif options == "2":
            url = input(f"{return_color()}Enter the video url --=>: {reset()}")
            self.download_audio(url)

    def download_audio(self, url):
        get_audio_stream(url).download()

    def download_video(self, url):

        resolutions = get_available_resolutions(url)
        for counter, resolution in enumerate(resolutions):
            print(f"{counter}) {resolution}")

        selected_resolution = input(f"{return_color()}Enter the video resolution --=>: {reset()}")
        y = YouTube(url)
        title = strip_title(y.title)
        if not self.output_path.endswith("/") or self.output_path.endswith("\\"):
            self.output_path += os.sep

        output = self.output_path + title + ".mp4"
        random_int = str(random.randint(0, 10000))

        y.register_on_progress_callback(custom_progress_bar)
        print(f"{return_color()}Downloading video for: {title}{reset()}")
        y.streams.filter(resolution=resolutions[int(selected_resolution)]).first().download(filename=random_int + ".mp4")
        print(f"{return_color()}Downloading audio for: {title}{reset()}")
        y.streams.filter(only_audio=True).first().download(filename=random_int + ".mp3")
        print(f"{return_color()}Concatenating videos and audio for: {title}{reset}")
        self.concat(audio=random_int + ".mp3", video=random_int + ".mp4", output=output)
        os.remove(random_int + ".mp4")
        os.remove(random_int + "mp3")
        print(f"{return_color()}Done!{reset()}")

    def concat(self, video, audio, output):
        setup_ffmpeg()

        command = [
            'ffmpeg',
            '-i', f'{video}',
            '-i', f'{audio}',
            '-c:v', 'copy',
            '-c:a', 'aac',
            '-strict', 'experimental',
            f'{output}'
        ]

        ff = FfmpegProgress(command)
        with tqdm(total=100, desc="Processing", ncols=100, colour=return_color()) as pbar:
            last_progress = 0
            for progress in ff.run_command_with_progress():
                pbar.update(progress - last_progress)
                last_progress = progress

    def load_user_settings(self):
        self.output_path = self.conf["VidFetch"]["output_path"]





























CLI()










