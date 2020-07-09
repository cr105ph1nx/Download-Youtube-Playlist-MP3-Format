from pytube import YouTube #pip install pytube or pytube3
from pytube import Playlist
import os, re, subprocess, time

# Initialize Variables and Get Input
c = 1
playlist = Playlist("https://www.youtube.com/playlist?list=PLt1MjqWQPImEhLdNWrBOX3m6hE0XDI0ph")

def Download(yt):
    print("Downloading....")
    # Filter to only Audio Streams
    vids = yt.streams.filter(only_audio = True)
    # Get only .mp4 format
    vids[0].download(r"Tracks/tmp/")

def Convert(_filename):
    mp4 = "Tracks/tmp/'%s'.mp4" % _filename
    mp3 = "Tracks/'%s'.mp3" % _filename
    ffmpeg = ('ffmpeg -i %s ' % mp4 + mp3)
    subprocess.call(ffmpeg, shell = True)

def main(c, playlist):
    # Filter Playlist Url
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
    # Iterate Through Playlist
    print(len(playlist.video_urls))
    for url in playlist.video_urls:
        # Remove file in /tmp
        try:
            os.remove("Tracks/tmp/" + _filename + ".mp4")
        except:
            print("Error: No such file or directory...")

        # Rename file in /Tracks
        try:
            os.rename("Tracks/" + _filename + ".mp3", "Tracks/Track " + str(c) + ".mp3")
            c = c + 1
        except:
            print("Error: No such file or directory...")

        # Handle Url
        yt = YouTube(url)
        # Filename specification
        _filename = yt.title
        print(_filename)
        # Downloading
        Download(yt)
        # Converting
        Convert(_filename)

if __name__ == '__main__':
    main()
