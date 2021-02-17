#Download all videos in a youtube list and convert to mp3

from pytube import Playlist
import os
import moviepy.editor as mp
import re

folder = r"C:\Users\user1\Songs\list"
 
try:
    playlist = Playlist('https://www.youtube.com/watch?v=AFWy1qyyMHE&list=PLkVSzrKdeIKUznc9C_1SCbYS-bVYtP3YF')
 
    for video in playlist.videos:
      video.streams.filter(only_audio=True).first().download()
 
except Exception as e:
    print(e)

for file in os.listdir(folder):
  if re.search('mp4', file):
    mp4_path = os.path.join(folder,file)
    mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
    new_file = mp.AudioFileClip(mp4_path)
    new_file.write_audiofile(mp3_path)
    os.remove(mp4_path)
