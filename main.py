from functools import partial
from tkinter import *
import tkinter as tk
import pytube
import youtube_downloader
import file_converter

def svuota():
    btMp4.grid_remove()
    btMp3.grid_remove()
    btPlaylistMp4.grid_remove()
    btPlaylistMp3.grid_remove()



def perMP4():
    svuota()
    btQuality.grid(row = 0, column = 0, padx = 120, pady = 10)



window = tk.Tk()
window.geometry("600x300")
window.title("YouTube Downloader");
window.resizable(False, False)
window.configure(background = '#262626')
#Home____________________________________________________________________________________________

btMp4 = tk.Button(text = "Download MP4", bd = 0, command = perMP4)
btMp3 = tk.Button(text = "Download MP3", bd = 0)
btPlaylistMp4 = tk.Button(text = "Download Playlist MP4", bd = 0)
btPlaylistMp3 = tk.Button(text = "Download Playlist MP3", bd = 0)

#btMp4
btMp4.grid(row = 0, column = 0, padx = 120, pady = 10)
btMp4.configure(background = '#FF7500')

#btMp3
btMp3.grid(row = 1, column = 0)
btMp3.configure(background = '#006DFF')

#btPlaylistMp4
btPlaylistMp4.grid(row = 0, column = 1, padx = 30, pady = 10)
btPlaylistMp4.configure(background = '#FF7500')

#btPlaylistMp3
btPlaylistMp3.grid(row = 1, column = 1)
btPlaylistMp3.configure(background = '#006DFF')

#Generale________________________________________________________________________________________
testo = tk.Label(text = "Link youtube:")


#MP4_____________________________________________________________________________________________
btQuality = tk.Menubutton(text = 'qualita')
btQuality.menu = tk.Menu(btQuality)
btQuality['menu'] = btQuality.menu
low = 0
medium = 1
high = 2
very_high = 3

btQuality.menu.add_checkbutton(label = 'bassa', variable = low)
btQuality.menu.add_checkbutton(label = 'media', variable = medium)
btQuality.menu.add_checkbutton(label = 'alta', variable = high)
btQuality.menu.add_checkbutton(label = 'suprema', variable = very_high)
 

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