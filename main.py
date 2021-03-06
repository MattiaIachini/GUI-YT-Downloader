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

def formatMP4Download():
    link = URL.get()
    if radio.get() == 0:
        quality = "low"
    if radio.get() == 1:
        quality = "medium"
    if radio.get() == 2:
        quality = "high"
    if radio.get() == 3:
        quality = "very high"
    youtube_downloader.download_video(link, quality)
    info.config(text = "Download MP4 di: " + link)

def formatMP3Downlaod():
    link = URL.get()
    info.config(text = "Download MP4 di: " + link)
    filename = youtube_downloader.download_video(link, 'low')
    info.config(text = "Convert to MP3 di: " + link)
    file_converter.convert_to_mp3(filename)

def formatMP4PlaylistDownload():
    link = URL.get()
    info.config(text = "Download MP4 di: " + link)
    youtube_downloader.download_playlist(link, quality)

def formatMP3PlaylistDownload():
    link = URL.get()
    info.config(text = "Download Playlist e conversione di: " + link)
    youtube_downloader.download_playlistMP3(link, quality)


#windows__________________________________________________________________________________________
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
btDownload = tk.Button(text = "Download", bd = 0, command = formatMP4Download)
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

#________________________________________________________________________________________________
if __name__ == "__main__":
    window.mainloop()