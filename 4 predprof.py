# Достаёт из csv файла данные и кладёт в список A
with open("products.csv", "r", encoding="utf-8-sig") as f:
    A = f.readlines()
    for i in range(len(A)):
        A[i] = A[i].split(";")
        A[i][-1] = A[i][-1][:-1]
# Добавляем столбец промокодов
A[0].append("promocode")
for i in range(1, len(A)): # Создаём промокод
    A[i].append((A[i][1][:2]).upper() + A[i][2][:2] + (A[i][1][-2:])[::-1].upper() + (A[i][2][3:5])[::-1])
# Из списка A записывает в новый csv файл
with open("product_promo.csv", "w", encoding="utf-8-sig") as f:
    for i in range(len(A)):
        f.write(";".join(A[i]))
        f.write("\n")
