from datetime import datetime, timedelta

fecha1 = datetime(2023, 1, 1) + timedelta(days=5)
fecha2 = datetime(2023, 2, 1)

print(fecha1)
delta = fecha2-fecha1
print(delta)
print("dias", delta.days)
print("segundos", delta.seconds)
print("microsegundos", delta.microseconds)
print("totalsegundos", delta.total_seconds())
