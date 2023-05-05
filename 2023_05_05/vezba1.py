import tkinter

prozor = tkinter.Tk()
prozor.title("Glavni prozor")
prozor.geometry("800x600")

ime = tkinter.Label(
    prozor,
    font=('Times New Roman',18,),
    text="Predrag Sanader",
    background='yellow')
ime.pack(side=tkinter.LEFT,anchor="s")
prezime=tkinter.Label(
    prozor,
    font=('Times New Roman', 18),
    text='Pedja', background='purple')
# prezime.pack( expand = True, fill = "x")
prezime.pack(side=tkinter.RIGHT, anchor='e')

prozor.mainloop()