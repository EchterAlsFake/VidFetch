import os
from pytube import YouTube
from tqdm import tqdm

resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p", "3840p"]


def setup_config_file(force=False):
    data = """
[VidFetch]
quality = best





"""

class TqdmToLogger(tqdm):
    def __init__(self, *args, **kwargs):
        super(TqdmToLogger, self).__init__(*args, **kwargs)

    def print_bar(self, bytes_remaining, total_size):
        self.total = total_size
        self.n = total_size - bytes_remaining
        self.last_print_n = self.n
        self.refresh()


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


def get_available_resolutions(url):
    streams = YouTube(url).streams.order_by("resolution")
    available_resolutions = []
    for resolution in resolutions:
        for stream in streams:
            if stream.resolution == resolution:
                if not stream.resolution in available_resolutions:
                    available_resolutions.append(stream.resolution)

    return available_resolutions


def check_url(url):
    if YouTube(url):
        return True


def get_highest_resolution(url):
    y = YouTube(url)
    resolutions = y.streams.order_by("resolution")
    return resolutions[-1].itag


def get_audio_stream(url):
    return YouTube(url).streams.get_audio_only()
