with open("diary.txt", "w", encoding="utf-8") as diary:
    diary.write("Сегодня мы работали с файлами Python.\n")
    diary.write("Научились сохранять текст.\n")
    diary.write("Узнали, как читать данные обратно.\n")
with open("diary.txt", "a", encoding="utf-8") as diary:
    diary.write("Следующее занятие – CSV и JSON\n")
with open("diary.txt", "r", encoding="utf-8") as diary:
    l = diary.readlines()
    c = len(l)
print("".join(l), end="")
print("Количество записей: ", c)