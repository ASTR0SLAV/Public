ticket_count = int(input("Введите колличество билетов:"))
total_sum = 0
for i in range(ticket_count):
    age = int(input("Введите возраст:"))
    if age<=18:
        total_sum = total_sum + 0
    elif age>18 and age<25:
        total_sum = total_sum + 990
    elif age>=25:
        total_sum = total_sum + 1390
if ticket_count>=3:
    total_sum = total_sum-(total_sum*10/100)
print(total_sum, "руб.")




