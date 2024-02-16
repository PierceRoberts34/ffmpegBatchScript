# ffmpegBatchScript
Batch convert all files in a folder with ffmpeg
# Requirements
Python Version 3+

[ffmpeg](https://www.ffmpeg.org/) should be placed in the same folder as the python script

# Usage
Settings are found in `config.toml`. 

`resolution` controls target final scale. Default is 1920:1080

`quality` governs variable bitrate. Lower numbers mean higher quality, higher numbers mean smaller files. Suggested values are 18-23, sane range is 17-28, 0 is lossless

`preset` controls compression efficiency. Values are ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow, and placebo (Do not use placebo)

`copyAudio` means the audio will not be encoded. Default is true.

`fastStart` is for videos meant to be viewed in a browser. Default is true
