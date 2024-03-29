import tkinter

window = tkinter.Tk()
menu = tkinter.Menu(window) 

window.title("Mundial Lista de Paises")
window.resizable(0, 0)
window.geometry('500x500')

#Menu
agregarM = tkinter.Menu(menu)
agregarM.add_command(label = 'Somos')
agregarM.add_separator()
agregarM.add_command(label = 'Salir', command = window.destroy)
menu.add_cascade(label = 'Archivo', menu = agregarM)

#label
tablaPos = tkinter.LabelFrame(window, text = "Tabla de Posiciones", height = 350, width = 350)
tablaPos.pack()

tablaText = tkinter.Text(tablaPos, height = 23, width = 45)
tablaText.pack()

#botones
generarR = tkinter.Button(text = "Generar Registro")
generarR.pack()
generarR.place(bordermode = tkinter.OUTSIDE, x = 75, y = 400)

grafico = tkinter.Button(text = "otro boton")
grafico.pack()
grafico.place(bordermode = tkinter.OUTSIDE, x = 200, y = 400)

btn = tkinter.Button(text = "Otro botton")
btn.pack()
btn.place(bordermode = tkinter.OUTSIDE, x = 300, y = 400)

window.config(menu = menu)
window.mainloop()
