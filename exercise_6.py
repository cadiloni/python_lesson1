
user_input = int(input('First day distance you covered in kilometers(km) '))
goal_distance = int(input('Your goal distance that you wish to reach '))
days_required = 1

while goal_distance - user_input > 0:
    user_input = user_input + (user_input * 0.1)
    days_required += 1
    print(f'In the {days_required} day: {user_input:.2f}')

print(f'It takes you {days_required} days to reach your goal:) I wish you good luck! ')
