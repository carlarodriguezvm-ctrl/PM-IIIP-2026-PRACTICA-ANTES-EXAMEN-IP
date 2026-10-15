import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from datetime import datetime

import logic
import sty

def view():
    # VENTANA PRINCIPAL
    ventana = ttk.Window()

    ventana.geometry(f"{sty.VENTANA_ANCHO}x{sty.VENTANA_ALTO}")
    ventana.resizable(False, False)

    # Configuramos las dos columnas del formulario.
    ventana.columnconfigure(0, weight=1)
    ventana.columnconfigure(1, weight=1)


    # TÍTULO DEL FORMULARIO
    lblTitulo = ttk.Label(
        ventana,
        text="FORMULARIO",
        font=sty.FUENTE_TITULO,
        bootstyle=sty.BOOTSTYLE_TITULO
    )

    lblTitulo.grid(
        row=0,
        column=0,
        columnspan=2,
        pady=sty.PAD_TITULO_Y
    )


    # ETIQUETAS
    lblNombre = ttk.Label(
        ventana,
        text="Nombre:",
        font=sty.FUENTE_ETIQUETA,
        bootstyle=sty.BOOTSTYLE_TITULO
    )
    lblNombre.grid(row=1, column=0, padx=sty.PAD_X, pady=sty.PAD_Y, sticky="e")


    lblApellido = ttk.Label(
        ventana,
        text="Apellido:",
        font=sty.FUENTE_ETIQUETA,
        bootstyle=sty.BOOTSTYLE_TITULO
    )
    lblApellido.grid(row=2, column=0, padx=sty.PAD_X, pady=sty.PAD_Y, sticky="e")


    lblCedula = ttk.Label(
        ventana,
        text="Cédula:",
        font=sty.FUENTE_ETIQUETA,
        bootstyle=sty.BOOTSTYLE_TITULO
    )
    lblCedula.grid(row=3, column=0, padx=sty.PAD_X, pady=sty.PAD_Y, sticky="e")


    lblFechaNacimiento = ttk.Label(
        ventana,
        text="Fecha de nacimiento:",
        font=sty.FUENTE_ETIQUETA,
        bootstyle=sty.BOOTSTYLE_TITULO
    )
    lblFechaNacimiento.grid(row=4, column=0, padx=sty.PAD_X, pady=sty.PAD_Y, sticky="e")


    lblSexo = ttk.Label(
        ventana,
        text="Sexo:",
        font=sty.FUENTE_ETIQUETA,
        bootstyle=sty.BOOTSTYLE_TITULO
    )
    lblSexo.grid(row=5, column=0, padx=sty.PAD_X, pady=sty.PAD_Y, sticky="e")


    # ENTRADAS DE DATOS

    entrada_nombre = ttk.Entry(
        ventana,
        font=sty.FUENTE_ETIQUETA,
        bootstyle=sty.BOOTSTYLE_ETIQUETA
    )
    entrada_nombre.grid(row=1, column=1, padx=sty.PAD_X, pady=sty.PAD_Y, sticky="ew")


    entrada_apellido = ttk.Entry(
        ventana,
        font=sty.FUENTE_ETIQUETA,
        bootstyle=sty.BOOTSTYLE_ETIQUETA
    )
    entrada_apellido.grid(row=2, column=1, padx=sty.PAD_X, pady=sty.PAD_Y, sticky="ew")


    entrada_cedula = ttk.Entry(
        ventana,
        font=sty.FUENTE_ETIQUETA,
        bootstyle=sty.BOOTSTYLE_ETIQUETA
    )
    entrada_cedula.grid(row=3, column=1, padx=sty.PAD_X, pady=sty.PAD_Y, sticky="ew")


    entrada_fecha = ttk.DateEntry(
        ventana,
        dateformat="%d/%m/%Y",
        bootstyle=sty.BOOTSTYLE_CALENDARIO
    )
    entrada_fecha.grid(row=4, column=1, padx=sty.PAD_X, pady=sty.PAD_Y, sticky="ew")


    # LISTA PARA SELECCIONAR EL SEXO
    entrada_sexo = ttk.Combobox(
        ventana,
        values=["Femenino", "Masculino"],
        state="readonly", #hace que no podamos modificar el combobox
        font=sty.FUENTE_ETIQUETA
    )
    entrada_sexo.grid(row=5, column=1, padx=sty.PAD_X, pady=sty.PAD_Y, sticky="ew")


    # FUNCIÓN PARA VALIDAR EL FORMULARIO Y MOSTRAR LOS DATOS
    def verificar_formulario():

        # Obtenemos el contenido de las entradas.
        nombre = entrada_nombre.get().strip()
        apellido = entrada_apellido.get().strip()
        cedula = entrada_cedula.get().strip()
        sexo = entrada_sexo.get()

        # Comprobamos que los campos de texto estén completos.
        if nombre == "" or apellido == "" or cedula == "" or sexo == "":
            Messagebox.show_error(  #porque dice show_error y no show_info hace RUIDO
                "Llene todos los campos del formulario.",
                "Error"
            )
            return

        # Obtenemos la fecha seleccionada en el calendario.
        fecha_texto = entrada_fecha.entry.get()

        # Convertimos el texto de la fecha a un objeto de fecha.
        try:
            fecha_nacimiento = datetime.strptime(
                fecha_texto,
                "%d/%m/%Y"
            ).date()

        except ValueError:
            Messagebox.show_error(
                "Seleccione una fecha de nacimiento válida.",
                "Error"
            )
            return

        # Comprobamos que la fecha de nacimiento no sea futura.
        hoy = datetime.now().date()

        if fecha_nacimiento > hoy:
            Messagebox.show_error(
                "La fecha de nacimiento no puede ser futura.",
                "Error"
            )
            return

        # Calculamos la edad utilizando la función del archivo logic.py.
        edad = logic.calcular_edad(fecha_nacimiento)

        # Unimos el nombre y el apellido para obtener el nombre completo.
        nombre_completo = nombre + " " + apellido

        # Mostramos todos los datos en una ventana emergente.
        Messagebox.show_info(
            f"Tu nombre completo es: {nombre_completo}\n"
            f"Tu número de identidad es: {cedula}\n"
            f"Sexo: {sexo}\n"
            f"Naciste el: {fecha_nacimiento.strftime('%d/%m/%Y')}\n"
            f"Tu edad es: {edad} años.",
            f"Hola, {nombre}"
        )


    # BOTÓN
    boton = ttk.Button(
        ventana,
        text="Llenar formulario",
        command=verificar_formulario,
        bootstyle="success"
    )

    boton.grid(
        row=6,
        column=0,
        columnspan=2,
        padx=sty.PAD_X,
        pady=sty.PAD_Y
    )


    # INICIAMOS LA VENTANA
    ventana.mainloop()