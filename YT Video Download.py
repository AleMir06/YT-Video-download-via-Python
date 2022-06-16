#pip install pytube

import pytube

link = input("Enter Youtube Video URL")
yt = pytube.YouTube(link)
yt.streams.get_highest_resolution().download()
print("downloaded", link)
