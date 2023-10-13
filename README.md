<img src="https://github.com/EchterAlsFake/VidFetch/blob/master/graphics/VidFetch.jpg" alt="Alt text" style="border-radius: 8px;">

### [Development Status v1.0](htttps://github.com/EchterAlsFake/VidFetch/blob/master/READMEs/DEVELOPMENT.md)

### Table of contents
- [Introduction](#what-is-vidfetch)
- [Supported Platforms](#supported-platforms)
- [Features](#features)
- [Legal Information](#legal-information)
- [Building from Source](#building-from-source)
- [FFMPEG](#ffmpeg)
- [Credits](#credits)
- [License](#license)

# What is VidFetch?

VidFetch is a YouTube downloader based on the [Pytube API](https://github.com/pytube/pytube).
It has a graphical User Interface made with [PySide6](), it supports high-resolution videos, multiple
codecs and threaded downloads. (More is coming in the future!)

# Supported Platforms

- Windows
- Linux
- Android (CLI - Linux emulator) . Native apk is in development.
- iOS (iSH - Alpine Linux emulator)
- (Theoretically every system with Linux and a Terminal)

# Features

- Download up to 8K resolution
- Threaded downloads for better optimization
- Downloading videos from a playlist / file (with choices)
- Support for different codecs (AAC, MP3: more coming soon)


# Legal Information

This software comes with no liability for the owner.
You are responsible for your actions. YouTube can sue you, and you can get in a lot of trouble 
for downloading copyright protected videos! If that happens, I don't care.

# Building from Source

# ffmpeg

FFMPEG is a media encoder / decoder tool used in all heavy applications out there.
VidFetch uses it to concat audio and video together and convert to different codecs.




# Credits

- Project API: [Pytube](https://github.com/pytube/pytube)
- Hue Shift  : [Hue Shift](https://github.com/EchterAlsFake/hue_shift)
- tqdm       : [tqdm](https://github.com/tqdm/tqdm)
- ffmpeg     : [ffmpeg](https://ffmpeg.org/)
- ffmpeg-progress-yield: [ffmpeg-progress-yield](https://github.com/slhck/ffmpeg-progress-yield)

> ChatGPT helped me with coding (especially mathematical stuff like the progressbar)

# License

Vid Fetch is licensed under the GPL v3 License

Copyright (c) 2023 EchterAlsFake | Johannes Habel

See: [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)