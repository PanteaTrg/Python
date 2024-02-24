from Account import *

# An empty dictionary for keeping account's information
account_dict = {}

# Creating two accounts
next_acc_number = 0

a_account = Account('pantea', 1000, '@@123')
account_dict[next_acc_number] = a_account
next_acc_number += 1

b_account = Account('reza', 2000, '@@321')
account_dict[next_acc_number] = b_account

# Uncomment in case of error
# account_dict[0].show()
# print()
#
# account_dict[1].show()
# print()

# Interactive Menu
while True:

    print()
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press o to open a new account')
    print('Press w to make a withdrawal')
    print('Press s to show all the accounts')
    print('Press q to quit')
    print()

    action = input('What do you want to do? Please enter a word: ').lower()[0]

    if action == 'b':
        print('*** Get Account balance ***')
        print()

        user_acc_number = int(input('Please enter your account number: '))
        if user_acc_number in account_dict:
            user_acc_password = input('please enter your account password: ')
            user_balance = account_dict[user_acc_number].getbalance(user_acc_password)
            if user_balance is not None:
                print('Your balance is: ', user_balance)
                print()
        else:
            print('Wrong account number!')
            print()

    elif action == 'd':
        print('*** Make a Deposit ***')
        print()

        user_acc_number = int(input('Please enter your account number: '))
        if user_acc_number in account_dict:
            user_acc_password = input('please enter your account password: ')
            user_input_amount = int(input('Please enter the amount: '))
            user_acc_new_balance = account_dict[user_acc_number].deposit(user_input_amount, user_acc_password)
            if user_acc_new_balance is not None:
                print('Your new balance is: ', user_acc_new_balance)
                print()
                print()
        else:
            print('Wrong Account number!')
            print()
            print()

    elif action == 'o':
        print('*** Open a New Account ***')
        print()
        acc_name = input('Please enter a name for the account: ')
        acc_balance = input('Please enter the initial balance: ')
        acc_password = input('Please choose a password for your account: ')

        next_acc_number += 1
        account_dict[next_acc_number] = Account(acc_name, acc_balance, acc_password)
        print('Your new account number is: ', next_acc_number)
        next_acc_number += 1
        print()

    elif action == 'w':
        print('*** Withdraw from Account ***')
        print()

        user_acc_number = int(input('Please enter your account number: '))
        if user_acc_number in account_dict:
            user_acc_password = input('please enter your account password: ')
            user_withdraw_amount = int(input('Please enter the amount: '))
            new_balance = account_dict[user_acc_number].withdraw(user_withdraw_amount, user_acc_password)
            if new_balance is not None:
                print('Your new balance is: ', new_balance)
        else:
            print('Wrong Account number!')
            print()
            print()

    elif action == 's':
        print('*** Show all Account ***')
        print()
        for acc_number in account_dict:
            print('Account number: ', acc_number)
            account_dict[acc_number].show()

    elif action == 'q':
        break

    else:
        print('Sorry! this is not a valid action. Try again later')

    if input('Do you wish to continue? : ').lower() == 'n':
        print('Hope to see you soon. Bye')
        break


