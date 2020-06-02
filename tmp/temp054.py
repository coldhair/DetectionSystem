from tkinter import *

top = Tk()
L1 = Label(top, text="网站名")
L1.pack(side="top")
E1 = Text(top, bd=5)
E1.pack(side="bottom")

txt = Text.get('0,0')

print(txt)

L1 = Label(top, text="提高")
L1.pack(side="bottom")
top.mainloop()
