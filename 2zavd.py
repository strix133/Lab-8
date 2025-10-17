n = int(input("Кількість рядків: "))
result = []

for i in range(n):
    s = input(f"Введіть рядок {i+1}: ")
if len(s) % 2 != 0:
    print("Рядок має бути з пароною кількістю букв!")
    exit()
mid = len(s)  // 2
new_s = s[:mid-1] + s[mid-1:mid+1].upper() + s[mid+1:]
result.append(new_s)

print("Результат:")
for r in result:
    print(r)
