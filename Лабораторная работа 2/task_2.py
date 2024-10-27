salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

new_spend = spend
money_capital = new_spend - salary

for i in range (months-1):
    new_spend += new_spend * increase
    money_capital += new_spend - salary

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round (money_capital))
