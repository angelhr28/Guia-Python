from tkinter import *
from tkinter.ttk import Combobox
window = Tk()
window.title("Sistemas inteligentes")
window.geometry('350x200')
lbl1 = Label(window,text="Hola mundo",bg="red")
lbl1.grid(column=0,row=0)
txt1 = Entry(window,width=10)
txt1.grid(column=0,row=1)
def mostrar():
    mensaje = "Hola mundo "+txt1.get() + " "+combo.get()
    lbl1.configure(text=mensaje)
btn1 = Button(window,text="mostrar",command=mostrar)
btn1.grid(column=1,row=0)
combo = Combobox(window)
combo['values'] = (1,2,3,4,"Text")
combo.current(1)
combo.grid(column=0,row=2)
window.mainloop()
