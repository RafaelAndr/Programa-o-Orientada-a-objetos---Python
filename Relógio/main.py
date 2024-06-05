from ClockDisplay import ClockDisplay
from NumberDisplay import NumberDisplay

def main():
    horario = NumberDisplay(24)
    horario.increment()
    print(horario.getDisplayValue())
    horario.setValue(4)
    print(horario.getValue())

    horario = ClockDisplay()
    print(horario.getDisplayValue())
    horario.timeTick()
    print(horario.getTime())
    horario.setTime(16, 30, 40)
    print(horario.getTime())
  
if __name__ == "__main__":
    main()