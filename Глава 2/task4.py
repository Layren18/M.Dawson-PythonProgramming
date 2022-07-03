cost = float(input("Введите стоимость автомобиля в рублях: "))
nalog = cost * 0.1
reg_sbor = cost * 0.15
agent_sbor = 5000
delievery = 20000
final_cost = cost + nalog + reg_sbor + agent_sbor + delievery
print("Финальная стоимость автомобиля с учётом налога, рег. сбора, агентского сбора, доставки автомобиля составляет: " + str(final_cost) + " рублей.")