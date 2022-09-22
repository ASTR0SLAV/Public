per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
L = (per_cent.values())
c = list(map(float, L))
money = int(input("money = "))
my_new_list = [money * i/100 for i in c]
print("deposit =",my_new_list)
deposit = max(my_new_list)
print("Максимальная сумма, которую вы можете заработать —",deposit)