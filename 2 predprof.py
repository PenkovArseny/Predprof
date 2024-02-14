# Достаёт из csv файла данные и кладёт в список A
with open("products.csv", "r", encoding="utf-8-sig") as f:
    A = f.readlines()
    for i in range(len(A)):
        A[i] = A[i].split(";")
        A[i][-1] = A[i][-1][:-1]
A.pop(0)
q = "ЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯЯ"
mark = []
# Ищем категория которая имеет наименьшее лексигрофическое значение
for i in range(len(A)):
    if A[i][0] == q:
        mark.append(i)
    elif A[i][0] < q:
        mark = [i]
        q = A[i][0]
l = 0
# В этой категории ищем самый дорогой товар
for i in range(len(mark)):
    if int(A[mark[i]][-2][:-2]) > l:
        l = int(A[mark[i]][-2][:-2])
        bes = int(mark[i])
print(
    f"В категории: {A[mark[0]][0]} самый дорогой товар: {A[bes][1]} его цена за единицу товара составляет {A[bes][-2]}")
