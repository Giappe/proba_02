import tkinter
import random

prozor = tkinter.Tk()

slika = tkinter.PhotoImage(file='bonba.png')

def obrada(evt):
    if evt.widget.nekibroj:
        evt.widget


for i in range(10):
    for j in range(10):
        l = tkinter.Label(prozor,width=48,height=64,bitmap='question',font=('Arial',24),text="A",background='red')
        l.grid(row=i,column=j,padx=2,pady=2,ipadx=2,ipady=2)
        l.nekibroj = random.randint(0,1)

ciljni_label = prozor.winfo_children()[10]
ciljni_label['background'] = 'blue'


prozor.mainloop()

'''treba dovrsiti kod, nisam ispratio'''