import os
import yt_dlp
# from moviepy.editor import VideoFileClip
# import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))
downloads_path = os.path.join(script_dir, "..", "downloads")
downloads_path = os.path.normpath(downloads_path)

def download(url, fileName):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4][vcodec=h264]+bestaudio[ext=m4a][acodec=aac]/best[ext=mp4]',
        'outtmpl': os.path.join(downloads_path, f'{fileName}.%(ext)s'),
        'noplaylist': True,
        'quiet': False,
        'verbose': True,
        'no_warnings': True
    
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except:
            return False
    
    # clip = VideoFileClip(f"{downloads_path}/{fileName}.mp4")
    # clip.write_videofile(f"{downloads_path}/{fileName}.mp4", codec='libx264', audio_codec='libfdk_aac')