import scipy
import scipy.signal

def f(x):
    return x

def g(x):
    return x

x_vals = np.linspace(0, 1, 1000)
f_list = [f(x) for x in x_vals]
g_list = [g(x) for x in x_vals]
result = np.convolve(f_list, g_list)

x_vals = np.linspace(0, 1, 44100)
signal2 = [np.sin(500 * x) for x in x_vals]

signal2_scaled = np.multiply(signal2 * 10000)
write('signal2.wav', 44100, signal2_scaled)

