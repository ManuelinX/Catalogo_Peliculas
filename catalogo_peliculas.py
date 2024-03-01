import tkinter as tk
from client.gui_app import Frame, barra_menu
def main():
    root = tk.Tk()
    root.title("Catalogo de Peliculas")
    root.iconbitmap("img/peli.ico")
    root.resizable(1,1)#modificar hacia los lados, y hacia arriba y abajo, true o false
    app = Frame(root = root)
    
    barra_menu(root)
    
    app.mainloop()#deve ir al final de nuestra ejecucion


if __name__ == '__main__':
    main()