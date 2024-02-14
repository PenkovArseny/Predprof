# Достаёт из csv файла данные и кладёт в список A
with open("products.csv", "r", encoding="utf-8-sig") as f:
    A = f.readlines()
    for i in range(len(A)):
        A[i] = A[i].split(";")
        A[i][-1] = A[i][-1][:-1]

c = 0
# Добавляем столбец total
A[0].append("total")
for i in range(1, len(A)):
    A[i].append(str(int(A[i][-1][:-2]) * int(A[i][-2][:-2]))) # Вычисляем значение для каждой строки в столбец total
    if A[i][0] == "Закуски": # Попутно ищем продажи Закусок
        c += int(A[i][-1])
# Из списка A записывает в новый csv файл
with open("products_new.csv", "w", encoding="utf-8-sig") as f:
    for i in range(len(A)):
        f.write(";".join(A[i]))
        f.write("\n")
print(c)
