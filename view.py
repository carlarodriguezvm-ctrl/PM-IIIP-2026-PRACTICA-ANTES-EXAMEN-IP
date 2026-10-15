import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox

import sty

ventana = ttk.Window()
ventana.geometry(f"{sty.VENTANA_ANCHO}x{sty.VENTANA_ALTO}")
ventana.resizable(False, False)

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)


#CAMPOS 
lblTitulo = ttk.Label(
    ventana,
    text="FORMULARIO",
    font=sty.FUENTE_TITULO,
    bootstyle=sty.BOOTSTYLE_TITULO,
)
lblTitulo.grid(
    row=0, 
    column=0,
    columnspan=2, 
    pady=sty.PAD_TITULO_Y
)

lblTitulo = ttk.Label(
    ventana,
    text="Nombre: ",
    font=sty.FUENTE_ETIQUETA,
    bootstyle=sty.BOOTSTYLE_TITULO
)
lblTitulo.grid(
    row=1, 
    column=0, 
    columnspan=2, 
    pady=sty.PAD_TITULO_Y
)

lblTitulo = ttk.Label(
    ventana,
    text="Apellido: ",
    font=sty.FUENTE_ETIQUETA,
    bootstyle=sty.BOOTSTYLE_TITULO
)
lblTitulo.grid(
    row=2, 
    column=0, 
    columnspan=2, 
    pady=sty.PAD_TITULO_Y
)

lblTitulo = ttk.Label(
    ventana,
    text="Cedula: ",
    font=sty.FUENTE_ETIQUETA,
    bootstyle=sty.BOOTSTYLE_TITULO
)
lblTitulo.grid(
    row=3, 
    column=0, 
    columnspan=2, 
    pady=sty.PAD_TITULO_Y
)

lblTitulo = ttk.Label(
    ventana,
    text="Fecha de Nacimiento: ",
    font=sty.FUENTE_ETIQUETA,
    bootstyle=sty.BOOTSTYLE_TITULO
)
lblTitulo.grid(
    row=4, 
    column=0, 
    columnspan=2, 
    pady=sty.PAD_TITULO_Y
)

#ENTRADAS
ENTRADA_NOMBRE = ttk.Entry(
    ventana,
    font=sty.FUENTE_ETIQUETA,
    bootstyle=sty.BOOTSTYLE_ETIQUETA
)
ENTRADA_NOMBRE.grid(
    row=1,      
    column=3,
    padx=sty.PAD_X, 
    pady=sty.PAD_Y, 
    sticky="w"
)

entrada_apellido = ttk.Entry(
    ventana,
    font=sty.FUENTE_ETIQUETA,
    bootstyle=sty.BOOTSTYLE_ETIQUETA
)
entrada_apellido.grid(
    row=2,
    column=3,
    padx=sty.PAD_X,
    pady=sty.PAD_Y,
    sticky="w"
)

ENTRADA_CEDULA = ttk.Entry(
    ventana, 
    font=sty.FUENTE_ETIQUETA,
    bootstyle=sty.BOOTSTYLE_ETIQUETA    
)
ENTRADA_CEDULA.grid(
    row=3,
    column=3,
    padx=sty.PAD_X,
    pady=sty.PAD_Y,
    sticky="w"
)

fecha_entry = ttk.DateEntry(
    ventana, 
    dateformat="%d/%m/%Y", 
    bootstyle=sty.BOOTSTYLE_CALENDARIO
)
fecha_entry.grid(
    row=4, 
    column=3, 
    padx=sty.PAD_X, 
    pady=sty.PAD_Y, 
    sticky="w"
)


boton = ttk.Button(
    ventana,
    
)
ventana.mainloop()