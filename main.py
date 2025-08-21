import sys
import os
from src.tarea1 import sinusoidal_signal
from src.tarea1 import exponential_signal
from src.tarea1 import triangular_signal_of_frequency
from src.tarea1 import square_frequency_signal
from src.tarea2 import continous_sinusoidal_sign
from src.tarea3 import sinusoidal_cont_signal
from src.tarea3 import sinusoidal_disc_signal
from src.tarea4 import DAC
from src.ExamenP1 import dft
from src.ExamenP2 import examen_p2


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')                                                            

def main(options):
    
    if options[1] == "tarea1":
        clear()
        print("\033[1;36m  _______                     __ \033[0m")
        print("\033[1;36m |__   __|                   /_ |\033[0m")
        print("\033[1;36m    | | __ _ _ __ ___  __ _   | |\033[0m")
        print("\033[1;36m    | |/ _` | '__/ _ \/ _` |  | |\033[0m")
        print("\033[1;36m    | | (_| | | |  __/ (_| |  | |\033[0m")
        print("\033[1;36m    |_|\__,_|_|  \___|\__,_|  |_|\033[0m")                      
        print("\n")
        
        if len(options) < 3:
            print("\n   \033[1;31mPor favor, Escoja Una Señal A Graficar.\033[0m")
            print("\n   \033[1;33mEjemplo\033[0m: python main.py tarea1 sinusoidal_signal")
            print("   \033[1;33mEjemplo\033[0m: python main.py tarea1 exponential_signal")
            print("   \033[1;33mEjemplo\033[0m: python main.py tarea1 triangular_signal_of_frequency")
            print("   \033[1;33mEjemplo\033[0m: python main.py tarea1 square_frequency_signal")
            print("\n")
            return            
        
        clear()    
        if options[2] == "sinusoidal_signal":
            sinusoidal_signal()
        elif options[2] == "exponential_signal":
            exponential_signal()
        elif options[2] == "triangular_signal_of_frequency":
            triangular_signal_of_frequency()
        elif options[2] == "square_frequency_signal":
            square_frequency_signal()  
        else:
            print("\n   Por favor, escoja una señal a graficar")
        
    elif options [1] == "tarea2":
        clear()
        print("\033[1;36m  _______                     ___  \033[0m")
        print("\033[1;36m |__   __|                   |__ \ \033[0m")
        print("\033[1;36m    | | __ _ _ __ ___  __ _     ) |\033[0m")
        print("\033[1;36m    | |/ _` | '__/ _ \/ _` |   / / \033[0m")
        print("\033[1;36m    | | (_| | | |  __/ (_| |  / /_ \033[0m")
        print("\033[1;36m    |_|\__,_|_|  \___|\__,_| |____|\033[0m")
        print("\n")
              
        if len(args) > 2: 
            clear()
            continous_sinusoidal_sign(options[2])
        else:
            print("\n   \033[1;31mPorfavor, escoja una frecuencia.\033[0m")
            print("\n   \033[1;33mEjemplo\033[0m: Python main.py tarea2 6")
            print("\n")
            
    elif options[1] == "tarea3":
        clear()
        print("\033[1;36m  _______                      ____   \033[0m")
        print("\033[1;36m |__   __|                    |___ \  \033[0m")
        print("\033[1;36m    | | __ _ _ __ ___  __ _     __) | \033[0m")
        print("\033[1;36m    | |/ _` | '__/ _ \/ _` |   |__ <  \033[0m")
        print("\033[1;36m    | | (_| | | |  __/ (_| |   ___) | \033[0m")
        print("\033[1;36m    |_|\__,_|_|  \___|\__,_|  |____/  \033[0m")
        print("\n")
        
        if len(args) > 5:
            clear()
            tipo_de_senal = options[2]
            frequency = options[3]
            amplitude = options[4]
            fase = options[5]
            
            if tipo_de_senal == 'sinusoidal_cont_signal':
                sinusoidal_cont_signal(frequency, amplitude, fase)
                
            elif  tipo_de_senal == 'sinusoidal_disc_signal':
                sinusoidal_disc_signal(frequency, amplitude, fase)
            else:
                print(f"\n   Tipo de señal '{tipo_de_senal}' no reconocido.")
        
        else: 
            print("\n   \033[1;31mPorfavor, escoja una señal, una frecuencia, una amplitud y una fase en grados.\033[0m")
            print("\n   \033[1;33mEjemplo\033[0m: Python main.py tarea3 sinusoidal_cont_signal 6 2 20")            
            print("   \033[1;33mEjemplo\033[0m: Python main.py tarea3 sinusoidal_disc_signal 6 2 20")
            print("\n")
            
    elif options[1] == "ExamenP1":
        clear()
        dft()
        
    elif options[1] == "ExamenP2":
        clear()
        examen_p2()
    
                
    elif options [1] == "tarea4":
        clear()
        print("\033[1;36m  _______                      _  _   \033[0m")
        print("\033[1;36m |__   __|                    | || |  \033[0m")
        print("\033[1;36m    | | __ _ _ __ ___  __ _   | || |_ \033[0m")
        print("\033[1;36m    | |/ _` | '__/ _ \/ _` |  |__   _|\033[0m")
        print("\033[1;36m    | | (_| | | |  __/ (_| |     | | \033[0m")
        print("\033[1;36m    |_|\__,_|_|  \___|\__,_|     |_|  \033[0m")
        print("\n")
        
        if len(args) > 2: 
            clear()
            bits = options[2]
            DAC(bits)
                
        else:
            print("\n   \033[1;31mPorfavor ingrese un numero de bits, y recuerde que deber ser entero.\033[0m")
            print("\n   \033[1;33mEjemplo\033[0m: Python main.py tarea4 6")
            print("\n")
    else:
        clear()
        print("\n   \033[1;31mPor favor, ingresa un numero de bits entero.")
        print("\n   \033[1;33mEjemplo\033[0m: python main.py tarea4 2")
        print("\n")

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        clear()
        print("\n")
        print("\033[36m    _____         __  _____     __   __                    ___   ")
        print("   / ___/__ ____ / / / ___/__ _/ /__/ /__ _______  ___    / _ |  ")
        print("  / (_ / _ `/ -_) / / /__/ _ `/ / _  / -_) __/ _ \/ _ \  / __ |_ ")
        print("  \___/\_,_/\__/_/  \___/\_,_/_/\_,_/\__/_/  \___/_//_/ /_/ |_(_)\033[0m")
        print("\n")   
        print("\n   \033[1;31mPorfavor ingresa un argumento.\033[0m")
        print("\n   \033[1;33mEjemplo\033[0m: (actividad 1) >> Python main.py tarea1 sinusoidal_signal")
        print("   \033[1;33mEjemplo\033[0m: (actividad 2) >> Python main.py tarea2 6")
        print("   \033[1;33mEjemplo\033[0m: (actividad 3) >> Python main.py tarea3 sinusoidal_cont_signal 6 2 20")
        print("   \033[1;33mEjemplo\033[0m: (actividad 4) >> Python main.py tarea4 2")
        print("   \033[1;33mEjemplo\033[0m: (Examen Parte 1) >> Python main.py ExamenP1")
        print("   \033[1;33mEjemplo\033[0m: (Examen Parte 2) >> Python main.py ExamenP2")
        print("\n")
        
    