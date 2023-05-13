'''Aplicación de notas: Desarrolla una aplicación de notas donde los usuarios puedan crear, editar y guardar notas en una
interfaz gráfica. Puedes incluir funciones como resaltado de texto, cambio de fuente y tamaño, y 
capacidad de guardar y cargar notas.'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
ventana=tk.Tk()
ventana.geometry('440x500')
ventana_texto=tk.Text(ventana,height=5)

#caja=tk.Entry(ventana)
# caja.pack()



def abrir_ventana_texto():
    ventana_texto.grid(column=0,row=2,columnspan=99)
    ventana_texto.focus()

Boton_crear=ttk.Button(ventana,text='Crear nota',command=abrir_ventana_texto)
Boton_crear.grid(column=0,row=0,columnspan=9,padx=100)
def guardar_nota1():
    global nota_guardada1
    nota_guardada1=ventana_texto.get(0.0, tk.END)
  
def guardar_nota2():
    global nota_guardada2
    nota_guardada2=ventana_texto.get(0.0, tk.END)
        
def guardar_nota3():
    global nota_guardada3
    nota_guardada3=ventana_texto.get(0.0, tk.END)
    
def guardar_nota4():
    global nota_guardada4
    nota_guardada4=ventana_texto.get(0.0, tk.END)
    
def guardar_nota5():
    global nota_guardada5
    nota_guardada5=ventana_texto.get(0.0, tk.END)



def cargar_nota1():
    caja_texto_cargada.delete('1.0','end')
    caja_texto_cargada.insert(tk.END,nota_guardada1)
    
def cargar_nota2():
    caja_texto_cargada.delete('1.0','end')
    caja_texto_cargada.insert(tk.END,nota_guardada2)
    
def cargar_nota3():
    caja_texto_cargada.delete('1.0','end')
    caja_texto_cargada.insert(tk.END,nota_guardada3)
    
def cargar_nota4():
    caja_texto_cargada.delete('1.0','end')
    caja_texto_cargada.insert(tk.END,nota_guardada4)
    
def cargar_nota5():
    caja_texto_cargada.delete('1.0','end')
    caja_texto_cargada.insert(tk.END,nota_guardada5)
    
boton_guardar_nota1=ttk.Button(ventana,text='Guardar nota 1',command=guardar_nota1,width=13).grid(column=0,row=5,columnspan=1,padx=0)
boton_guardar_nota2=ttk.Button(ventana,text='Guardar nota 2',command=guardar_nota2,width=13).grid(column=1,row=5,columnspan=1,padx=0)
boton_guardar_nota3=ttk.Button(ventana,text='Guardar nota 3',command=guardar_nota3,width=13).grid(column=2,row=5,columnspan=1,padx=0)
boton_guardar_nota4=ttk.Button(ventana,text='Guardar nota 4',command=guardar_nota4,width=13).grid(column=3,row=5,columnspan=1,padx=0)
boton_guardar_nota5=ttk.Button(ventana,text='Guardar nota 5',command=guardar_nota5,width=13).grid(column=4,row=5,columnspan=1,padx=0)
def ventana_guardados():
    global ventana_notas_guardadas 
    global caja_texto_cargada 
    ventana_notas_guardadas=tk.Tk()
    caja_texto_cargada=tk.Text(ventana_notas_guardadas,height=5)
    caja_texto_cargada.grid(column=1,row=2)
    
    boton_lista_cargada1=ttk.Button(ventana_notas_guardadas,text='Nota 1',command=cargar_nota1)
    boton_lista_cargada1.grid(column=1,row=3)
    
    boton_lista_cargada2=ttk.Button(ventana_notas_guardadas,text='Nota 2',command=cargar_nota2)
    boton_lista_cargada2.grid(column=1,row=4)
    
    boton_lista_cargada3=ttk.Button(ventana_notas_guardadas,text='Nota 3',command=cargar_nota3)
    boton_lista_cargada3.grid(column=1,row=5)
    
    boton_lista_cargada4=ttk.Button(ventana_notas_guardadas,text='Nota 4',command=cargar_nota4)
    boton_lista_cargada4.grid(column=1,row=6)
    
    boton_lista_cargada5=ttk.Button(ventana_notas_guardadas,text='Nota 5',command=cargar_nota5)
    boton_lista_cargada5.grid(column=1,row=7)
    
    

    ventana_notas_guardadas.mainloop()


global ventana_notas_guardadas
boton_cargar=ttk.Button(ventana,text='Cargar nota',command=ventana_guardados)
boton_cargar.grid(column=0,row=4,columnspan=9)








ventana.mainloop()