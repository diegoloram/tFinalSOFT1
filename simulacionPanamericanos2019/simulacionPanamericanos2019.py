import tkinter
import randomPaises

#PRINCIPAL
# -*- coding: utf-8 -*-
import tkinter as tk
ventana=tk.Tk()
ventana.title("")

#AnchoxAlto
ventana.geometry("700x600")
ventana.configure(background="white")




etiqueta1=tk.Label(ventana,text="Paises:",bg="white",fg="black",font=("Verdana",20))
etiqueta1.pack(padx=20,pady=20,side=tk.LEFT)

image=tk.PhotoImage(file="1.gif")
image=image.subsample(1,1)
label=tk.Label(image=image)
label.pack()


generar= tkinter.Button(text = "Generar", command = "")
generar.pack()
generar.place(bordermode = tkinter.OUTSIDE, x = 75, y = 400)


ventana.mainloop()

lista = randomPaises.rand(10)

print(lista)
