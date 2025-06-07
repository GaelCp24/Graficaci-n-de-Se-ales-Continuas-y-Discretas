from src.utils.grapher import continuous_plotter
import matplotlib.pyplot as plt
import numpy as np

def continous_sinusoidal_sign(frequency):
    frequency = float(frequency)
    amplitude = 1
    number_of_points = 10000
    time_initial = 0
    time_final = 5
    time = np.linspace(time_initial, time_final, number_of_points)
    
    x_t = amplitude * np.sin(2 * np.pi * frequency * time)
    
    continuous_plotter(
        time, x_t,
        'Señal Sinusoidal Continua', 'Señal De Onda Sinusoidal',
        'Time[s]', 'Amplitude'
    )
    
    