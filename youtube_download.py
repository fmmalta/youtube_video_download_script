from pytube import YouTube
from sys import argv
import os

link = argv[1]
yt = YouTube(link)
desktop = os.path.join(os.path.join(os.path.expanduser("~")), "Desktop")

yd = yt.streams.get_highest_resolution()
if yd is not None:
    yd.download(desktop)
