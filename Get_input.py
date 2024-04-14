def get_input(max_digit: int):
    max_try = 5

    for try_cnt in range(1, max_try + 1):
        print(f'\nTry number: {try_cnt}')
        user_input = input('>')

        if len(user_input) != max_digit or not user_input.isdigit():
            if try_cnt < max_try:
                messages = ['Please Enter a 3 digit number!',
                            '3 DIGIT number!',
                            'Why do not you enter a 3 digit number?',
                            ':(']
                print(messages[try_cnt - 1])
            else:
                print('I asked you to enter a 3 digit number 5 times but you did not pay attention!')
        else:
            return user_input


input_number = get_input(3)
print(input_number)