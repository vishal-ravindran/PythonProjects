from pytube import YouTube
from sys import argv

folder_save_path = r'C:\Users\Visha\Videos\Python video'
link = argv[1] #wnd argument in the terminal, 1st will be program name

yt = YouTube(link)

print("Details..")
print("Title : ", yt.title)
print("views : ", yt.views)
print("id : ", yt.video_id)

video = yt.streams.get_highest_resolution()

video.download(f"{folder_save_path}")