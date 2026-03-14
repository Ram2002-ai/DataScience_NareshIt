import tkinter
from PIL import Image,ImageTk
import random

# top-level widget which represents the main window of an application
root=tkinter.Tk()
# root.geometry('400**400')
root.title('ROLLING THE DICE')

# designing the buttons
# adding label into the frame
Blankline=tkinter.Label(root,text='')
Blankline.pack()

# adding label with different font and formating

headinglabel=tkinter.Label(root,text='Hello from Rsam',
        fg='light green',
        bg='dark green',
        font='Helvetica 16 bold italic')
headinglabel.pack()

# images
dice = ['die1.png', 'die2.png', 'die3.png', 
    'die4.png', 'die5.png', 'die6.png']


# simulating the dice with random number b/w 0-6
diceimage=ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image (only once)
imagelabel=tkinter.Label(root,image=diceimage)
imagelabel.image=diceimage

# packing a widget in the parent widget
imagelabel.pack(expand=True)

# function activated by button
def rolling_dice():
    diceimage=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    #  update image
    imagelabel.configure(image=diceimage)

    # keep a reference
    imagelabel.image=diceimage

# adding button and command will use rolling_dice functions
button=tkinter.Button(root,text='Roll the Dice',fg='blue',command=rolling_dice)

# pack a widget in the parent widget
button.pack(expand=True)

# call the mainloop of TK
# keeps window open
root.mainloop()
