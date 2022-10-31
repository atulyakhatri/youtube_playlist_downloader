from pytube import Playlist
import sys

print(sys.argv[1])
playlist = Playlist(sys.argv[1])

print('Number of videos in playlist: %s' % len(playlist.video_urls))
for video in playlist.videos:
    video.streams.filter(progressive=True,
                               file_extension='mp4').order_by(
        'resolution').desc().first().download()
