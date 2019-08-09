number = 3
running = True

while running:
    guess = int(input('an integer'))
    if guess == number:
        print('相等')
        running = False
    elif guess < number:
        print('小')
    else:
        print('大')
else:
    print('while is over')
