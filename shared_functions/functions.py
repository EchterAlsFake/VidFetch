import os
import sys
import wget

from pytube import YouTube, exceptions, Playlist
from tqdm import tqdm

resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p", "3840p"]

def setup_ffmpeg():
    if not os.path.isfile("../ffmpeg") or not os.path.isfile("../ffmpeg.exe"):

        if os.path.isfile("../ffmpeg.exe"):
            print("ffmpeg.exe found")

        elif os.path.isfile("../ffmpeg"):
            print("ffmpeg found")

        print(f"Downloading ffmpeg...")

        if sys.platform == "linux":
            wget.download("https://drive.google.com/uc?export=download&id=1TjnA9oISF58DWWZ0zss22uJuQYi3ltLU", out="../ffmpeg")

        elif sys.platform == "win":
            wget.download("https://drive.google.com/uc?export=download&id=1hls6bh_TFux8Agk5y9VkaEJ3LlXcNTIq", out="../ffmpeg.exe")

def create_config_file():
    with open("config.ini", "w") as config:
        config.close()


def setup_config_file(force=False):
    data = """
[VidFetch]
output_path = ./
default_quality = highest
default_codec = aac
default_mode = music



"""

    if not os.path.isfile("../config.ini") or force:
        create_config_file()

        with open("config.ini", "w") as config:
            config.write(data)


class TqdmToLogger(tqdm):
    def __init__(self, *args, **kwargs):
        super(TqdmToLogger, self).__init__(*args, **kwargs)

    def print_bar(self, bytes_remaining, total_size):
        self.total = total_size
        self.n = total_size - bytes_remaining
        self.last_print_n = self.n
        self.refresh()


def strip_title(title):
    disallowed_characters = ["/", "\\", ":", "*", "?", "\"", "<", ">", "|", "'", '"', "[", "]"]
    for disallowed_character in disallowed_characters:
        title = title.replace(disallowed_character, "")

    return title


def custom_progress_bar(stream, chunk, bytes_remaining):
    # If the progress bar doesn't exist, initialize it
    if not hasattr(custom_progress_bar, "_bar"):
        total_size = stream.filesize
        custom_progress_bar._bar = TqdmToLogger(
            total=total_size, unit='B', unit_scale=True, unit_divisor=1024, desc=stream.title
        )
    # Update the progress bar
    custom_progress_bar._bar.print_bar(bytes_remaining, stream.filesize)
    # Close the progress bar when download is finished
    if bytes_remaining == 0:
        custom_progress_bar._bar.close()
        del custom_progress_bar._bar


def get_available_resolutions(y):
    streams = y.streams.order_by("resolution")
    available_resolutions = []
    for resolution in resolutions:
        for stream in streams:
            if stream.resolution == resolution:
                if not stream.resolution in available_resolutions:
                    available_resolutions.append(stream.resolution)

    return available_resolutions


def check_url(url):
    try:
        return YouTube(url)

    except exceptions.RegexMatchError:
        print(f"Invalid URL! : {url}")


def check_playlist(url):
    try:
        return Playlist(url)

    except exceptions.RegexMatchError:
        print(f"Invalid URL! : {url}")


def get_highest_resolution(y):
    resolutions = y.streams.order_by("resolution")
    return resolutions[-1].itag
