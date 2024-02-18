import os
import tomllib

with open('config.toml', 'rb') as f:
    data = tomllib.load(f)

# Convert video settings from config file into ffmpeg
def videoSettings(filename):
    string = f'ffmpeg -i \"{filename}\" -vf scale={data['resolution']} -crf {data['quality']} -preset {data['preset']}'
    if data['fastStart']:
        string += ' -movflags +faststart'
    if data['copyAudio']:
        string += ' -c:a copy'
    string += f' \"1080 {filename}\"'
    return string

# Find all files in working directory
dir = os.getcwd()
files = os.listdir(dir)
check = 0

# Find all video files to be reencoded and verify ffmpeg exists
videolist = []
for filename in files:
    if filename == 'ffmpeg.exe':
        check += 1
    if filename.endswith(('.mp4', '.mov', '.MOV', '.avi', '.mpg')):
        print('video found')
        videolist.append(filename)
if check == 0:
    print('ffmpeg not found')
    exit()

for video in videolist:
    string = videoSettings(video)
    os.system(string)

