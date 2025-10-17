text = input("Введіть речення: ")
words = text.split()
print("Кількість слів: ", len(words))
print("Найдовше слово: ", max(words, key=len))
