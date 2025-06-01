import numpy as np
import matplotlib.pyplot as plt
from src.utils.grapher import combined_plotter
#importamos scipy.signal para poder construir una onda triangular
from scipy.signal import sawtooth
#importamos ahora con la mima libreria scipy square para la señal cuadrada
from scipy.signal import square

def sinusoidal_signal():
    frequency = 2
    amplitude = 2
    time_initial = 0
    time_final = 2
    
    # Señal Continua
    number_of_points = 1000
    t_cont = np.linspace(time_initial, time_final, number_of_points)
    x_cont = amplitude * np.sin(2 * np.pi * frequency * t_cont)
    
    # Señal discreta
    ts = 0.01
    t_disc = np.arange(time_initial, time_final, ts)
    x_disc = amplitude * np.sin(2 * np.pi * frequency * t_disc)
    
    combined_plotter(
        t_cont, x_cont,
        t_disc, x_disc,
        title='Señal Senoidal Continua y Muestreada',
        graph_label_cont='Señal Continua',
        graph_label_disc='Muestras',
        x_label='Tiempo [s]',
        y_label='Amplitud'
    )
    
def exponential_signal():
    time_initial = -2
    time_final = 5
    number_of_points = 1000
    ts = 0.1
    
    # Señal continua
    t_cont = np.linspace(time_initial, time_final, number_of_points)
    u_cont = np.where(t_cont >= 0, 1, 0)
    x_cont = np.exp(-2 * t_cont) * u_cont
    
    # Señal discreta
    t_disc = np.arange(time_initial, time_final, ts)
    u_disc = np.where(t_disc >= 0, 1, 0)
    x_disc = np.exp(-2 * t_disc) * u_disc

    combined_plotter(
        t_cont, x_cont,
        t_disc, x_disc,
        title='Señal Exponencial Con Escalón Unitario',
        graph_label_cont='Señal Continua',
        graph_label_disc='Muestras',
        x_label='Tiempo [s]',
        y_label='Amplitud'
    )

def triangular_signal_of_frequency():
    frequency = 2
    time_initial = 0
    time_final = 2
    number_of_points = 1000
    ts = 0.01  # Periodo de muestreo heurístico adecuado

    # Señal continua
    t_cont = np.linspace(time_initial, time_final, number_of_points)
    x_cont = sawtooth(2 * np.pi * frequency * t_cont, width=0.5)

    # Señal discreta
    t_disc = np.arange(time_initial, time_final, ts)
    x_disc = sawtooth(2 * np.pi * frequency * t_disc, width=0.5)

    # Graficar ambas
    combined_plotter(
        t_cont, x_cont,
        t_disc, x_disc,
        title='x₃(t) = tri(t, f=2)',
        graph_label_cont='Señal Continua',
        graph_label_disc='Muestras',
        x_label='Tiempo [s]',
        y_label='Amplitud'
    )
    
def square_frequency_signal():
    frequency = 2
    time_initial = 0
    time_final = 2
    number_of_points = 1000
    Ts = 0.01  # Periodo de muestreo heurístico

    # Señal continua
    t_cont = np.linspace(time_initial, time_final, number_of_points)
    x_cont = square(2 * np.pi * frequency * t_cont)

    # Señal discreta
    t_disc = np.arange(time_initial, time_final, Ts)
    x_disc = square(2 * np.pi * frequency * t_disc)

    # Graficar ambas
    combined_plotter(
        t_cont, x_cont,
        t_disc, x_disc,
        title='x₄(t) = sq(t, f=2)',
        graph_label_cont='Señal Continua',
        graph_label_disc='Muestras',
        x_label='Tiempo [s]',
        y_label='Amplitud'
    )
