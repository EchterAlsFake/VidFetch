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


def concat(video, audio, output):
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
    with tqdm(total=100, desc="Processing", ncols=100) as pbar:
        last_progress = 0
        for progress in ff.run_command_with_progress():
            pbar.update(progress - last_progress)
            last_progress = progress


def cleanup(file):
    os.remove(f"{file}.mp4")
    os.remove(f"{file}.mp3")


def download_video(resolutions, y, title, random_int, output):
    for counter, resolution in enumerate(resolutions):
        print(f"{counter}) {resolution}")

    selected_resolution = input(f"{return_color()}Enter the video resolution --=>: {reset()}")
    print(f"{return_color()}Downloading video for: {title}{reset()}")
    y.streams.filter(resolution=resolutions[int(selected_resolution)]).first().download(filename=random_int + ".mp4")
    print(f"{return_color()}Downloading audio for: {title}{reset()}")
    y.streams.filter(only_audio=True).first().download(filename=random_int + ".mp3")
    print(f"{return_color()}Concatenating videos and audio for: {title}{reset}")
    concat(audio=random_int + ".mp3", video=random_int + ".mp4", output=output)
    cleanup(random_int)
    print(f"{return_color()}Done!{reset()}")


def download_audio(y, title, output):
    print(f"{return_color()}Downloading audio for: {title}{reset()}")
    y.streams.filter(only_audio=True).first().download(filename=output)
    print(f"{return_color()}Done!{reset()}")


class CLI:
    def __init__(self):
        setup_config_file()
        self.conf = ConfigParser()
        self.conf.read("config.ini")
        self.load_user_settings()
        self.output_path = "./"
        while True:
            try:
                self.main_menu()

            except Exception as e:
                print(f"{return_color()}Error! --: {e}{reset()}")

    def main_menu(self):
        options = input(f"""
{return_color()}1) Download a video
{return_color()}2) Download an audio (mp3)
{return_color()}3) Download a playlist
{return_color()}4) Settings
{return_color()}-------------=>:""")

        if options == "1":
            url = input(f"{return_color()}Enter the video url --=>: {reset()}")
            self.pre_setup(url, mode=1)

        elif options == "2":
            url = input(f"{return_color()}Enter the video url --=>: {reset()}")
            self.pre_setup(url, mode=2)

        elif options == "3":
            self.download_playlist()

    def pre_setup(self, url, mode):

        if type(url) == "str":
            y = check_url(url)

        else:
            y = url

        title = strip_title(y.title)
        if not self.output_path.endswith("/") or self.output_path.endswith("\\"):
            self.output_path += os.sep

        resolutions = get_available_resolutions(url)
        output_video = self.output_path + title + ".mp4"
        output_music = self.output_path + title + ".mp3"
        random_int = str(random.randint(0, 10000))
        y.register_on_progress_callback(custom_progress_bar)

        if mode == 1:
            download_video(resolutions=resolutions, y=y, title=title, random_int=random_int, output=output_video)

        elif mode == 2:
            download_audio(y=y, title=title, output=output_music)

    def download_playlist(self):
        url = input(f"{return_color()}Enter the playlist url --=>: {reset()}")
        p = check_playlist(url)
        videos = p.videos
        video_objects = []

        print(f"{return_color()}Loading video objects... This can take some time!{reset()}")
        for counter, video in enumerate(videos):
            print(f"{counter}) {video.title}")
            video_objects.append(video)

        choices = input(f"{return_color()}Enter the number of the video you want to download (1,2,3,4,18,43) "
                        f"(enter 'all' for all)--=>:")
        mode = input(f"{return_color()}Enter the download mode [1] = Video [2] = Music --=>:")

        if choices == "all":
            for video in video_objects:
                self.pre_setup(video, mode=int(mode))

        else:
            selected_videos = choices.split(",")
            for video in selected_videos:
                self.pre_setup(video_objects[int(video)], mode=int(mode))

    def load_user_settings(self):
        self.output_path = self.conf["VidFetch"]["output_path"]

    def settings(self):
        options = input(f"""
1) Change output path


""")

        if options == "1":
            new_path = input(f"{return_color()}Enter the new output path --=>: {reset}")
            if os.path.exists(new_path):
                self.conf["VidFetch"]["output_path"] = new_path

            else:
                print(f"{return_color()}Invalid path!{reset()}")
                self.settings()

        else:
            print(f"{return_color()}Invalid option!{reset()}")
            self.settings()


























CLI()










