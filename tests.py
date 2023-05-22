from pytube import YouTube

y = YouTube(url="https://www.youtube.com/watch?v=etfX6YVb2ms&pp=ygUIOGsgdmlkZW8%3D")

data = y.streams.all()

for stream in data:
    print(stream.resolution)