import tkinter

prozor = tkinter.Tk()
prozor.geometry("800x600")

slika = tkinter.PhotoImage(file="delorean.png")

natpis = tkinter.Label(prozor,text='Delorian - Pedja')
delorean = tkinter.Label(prozor,font=('Areal',24),text='Delorean')
delorean.place(x=50,y=20)
natpis.place(x=50,y=0)


prozor.mainloop()