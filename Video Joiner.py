from pytube import YouTube
from bs4 import BeautifulSoup
import requests
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

def getPlaylistLinks(url):
    sourceCode = requests.get(url).text
    soup = BeautifulSoup(sourceCode, 'html.parser')
    domain = 'https://www.youtube.com'
    number=0
    for link in soup.find_all("a", {"dir": "ltr"}):
        href = link.get('href')
        if href.startswith('/watch?'):
            print(link.string.strip())
            yt=YouTube(domain + href)
            videos=yt.streams.first()
            videos.download("/home/aditya/Desktop/PYTHON PROGRAMS/YouTube playlist joiner and cropper")
            print("100% == Downloaded")
            if(number):
                final_clip = VideoFileClip("Final_file.mp4")
                clip = VideoFileClip(yt.streams.first().default_filename)
                final_clip = concatenate_videoclips([final_clip,clip])
                final_clip.write_videofile("Final_file.mp4")
            else:
                final_clip=VideoFileClip(yt.streams.first().default_filename)
                final_clip.write_videofile("Final_file.mp4")
            os.remove("/home/aditya/Desktop/PYTHON PROGRAMS/YouTube playlist joiner and cropper/"+yt.streams.first().default_filename)
            number+=1
                
link = input("Enter the Playlist link :")

getPlaylistLinks(link)

#print("Number of videos downloaded"+number)
