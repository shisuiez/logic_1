import random

arr = []
D = 3


for r in range(7):
    r = random.randint(0, 7)
    arr.append(r)

print("Исходный массив:", arr)


new = 6
arr.append(new)
print("Массив после добавления:", arr)


m = 0
for i in arr:
    if i == D:
        m += 1

print(f"Число {D} встречается", m, "раз(а)")


a = int(input("Задайте индекс: "))
if 0 <= a < len(arr):
    arr.pop(a)
    print("Результат после удаления:", arr)
else:
    print("Неверный индекс")
