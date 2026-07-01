from tkinter import *
import tkinter.messagebox as mb
import json
import requests

# functions
def extrac_lyrics():
    global artist,song
    artist_name=str(artist.get())
    song_name=str(song.get()).lower()
    link="https://api.lyrics.ovh/v1/"+artist_name.replace(' ','%20')+'/'+song_name.replace(' ','%20')

    try:
        req=requests.get(link)
        req.raise_for_status()
        json_data=req.json()

        lyrics=json_data.get('lyrics',None)

        if lyrics:
            print(lyrics)
            mb.showinfo('Lyrics printed',"The lyrics to the song you wanted have been extracted and printed on your command terminal.")

        else:
            raise ValueError('Lyrics not found')
        
    except requests.exceptions.RequestException as e:
        mb.showerror('Network Error',f"An error occurred whiletrying to fetch the lyrics:{e}")

    except Exception as e:
        mb.showerror("No such song found",'We were unable to findsuch a song in our directory.Please recheck the name of the artist and the song, and if correct , we apologize because we do not have that song available with us.')

# Initializing the window
root=Tk()
root.title('SONG LYRICS EXTRACOR')
root.geometry("800x250")
root.resizable(100,25)
root.config(bg='CadetBlue')

# Placing the componets
Label(root, text=" Song Lyrics Extractor", font=("Comic Sans MS", 16, 'bold'), bg='CadetBlue').pack(side=TOP, fill=X)

Label(root, text='Enter the song name: ', font=("Times New Roman", 14), bg='CadetBlue').place(x=20, y=50)
song = StringVar()
Entry(root, width=40, textvariable=song, font=('Times New Roman', 14)).place(x=200, y=50)

Label(root, text="Enter the artist's name: ", font=("Times New Roman", 14), bg='CadetBlue').place(x=20, y=100)
artist = StringVar()
Entry(root, width=40, textvariable=artist, font=('Times New Roman', 14)).place(x=200, y=100)

Button(root, text='Extract lyrics', font=("Georgia", 10), width=15, command=extrac_lyrics).place(x=220, y=150)

# Finalizing the window
root.mainloop()