from tkinter import *
from pytube import YouTube

stage = Tk()
stage.geometry('500x400')
stage.resizable(0,0)
stage.title("Youtube video downloader")

Label(stage,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
##enter link
link = StringVar()
Label(stage, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(stage, width = 70,textvariable = link).place(x = 32, y = 90)
#function to download video
def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(stage, text = 'DONE', font = 'arial 15').place(x= 180 , y = 210)  

Button(stage,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'blue', padx = 2, command = Downloader).place(x=180 ,y = 150)

stage.mainloop()