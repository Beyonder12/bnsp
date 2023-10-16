import os


while True:
    try:
        # os.system('clear')
        
        print(' Welcome to The Club')
        print('====================')
        print('1. Input your name. ')
        print('2. Exit.')
        option = input('Input your options: ')

        if option == '2':
            print('Thanks for coming!')
            break
        name = input('Name: ')
        print('\nHello, Mr./Mrs.', name + '\n')
        print('====================')
        option/5
    except:
        pass
    