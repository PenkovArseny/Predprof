# Достаёт из csv файла данные и кладёт в список A
with open("products.csv", "r", encoding="utf-8-sig") as f:
    A = f.readlines()
    for i in range(len(A)):
        A[i] = A[i].split(";")
        A[i][-1] = A[i][-1][:-1]
a = input()
while a != "молоко": # будет выполняться пока не молоко
    prodmin = 10 ** 9 # большое значние для нахождения минимума
    flag = False # флаг, чтобы определить, нашли ли мы минимиум
    for i in range(len(A)):
        if A[i][0] == a:
            flag = True
            if int(A[i][-1][:-2]) < prodmin: # операция сравнения
                prodmin = int(A[i][-1][:-2])
                otv = i
    if flag: # если нашли
        print(f"В категории: {A[otv][0]} товар: {A[otv][1]} был куплен {A[otv][-1]} раз")
    else: # если не нашли
        print("Такой категории не существует в нашей БД")
    a = input() # повторный ввод
