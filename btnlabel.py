#∂‘ª∞øÚ–°≤‚ ‘
from Tkinter import *
def on_click():
    if label['text']=='no way out':
        label['text'] = 'be on your own'
    else:
        label['text'] = 'no way out'
root = Tk(className = 'bitunion')
label = Label(root)
label['text'] = 'be on your own'
label.pack()
button = Button(root)
button['text'] = 'change it'
button['command'] = on_click
button.pack()
root.mainloop()
