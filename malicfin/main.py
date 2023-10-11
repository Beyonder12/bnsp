import os

if __name__ == "__main__":
    operation_system = os.name

    match operation_system:
        case "posix": os.system('clear')
        case 'nt': os.system('cls')

    print('WELCOME TO THE APPLICATION')
    print('DATABASE OF LIBARY')
    print('===========================')

    while(True):
        print(f'1. Create Data')
        print(f'2. Read Data')
        print(f'3. Update Data')
        print(f'4. Delete Data')

        user_option = input('Input your option: ')

