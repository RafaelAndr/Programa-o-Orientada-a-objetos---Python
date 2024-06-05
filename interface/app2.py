from tkinter import *

# Função a ser executada quando o botão for clicado
def mostrar_mensagem():
    label.configure(text="Olá, Mundo!")

# Cria uma janela
janela = Tk()
janela.title("Minha Interface Gráfica")
janela.geometry("250x250")

# Cria uma etiqueta
label = Label(text="Bem-vindo ao Tkinter!")
label.pack(pady=50)

# Cria um botão
botao = Button(text="Clique em mim", command=mostrar_mensagem)
botao.pack()
botao.configure(font="times new roman")
# Inicia o loop principal da aplicação
janela.mainloop()
