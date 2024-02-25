"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
Сумма рассчитывается как ставка умноженная на процент премии
"""
name = ['Вася','Петя','Алексей']
rates = [100, 200, 300]
bonuses = ['10%', '20%', '30%']

def generate_bonus_dict(names, rates, bonuses):
    return {name: rate * float(bonus.rstrip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)}

bonus_dict = generate_bonus_dict(name, rates, bonuses)

print(bonus_dict)