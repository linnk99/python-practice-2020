from lamp018 import Lamp

def run():
    lamp = Lamp(_is_turned_on=False)
    
    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        '''))
        
        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        elif command == 's':
            break
        else:
            print('Comando invalido, elige otra opcion.')

if __name__ == "__main__":
    run()