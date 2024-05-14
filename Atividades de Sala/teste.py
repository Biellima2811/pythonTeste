import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sinal
amplitude = 1.0
frequencia_inicial = 1.0  # Frequência inicial em Hertz
frequencia_final = 2.0    # Frequência final em Hertz
tempo_inicio = 0
tempo_fim = 2
taxa_amostragem = 1000    # Número de pontos no gráfico

# Número hexadecimal para identificar a transmissão
numero_hexadecimal = 0xABCDEF

# Criação do vetor de tempo usando a função linspace
tempo = np.linspace(tempo_inicio, tempo_fim, int((tempo_fim - tempo_inicio) * taxa_amostragem), endpoint=False)

# Criação do sinal senoidal com frequência variável
# A função linspace é utilizada novamente para criar um vetor de frequência linearmente espaçado
frequencia = np.linspace(frequencia_inicial, frequencia_final, len(tempo))
sinal = amplitude * np.sin(2 * np.pi * frequencia * tempo)

# Plotagem do gráfico
plt.plot(tempo, sinal)
plt.title(f'Sinal Analógico - Oscilação entre 1 e 2 Hertz\nTransmissão: 0x{numero_hexadecimal:X}')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
