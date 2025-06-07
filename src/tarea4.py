import numpy as np
import matplotlib.pyplot as plt
from src.utils.grapher import discrete_plotter

def DAC(bits):
    bits = int(bits)
    VFS = 5.0
    N = bits
    niveles = 2 ** N
    paso = VFS / (niveles - 1)
    resolution = (paso / VFS) * 100
    
    print(f"\n   Tarea 4 >> DAC de {bits} bits")
    print(f"   Número de niveles: {niveles}")
    print(f"   Tamaño del paso: {paso:.6f} V")
    print(f"   Resolución porcentual: {resolution:.6f} %")
    print("\n")
    
    inputs = np.arange(niveles)
    outputs = inputs * paso
    
    discrete_plotter(
        inputs, outputs,
        f'DAC de {bits} bits', 'Salida Analogica', 
        'Nivel Digital De Entrada', 'Voltaje Analogico [V]'
    )