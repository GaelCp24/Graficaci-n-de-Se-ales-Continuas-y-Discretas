import sys
from src.tarea1 import sinusoidal_signal
from src.tarea1 import exponential_signal
from src.tarea1 import triangular_signal_of_frequency
from src.tarea1 import square_frequency_signal
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
clear_console()
    
def main():
    while True: 
        print("\n   Bienvenido. ¿Que programa deseas correr?")
        print("\n   ____________________")
        print("\n   1.- Tarea 1")
        print("   2.- Salir")
        print("   ____________________")
        
        option = input("\n   Ingresa Una Opcion [1] [2]:    ")
        option = int(option)
        
        if option == 1:
            
            while True:
                clear_console()
                print("\n   ¿Que Onda Te Gustaria Ver?")
                print("\n   ____________________")
                print("\n   1.- Señal Sinusoidal De Frecuencia")
                print("   2.- Señal Exponencial")
                print("   3.- Señal Triangular")
                print("   4.- Señal Cuadrada")
                print("   5.- Regresar")
                print("   ____________________")
                
                homework_option = input("\n   Ingresa Una Opcion [1] [2] [3] [4] [5]:    ")
                homework_option = int(homework_option)
                
                if homework_option == 1:
                    sinusoidal_signal()
                    
                elif homework_option == 2:
                    exponential_signal()
                
                elif homework_option == 3:
                    triangular_signal_of_frequency()
                    
                elif homework_option == 4:
                    square_frequency_signal()
                    
                elif homework_option == 5:
                    clear_console()
                    print("\n   Regresando...")
                    break
                    
                else:
                    print("\n   Entrada No Valida.")
                    
        elif option == 2:
            
            print("\n   Saliendo...")
            print("\n")
            break

if __name__ == "__main__":
    main()
            
                    
                    
                    
                
                
    