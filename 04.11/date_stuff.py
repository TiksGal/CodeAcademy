# import datetime
# import locale

# locale.setlocale(locale.LC_TIME, 'lt_LT.UTF-8')
# x = datetime.datetime(2020, 2, 29, 18, 20, 50)
# print(x.strftime("%A, %d. %B %Y %I:%M%p"))

# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now - datetime.timedelta(days=5))
# print(now + datetime.timedelta(hours=5))
# print(now + datetime.timedelta(days=20, hours=8))

# import datetime
# now = datetime.datetime.now()
# nepriklausomybes_diena = datetime.datetime(1990, 3, 11)
# skirtumas = now - nepriklausomybes_diena
# print(skirtumas.days)

import datetime

pradzia = datetime.datetime.today()
for x in range(10000):
    print(x)

pabaiga = datetime.datetime.today()
print(f"Programa užtruko {(pabaiga - pradzia).total_seconds()}")