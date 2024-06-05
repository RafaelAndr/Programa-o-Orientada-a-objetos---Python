import tkinter as tk

def calcular():
    try:
        num1 = float(entrada_num1.get())
        num2 = float(entrada_num2.get())
        operacao = operacao_var.get()

        if operacao == "+":
            resultado.set(num1 + num2)
        elif operacao == "-":
            resultado.set(num1 - num2)
        elif operacao == "*":
            resultado.set(num1 * num2)
        elif operacao == "/":
            resultado.set(num1 / num2)
    except ValueError:
        resultado.set("Erro")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("200x200")

# Variáveis
entrada_num1 = tk.Entry(janela)
entrada_num2 = tk.Entry(janela)
operacao_var = tk.StringVar()
resultado = tk.StringVar()

# Rótulos
rotulo_num1 = tk.Label(janela, text="Número 1:")
rotulo_num2 = tk.Label(janela, text="Número 2:")
rotulo_resultado = tk.Label(janela, text="Resultado:")

# Botões
botao_calcular = tk.Button(janela, text="Calcular", command=calcular)

# Menu suspenso (DropDown) para a operação
menu_operacao = tk.OptionMenu(janela, operacao_var, "+", "-", "*", "/")
operacao_var.set("+")  # Operação padrão

# Posicionamento dos widgets na janela
rotulo_num1.grid(row=0, column=0)
rotulo_num2.grid(row=1, column=0)
rotulo_resultado.grid(row=2, column=0)
entrada_num1.grid(row=0, column=1)
entrada_num2.grid(row=1, column=1)
menu_operacao.grid(row=0, column=2)
botao_calcular.grid(row=2, column=1)
tk.Label(janela, textvariable=resultado).grid(row=2, column=1, columnspan=2)

# Iniciar o loop principal da aplicação
janela.mainloop()

