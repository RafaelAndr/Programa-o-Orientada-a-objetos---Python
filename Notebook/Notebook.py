import random

class Notebook:
    def __init__(self):
        self.__notes = []

    def storeNote(self,note):
        self.__notes.append(note)

    def getList(self):
        return self.__notes

    def numberOfNotes(self):
        return len(self.__notes)

    def setNote(self, noteNumber, novaNota):
        self.__notes[noteNumber] = novaNota

    def getNote(self, noteNumber):
        return self.__notes[noteNumber]

    def showNote(self,noteNumber):
        if noteNumber < 0:
            print("Este não é um número de nota válido")

        elif noteNumber < self.numberOfNotes():
            print(self.__notes[noteNumber])

        else:
            print("Este não é um número de nota válido")

    def removeNote(self, note):
        if note in self.__notes:
            self.__notes.remove(note)
        else:
            print("Esta não é uma nota válida")

    def listNotes(self):
        index = 0
        while index < self.numberOfNotes():
            print(self.__notes[index])
            index += 1

    def listNotesFor(self):
        for nota in self.__notes:
            print(nota)

    def hasNotes(self):
        return len(self.__notes) > 0

    def compareNote(self, nomeNota):
        return nomeNota in self.__notes

    def showNoteRandom(self):
        nota_aleatoria = random.choice(self.__notes)
        print("Nota aleatória: ")
        print(nota_aleatoria)

    def showMultiNoteRandom(self, numero):
        print("Notas Aleatórias: ")
        contador = numero
        while contador > 0:
            valores = random.choice(self.__notes)
            print(valores)
            contador -= 1