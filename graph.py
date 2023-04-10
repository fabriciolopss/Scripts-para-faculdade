import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

def x(t):
    return ((1.891 * 0.017) * 10 ** -2) * np.sin((14.95007 * t + 0.224000027))

t = np.linspace(-1.2, 1.2, 1000) # gera 1000 valores entre 0 e 10
y = x(t) # calcula os valores de x para cada valor de t

plt.plot(t, y, label = "Função x(t)")
plt.xlabel('t')
plt.ylabel('x(t)')
plt.ylim(-0.0006,0.0006) # Alterando a escala do gráfico
amplitude = np.max(y)
plt.axhline(y= amplitude, color='r', linestyle=':', label = "Amplitude")
plt.axhline(y= -amplitude, color='r', linestyle=':')
plt.axvline(x=0, color='black', linestyle='-') # traçando a linha do eixo x
plt.axhline(y = 0, color = "black", linestyle = "-") #traçando a linha do eixo y

# Encontra os índices dos pontos de máximo da função
max_indices = argrelextrema(y, np.greater)

# Calcula o período da função
period = t[max_indices[0][-1]] - t[max_indices[0][0]]

# Traça uma linha vertical em cada ponto de máximo da função
for i in max_indices[0]:
    plt.axvline(x=t[i], color='blue', linestyle='--', alpha = 0.7) 
    print(t[i])
    plt.text(t[i]+ abs(0.1 * t[2]), amplitude, '1 periodo')
plt.axhline(y= 10, color = 'blue', linestyle = '--', alpha=0.7, label = "Periodo") # Definindo da legenda

# Adiciona um texto com o valor do período no gráfico
plt.text(2, amplitude/2, f'Período = {period:.2f}', fontsize=12)


plt.legend()
plt.show()
