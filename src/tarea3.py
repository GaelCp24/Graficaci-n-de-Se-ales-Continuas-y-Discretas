from src.utils.grapher import more_continous_signal
import matplotlib.pyplot as plt
import numpy as np
import math

def sinusoidal_cont_signal(frequency, amplitude, fase):
    frequency = float(frequency)
    amplitude = float(amplitude)
    fase = float(fase)
    #el dato de la fase ingressa en grados pero despues pasa a ser radianes
    fase = math.radians(fase)
    
    number_of_points = 10000
    time_initial = 0
    time_final = 5
    time = np.linspace(time_initial, time_final, number_of_points)
    
    user_signal = amplitude * np.sin(2 * np.pi * frequency * time + fase)
    
    ref_signal = np.sin(2 * np.pi * 1 * time) # A=1, f=1Hz, ϕ=0
    
    more_continous_signal(
        time,
        user_signal, ref_signal,
        f'User: A = {amplitude}, f = {frequency} Hz, ϕ = {fase} rad', 'Reference: A = 1, f = 1 Hz, ϕ = 0 rad',
        'Señal Sinusoidal x(t)=A*sin(2πft+ϕ) Continua', 'Time [s]', 'Amplitude'
    )
    
def sinusoidal_disc_signal(frequency, amplitude, fase):
    frequency = float(frequency)
    amplitude = float(amplitude)
    fase = float(fase)
    fase = math.radians(fase)
    
    Ts = 0.01
    samples = 100
    n = np.arange(samples)
    
    user_signal = amplitude * np.sin(2 * np.pi * frequency * n * Ts + fase)
    
    ref_signal = 1 * np.sin(2 * np.pi * 1 * n * Ts + 0)
    
    more_continous_signal(
        n,
        user_signal, ref_signal,
        f'User: A={amplitude}, f={frequency}, ϕ={fase} rad', 'Reference: A=1, f=1Hz, ϕ=0 rad',
        'Señal Sinusoidal x(t)=A*sin(2πft+ϕ) Discreta', 'Time [s]', 'Ampitude'
    )
    
    
    