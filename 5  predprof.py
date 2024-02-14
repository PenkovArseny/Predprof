# Достаёт из csv файла данные и кладёт в список A
with open("products.csv", "r", encoding="utf-8-sig") as f:
    A = f.readlines()
    for i in range(len(A)):
        A[i] = A[i].split(";")
        A[i][-1] = A[i][-1][:-1]
A.pop(0)
key = []
val = []
B = []
hash = {}
for i in range(len(A)):
    if A[i][0] not in key:
        key.append(A[i][0])
        val.append([])
    else:
        val[key.index(A[i][0])].append(A[i][-1])
for i in range(len(key)):
    hash[key[i]] = val[i]
for i in A:
    B.append([int(i[-1][:-2]), i[0]])
B = sorted(B)
for i in range(10):
    print(B[i][1], B[i][0])
