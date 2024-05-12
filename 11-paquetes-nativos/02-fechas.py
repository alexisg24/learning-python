# import time

# print(time.time()) <- timestamp

from datetime import datetime

fecha = datetime(2023, 1, 20)
ahora = datetime.now()
print(ahora)
print(fecha)

fecha_str = datetime.strptime("2023-01-15", "%Y-%m-%d")
print(fecha_str)

str_fecha = ahora.strftime("%Y.%m.%d")
print(str_fecha)
print(ahora > fecha)
print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.hour
)
