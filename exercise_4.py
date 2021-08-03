user_input = abs(int(input("Пожалуйста, введите целое и положительное число --> ")))
maximum = user_input % 10

while user_input >= 1:

    user_input = user_input // 10

    if user_input % 10 > maximum:
        maximum = user_input % 10
    if user_input > 9:
        continue
    else:
        print("Максимальное цифра в числе ", maximum)
        break
