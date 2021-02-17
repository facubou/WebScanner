#Download Videos from youtube and convert to mp3

from pytube import YouTube
import os
import moviepy.editor as mp
import re

folder = r"C:\Users\user1\Songs"
 
list_urls = ['https://www.youtube.com/watch?v=QGDqhpnrIqI',
             'https://www.youtube.com/watch?v=7MJvKW2KVJQ'
             ]

for url in list_urls:
  try:
      yt_obj = YouTube(url)
  
      yt_obj.streams.get_audio_only().download(output_path='', filename=yt_obj.title)
      print('YouTube video audio downloaded successfully')
  except Exception as e:
      print(e)

for file in os.listdir(folder):
  if re.search('mp4', file):
    mp4_path = os.path.join(folder,file)
    mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
    new_file = mp.AudioFileClip(mp4_path)
    new_file.write_audiofile(mp3_path)
    os.remove(mp4_path)
