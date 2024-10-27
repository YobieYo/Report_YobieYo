money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

count = 0
new_spend = spend
new_money_capital = money_capital + salary - new_spend

while new_money_capital >= 0:
    count += 1
    new_spend += new_spend * increase
    new_money_capital = new_money_capital + salary - new_spend

print("Количество месяцев, которое можно протянуть без долгов:", count)