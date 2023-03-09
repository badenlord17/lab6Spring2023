while True:
    print('Menu\n-------------\n1. Encode  \n2. Decode  \n3. Quit')
    print('\n')
    op = input('Please enter an option: ')
    if op == '1':
        var = input('Please enter your password to encode: ')
        new_string = ''
        for i in var:
            temp = int(i)
            temp += 3
            if temp >= 10:
                temp -= 10
            new_string += str(temp)
        print('Your password has been encoded and stored!')
    elif op == '2':
        pass
    elif op == '0':
        break
