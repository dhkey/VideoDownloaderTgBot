import os
import yt_dlp

script_dir = os.path.dirname(os.path.abspath(__file__))
downloads_path = os.path.join(script_dir, "..", "downloads")
downloads_path = os.path.normpath(downloads_path)


def download(url, fileName):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(downloads_path, f'{fileName}.%(ext)s'),
        'noplaylist': True,
        'quiet': False,
        'verbose': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
