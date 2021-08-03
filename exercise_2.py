# Seconds to fully understandable hh.mm.ss format
user_input_seconds = int(input("Введите время в секундах для конвертации его на чч:мм:сс формат -->"))

hours = user_input_seconds // (60**2)
user_input_seconds %= (60**2)
minutes = user_input_seconds // 60
user_input_seconds %= 60

print("%02i:%02i:%02i" % (hours, minutes, user_input_seconds))
