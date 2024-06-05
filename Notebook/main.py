from Notebook import Notebook

def main():
    notebook = Notebook()


    while True:
        print("MENU")
        print("1. Adicionar uma nova nota")
        print("2. Mostrar o número de notas")
        print("3. Mostrar uma nota específica")
        print("4. Remover uma nota")
        print("5. Mostrar todas as notas")
        print("6. Verificar se há notas")
        print("7. Verificar se uma nota específica existe")
        print("8. Mostrar uma nota aleatória")
        print("9. Mostrar várias notas aleatoriamente")
        print("10. Sair")

        choice = input("Escolha uma opção (1-10): ")

        if choice == "1":
            note_text = input("Digite o texto da nota: ")
            notebook.storeNote(note_text)
            print("Nota adicionada com sucesso!")

        elif choice == "2":
            num_notes = notebook.numberOfNotes()
            print(f"Total de notas: {num_notes}")

        elif choice == "3":
            note_number = int(input("Digite o número da nota que deseja ver: "))
            notebook.showNote(note_number)

        elif choice == "4":
            note_text = input("Digite o texto da nota que deseja remover: ")
            notebook.removeNote(note_text)
            print("Nota removida com sucesso!")

        elif choice == "5":
            notebook.listNotesfor()

        elif choice == "6":
            if notebook.hasNotes():
                print("Há notas na coleção.")
            else:
                print("A coleção está vazia.")

        elif choice == "7":
            note_to_find = input("Digite a nota que deseja verificar: ")
            if notebook.compareNote(note_to_find):
                print("A nota existe na coleção.")
            else:
                print("A nota não existe na coleção.")

        elif choice == "8":
            notebook.showNoteRandom()

        elif choice == "9":
            num_notes = int(input("Digite o número de notas que deseja mostrar: "))
            notebook.showMultiNoteRandom(num_notes)

        elif choice == "10":
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Escolha uma opção válida (1-10).")


if __name__ == "__main__":
    main()