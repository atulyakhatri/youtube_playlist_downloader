from pytube import Playlist
if __name__ == "__main__":
    name = input('Enter playlist url')
    playlist = Playlist(name)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    for video in playlist.videos:
        video.streams.filter(progressive=True,
                                   file_extension='mp4').order_by(
            'resolution').desc().first().download()

