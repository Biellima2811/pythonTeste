matriz = [[10, 9, 8],
          [7, 8, 6]]
media = 0

for i in range(2):
    for j in range(3):
        media = matriz[i][j] + media

media = media / 6
print(media)
