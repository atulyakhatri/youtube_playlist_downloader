from pytube import Playlist

playlist = Playlist('https://youtube.com/playlist?list=PLu0W_9lII9aiXlHcLx-mDH1Qul38wD3aR')
print('Number of videos in playlist: %s' % len(playlist.video_urls))
for video in playlist.videos:
    video.streams.filter(progressive=True,
                               file_extension='mp4').order_by(
        'resolution').desc().first().download()
