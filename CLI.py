from shared_functions.functions import *




class CLI:
    def __init__(self):
        self.main_menu()


    def main_menu(self):
        options = input(f"""
1) Download a video
2) Download an audio
3) Download a playlist
4) Settings""")

        if options == "1":
            url = input("Enter the video url --=>: ")
            self.download_video(url)

        elif options == "2":
            url = input("Enter the video url --=>: ")
            self.download_audio(url)






    def download_audio(self, url):
        get_audio_stream(url).download()


    def download_video(self, url):
        resolutions = get_available_resolutions(url)
        print(resolutions)
        for counter, resolution in enumerate(resolutions):
            print(f"{counter}) {resolution}")

        selected_resolution = input("Enter the video resolution --=>: ")
        y = YouTube(url)
        y.register_on_progress_callback(custom_progress_bar)
        y.streams.filter(resolution=resolutions[int(selected_resolution)]).first().download()


    def concat(self):
        ""
































CLI()










