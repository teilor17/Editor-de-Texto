import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename
class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Teilor Zapata - Editor de texto')
        self.iconbitmap('icono.ico')
        #configuracion tamaño minimo de la ventana
        self.rowconfigure(0, minsize=600, weight=1)
        #configuramos el maximo de columnas que vamos a tener
        self.columnconfigure(1, minsize=600, weight=1)
        #atributo de campo de texto
        self.camp_text = tk.Text(self, wrap=tk.WORD)
        #atribto de archivo
        self.archivo = None
        # atribut para saber si ya se abrio un archivo a
        self.archivo_abierto = False
        #creacion de componentes
        self._crear_componentes()
        #crear menu
        self._crear_menu()

    def _crear_componentes(self):
        frame_botones = tk.Frame(self, relief=tk.RAISED, bd=2)
        boton_abrir = tk.Button(frame_botones, text='Abrir', command=self._abrir_archivo)
        boton_guardar = tk.Button(frame_botones, text='Guardar', command=self._guardar_archivo)
        boton_guar_como = tk.Button(frame_botones, text='Guardar Como..', command=self._guardar_como)
        # los botones se expanden de manera Horizontal
        boton_abrir.grid(row=0, column=0, sticky='we', padx=5, pady=5)
        boton_guardar.grid(row=1, column=0, sticky='we', padx=5, pady=5)
        boton_guar_como.grid(row=2, column=0, sticky='we', padx=5, pady=5)
        # se coloca el frma de manera vertical
        frame_botones.grid(row=0, column=0, sticky='ns')
        #agregamos el campo de texto se exppandira en el espacio que reste
        self.camp_text.grid(row=0, column=1, sticky='nswe')

    def _crear_menu(self):
        #creamos el menu de app
        menu_app = tk.Menu(self)
        self.config(menu=menu_app)
        #agregar las opciones del menu
        #agregamos el menu archivo
        menu_archivo = tk.Menu(menu_app, tearoff=False)#tearoff no se puede separa de la aplicacion ya que seria un menu flotante
        menu_app.add_cascade(label='Archivo', menu=menu_archivo)
        #agregar opciones del sub menu archivo
        menu_archivo.add_command(label='Abrir', command=self._abrir_archivo)
        menu_archivo.add_command(label='Guardar', command=self._guardar_archivo)
        menu_archivo.add_command(label='Guardar Como..', command=self._guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label='Salir', command=self.quit)#quit es un metodo ya definido que nor permite salir

    def _abrir_archivo(self):
        #abrimor el archivo para ediion
        self.archivo_abierto = askopenfile(mode='r+')
        # eliminamos el texto anterio de la caja
        self.camp_text.delete(1.0, tk.END)
        # revisamos si efectivamente hay un archivo
        if not self.archivo_abierto:
            return
        #abrimoe el archivo en modo lectura escritura
        with open(self.archivo_abierto.name, 'r+') as self.archivo:
            #ya abierto leemos el contenido
            texto = self.archivo.read()
            # insertamos el contenido en el campo de text
            self.camp_text.insert(1.0, texto)
            # modificamos el titulo de la aplicaion al nombre del archivo que abrimos
            self.title(f'*Editor texto - {self.archivo.name}')

    def _guardar_archivo(self):
        #si ya se abrio un archivo lo guardamos
        if self.archivo_abierto:
            #salvamos el archivo
            with open(self.archivo_abierto.name, 'w') as self.archivo:
                #leemos el contenido de la caja de texto
                texto = self.camp_text.get(1.0, tk.END)
                # escribimos ese contenido al mismo archivo
                self.archivo.write(texto)
                #cambiamos el nombre del titlo de la add
                self.title(f'Editor texto - {self.archivo.name}')
        else:
            self._guardar_como()
    def _guardar_como(self):
        #si estamos aca es por que no estamos editando ningun archivo
        self.archivo = asksaveasfilename(
            defaultextension='txt',
            filetypes=[('Archivos de texto', '*.txt'), ('Todos los archivos', '*.*')]
        )
        if not self.archivo:
            return
        #abrimos el archivo en modo escritura
        with open(self.archivo, 'w') as self.archivo:
            #leemos el contenido de la caja de texto
            texto = self.camp_text.get(1.0, tk.END)
            #guardamos ese contenido
            self.archivo.write(texto)
            #cambiamos el titulo de la palicacion
            self.title(f'Editor de texto - {self.archivo.name}')
            #indicamos que ya heos abierto este archivo
            self.archivo_abierto = self.archivo
            self.title(f'+Editor de texto - {self.archivo.name}')



if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()