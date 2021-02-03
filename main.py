from functools import partial
from tkinter import *
import tkinter as tk
import pytube
import youtube_downloader
import file_converter

def svuota1():
    titolo.place_forget()
    btMp4.place_forget()
    btMp3.place_forget()
    btPlaylistMp4.place_forget()
    btPlaylistMp3.place_forget()
    btQuit.place_forget()

def svuota2():
    titoloURL.place_forget()
    URL.place_forget()
    btDownload.place_forget()
    btBack.place_forget()
    div.place_forget()
    info.place_forget()
    radioQLow.place_forget()
    radioQMedium.place_forget()
    radioQHigh.place_forget()
    radioQVeryHigh.place_forget()

def perMP4():
    svuota1()
    titoloURL.place(x = 275, y = 40)
    URL.place(x = 100, y = 60)
    btDownload.place(x = 400, y = 110)
    btBack.place(x = 10, y = 10)
    div.place(x = 100, y = 175)
    info.place(x = 0, y = 0)
    radioQLow.place(x = 100, y = 110)
    radioQMedium.place(x = 160, y = 110)
    radioQHigh.place(x = 220, y = 110)
    radioQVeryHigh.place(x = 280, y = 110)

def perMP3():
    svuota1()
    titoloURL.place(x = 275, y = 40)
    URL.place(x = 100, y = 60)
    btDownload.place(x = 400, y = 110)
    btBack.place(x = 10, y = 10)
    div.place(x = 100, y = 175)
    info.place(x = 0, y = 0)

def indietro():
    svuota2()
    titolo.place(x = 230, y = 10)
    btMp4.place(x = 130, y = 50)
    btMp3.place(x = 130, y = 80)
    btPlaylistMp4.place(x = 350, y = 50)
    btPlaylistMp3.place(x = 350, y = 80)
    btQuit.place(x = 565, y = 270)

def selection(): 
    if  radioQLow.select():
        radioQMedium.deselect()
        radioQHigh.deselect()
        radioQVeryHigh.deselect()
        quality = 0

    if  radioQMedium.select():
        radioQLow.deselect()
        radioQHigh.deselect()
        radioQVeryHigh.deselect()
        quality = 1

    if  radioQHigh.select():
        radioQMedium.deselect()
        radioQLow.deselect()
        radioQVeryHigh.deselect()
        quality = 2

    if  radioQVeryHigh.select():
        radioQMedium.deselect()
        radioQLow.deselect()
        radioQHigh.deselect()
        quality = 3



window = tk.Tk()
window.geometry("600x300")
window.title("YouTube Downloader");
window.resizable(False, False)
window.configure(background = '#262626')
#Dichiarazione____________________________________________________________________________________
radio = IntVar()
btQuit = tk.Button(text = "Exit", bd = 0, command = exit)
btMp4 = tk.Button(text = "Download MP4", bd = 0, command = perMP4)
btMp3 = tk.Button(text = "Download MP3", bd = 0, command = perMP3)
btPlaylistMp4 = tk.Button(text = "Download Playlist MP4", bd = 0, command = perMP4)
btPlaylistMp3 = tk.Button(text = "Download Playlist MP3", bd = 0, command = perMP3)
titolo = tk.Label(text = "Seleziona un'opzione:")
titoloURL = tk.Label(text = "URL:")
btDownload = tk.Button(text = "Download", bd = 0)
btBack = tk.Button(text = "Back", bd = 0, command = indietro)
URL = tk.Entry(width = 65, background = '#5C5B5D', bd = 0)
div = tk.Frame(width = 390, height = 100)
info = tk.Label(div, text = "")
radioQLow = tk.Radiobutton(window, text="Bassa", value = 0, variable = radio, command = selection)
radioQMedium = tk.Radiobutton(window, text="Media", value = 1, variable = radio, command = selection)
radioQHigh = tk.Radiobutton(window, text="Alta", value = 2, variable = radio, command = selection)
radioQVeryHigh = tk.Radiobutton(window, text="Molto Alta", value = 3, variable = radio, command = selection)

#titoli
titolo.place(x = 230, y = 10)
titolo.configure(background = '#262626', foreground="white")
titoloURL.configure(background = '#262626', foreground="white")

#radio
radioQLow.configure(background = '#262626', foreground="white")
radioQMedium.configure(background = '#262626', foreground="white")
radioQHigh.configure(background = '#262626', foreground="white")
radioQVeryHigh.configure(background = '#262626', foreground="white")

#btDownload
btDownload.configure(background = '#5C5B5D')

#btBack
btBack.configure(background = '#5C5B5D')

#btQuit
btQuit.place(x = 565, y = 270)
btQuit.configure(background = '#5C5B5D')

#btMp4
btMp4.place(x = 130, y = 50)
btMp4.configure(background = '#FF7500')

#btMp3
btMp3.place(x = 130, y = 80)
btMp3.configure(background = '#006DFF')

#btPlaylistMp4
btPlaylistMp4.place(x = 350, y = 50)
btPlaylistMp4.configure(background = '#FF7500')

#btPlaylistMp3
btPlaylistMp3.place(x = 350, y = 80)
btPlaylistMp3.configure(background = '#006DFF')

#Generale________________________________________________________________________________________
testo = tk.Label(text = "Link youtube:")

#MP4_____________________________________________________________________________________________


#MP3_____________________________________________________________________________________________


#PlaylistMP4_____________________________________________________________________________________


#PlaylistMP3_____________________________________________________________________________________




#________________________________________________________________________________________________
if __name__ == "__main__":
    window.mainloop()



    

"""
print('''
What do you want?

(1) Download YouTube Videos Manually
(2) Download a YouTube Playlist
(3) Download YouTube Videos and Convert Into MP3

''')

choice = input("Choice: ")

if choice == "1" or choice == "2":
    quality = input("Please choose a quality (low, medium, high, very high):")
    if choice == "2":
        link = input("Enter the link to the playlist: ")
        print("Downloading playlist...")
        youtube_downloader.download_playlist(link, quality)
        print("Download finished!")
    if choice == "1":
        links = youtube_downloader.input_links()
        for link in links:
            youtube_downloader.download_video(link, quality)
elif choice == "3":
    links = youtube_downloader.input_links()
    for link in links:
        print("Downloading...")
        filename = youtube_downloader.download_video(link, 'low')
        print("Converting...")
        file_converter.convert_to_mp3(filename)
else:
    print("Invalid input! Terminating...")
"""