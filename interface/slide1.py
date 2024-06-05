from tkinter import *
root = Tk()
conteudo = Frame(root)
conteudo.pack()
button1 = Button(conteudo)
button1.configure(text="Hello world")
button1.configure(background="green")
root.mainloop()

from tkinter import *
class MainFrame:
    def __init__(self, myParent):
        self.conteudo = Frame(myParent)
        self.conteudo.pack()
        self.button1 = Button(self.conteudo)
        self.button1.configure(text="Hello world")
        self.button1.configure(background="green")
        self.button1.pack()

root = Tk()
myapp = MainFrame(root)
root.mainloop()

from tkinter import *
class MainFrame:
    def __init__(self, parent):
        self.principal=Menu(parent)
        self.arquivo=Menu(self.principal)
        self.arquivo.add_command(label="Abrir")
        self.arquivo.add_command(label="Salvar")
        self.principal.add_cascade(label="Arquivo",menu=self.arquivo)
        self.principal.add_command(label="Ajuda")
        parent.configure(menu=self.principal)
        
root=Tk()
app = MainFrame(root)
root.mainloop()
