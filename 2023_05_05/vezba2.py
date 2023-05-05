import tkinter

prozor = tkinter.Tk()

ime = tkinter.Label(prozor,font=('Arial',24),text='Pedja', background='red')
ime.grid(row=0,column=0, sticky='we')
prezime = tkinter.Label(prozor,font=('Arial',24), text='Sanader',background='yellow')
prezime.grid(row=1,column=1)
je = tkinter.Label(prozor,font=('Arial', 24),text='Je',background='blue',foreground='white')
je.grid(row=2,column=3)
najjaci = tkinter.Label(prozor, font=('Arial',24), text='Najjaci', background='purple', foreground='White')
najjaci.grid(row=3, column=0, columnspan=3, sticky='we')

prozor.mainloop()