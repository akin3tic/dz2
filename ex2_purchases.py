import csv

with open("purchases.csv", "w", newline="", encoding="utf-8-sig") as p:
    w = csv.writer(p, delimiter = ";")
    w.writerow(["Товар", "Цена за штуку", "Количество"])
    w.writerow(["Тетрадь", 2.50, 4])
    w.writerow(["Ручка", 1.20, 3])
    w.writerow(["Папка", 4.00, 2])
    w.writerow(["Маркер", 3.30, 1])
c = []
with open("purchases.csv", "r", newline="", encoding="utf-8-sig") as p:
    r = csv.DictReader(p, delimiter = ";")
    for i in r:
        print(dict(i))
        ic = round(float(i["Цена за штуку"]) * int(i["Количество"]), 2)
        c.append(ic)
print("Стоимость за товар соответственно: ", c)
print("Общая сумма: ", sum(c))