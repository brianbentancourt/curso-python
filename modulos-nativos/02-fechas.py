import time
from datetime import datetime

# timestamp
print(time.time())

fecha = datetime(2023, 1, 1)
fecha2 = datetime(2023, 2, 1)
print(fecha)
print(fecha > fecha2)
print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute
)

ahora = datetime.now()
print(ahora)

fechaStr = datetime.strptime("2023-01-03", "%Y-%m-%d")
print(fechaStr)

print(fecha.strftime("%Y.%m.%d"))

# directivas de fechas
# https://docs.python.org/3/library/datetime.html
