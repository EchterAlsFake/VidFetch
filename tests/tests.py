from pytube import YouTube
from tqdm import tqdm


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


# URL of the YouTube video
url = 'https://www.youtube.com/watch?v=lke-ZjdCXaM'

yt = YouTube(url)
yt.register_on_progress_callback(custom_progress_bar)
stream = yt.streams.get_highest_resolution()
print(f"Downloading: {stream.title}")
stream.download()
print("\nDownload completed!")
