from pytube import YouTube


def get_highest_resolution(youtube_object):  # YouTube object must be an object from Pytube

    resolutions = ["144p", "240p", "360p", "480p", "720p", "1080p", "1440p", "2160p", "3840p"]
    y = youtube_object
    data = y.streams.all()  # I know this is deprecated, but it's the only way to get a list of resolutions.
    valid_resolutions = []


    for resolution in resolutions:

        for stream in data:

            if stream.resolution == resolution:
                valid_resolutions.append(resolution)

    return valid_resolutions

url = "https://youtube.com/watch?v=wJnBTPUQS5A"
y = YouTube(url)

z = get_highest_resolution(y)

for data in z:
    print(data)