#Create by Gabriel Levi
import random
# Número de lançamento
num = 50
#Incialização de lista para armazenar os dados.
resultados = []
# Contador para ocorrencias face 6
ocorrencia_face_6 = 0

# Simulação de lançamentos de dados
for i in range(num):
    result_dado = random.randint(1, 6)
    resultados.append(result_dado)
    if result_dado == 6:
        ocorrencia_face_6 += 1
#Calcular percentual de ocorrencias de face 6
percent = (ocorrencia_face_6 / num) * 100

#Exibição de Resultados
print(f'Numeros Lançados: {resultados}')
print(f'Percentual de ocorrencias face 6: {percent:.2f}%')