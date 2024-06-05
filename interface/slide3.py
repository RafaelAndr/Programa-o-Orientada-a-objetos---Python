from tkinter import *
def inc():
    n = int(rotulo.configure("text")[4])+1
    rotulo.configure(text=str(n))

tk = Tk()
tk.geometry("200x200")
    
b = Button(text="Incrementa",command=inc)
b.configure(background="Blue")
b.pack()
rotulo = Label(text="0")
rotulo.pack()
mainloop()



from tkinter import *

class MainFrame:
    def __init__(self, parent):
        self.principal = Menu(root)
        self.arquivo = Menu(self.principal)
        self.rafael = Menu(self.principal)
        self.arquivo.add_command(label="Abrir",command=self.abrir)
        self.arquivo.add_command(label="Salvar", command=self.salvar)
        self.arquivo.add_command(label="Opções", command=self.opcoes)
        self.principal.add_cascade(label="Arquivo",menu=self.arquivo)
        self.principal.add_command(label="Ajuda", command=self.ajuda)
        self.rafael.add_command(label="Sobrenome", command=self.sobrenome)
        self.rafael.add_command(label="Principio", command=self.guardar)
        self.principal.add_cascade(label="Rafael", menu=self.rafael)
        parent.configure(menu=self.principal)

    def sobrenome(self):
        print("Nascimento")
    def guardar(self):
        print("Guardando")
    def abrir(self):
         print("abrir")
    def salvar(self):
         print("salvar")
    def ajuda(self):
        print("ajuda")
    def opcoes(self):
        print("opções")

root = Tk()
app = MainFrame(root)
root.mainloop()



from tkinter import *

def alo(): 
     print("Alo!")

root = Tk()
menu = Menu(root, tearoff=0)
menu.add_command(label="Alo 1", command=alo)
menu.add_command(label="Alo 2", command=alo)

def popup(e): 
    menu.post(e.x_root, e.y_root)

frame = Frame(root, width=200, height=200)
frame.pack()
frame.bind("<Button-3>", popup)
mainloop()

root = Tk()
app = alo(root)
root.mainloop()



from tkinter import *
def clica(e):
    txt = "Mouse clicado em\n%d,%d"%(e.x,e.y)
    r.configure(text=txt)

r = Label()
r.pack(expand=True, fill="both")
r.master.geometry("250x250")
r.bind("<Button-1>", clica)
mainloop()  