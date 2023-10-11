import os

if __name__ == "__main__":
    while(True):
        operation_system = os.name
        match operation_system:
            case "posix": os.system('clear')
            case 'nt': os.system('cls')

        print('WELCOME TO THE APPLICATION')
        print('DATABASE OF LIBARY')
        print('===========================')
        print(f'1. Create Data')
        print(f'2. Read Data')
        print(f'3. Update Data')
        print(f'4. Delete Data')

        user_option = input( '\nInput your option: ')
        print('\n===========================\n')
        match user_option:
            case "1": print("Create Data")
            case "2": print("Read Data")
            case "3": print("Update Data")
            case "4": print("Delete Data")

        print('\n===========================\n')
        is_done = input('Is it done?(yes/no/y/n)')
        if is_done.lower() == 'y' or is_done == 'yes':
            os.system('clear');break
    print("\nProgram is Over. Thanks!\n")

