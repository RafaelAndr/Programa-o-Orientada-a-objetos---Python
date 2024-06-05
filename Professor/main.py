from Professor import Professor
from ProfessorUfs import ProfessorUFS

def main():
    professor = Professor("kenia", 20220001, 15)
    professor.maisHoras(6)
    print(professor.getCarga())
    professor.menosHoras(8)
    print(professor.getCarga())
    professor.setNome("admilson")
    print(professor.getNome())
    
    professor = ProfessorUFS("admilson", 20220001, 15, 8, 20)
    professor.maisHoras(6)
    print(professor.getCarga())
    professor.menosHoras(8)
    print(professor.getCarga())
    professor.setNome("kenia")
    print(professor.getNome())
 
if __name__ == "__main__":
  main()