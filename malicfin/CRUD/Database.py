from . import Operasi

DB_NAME = 'data.txt'

TEMPLATE = {
    "pk" : "XXXXXX",
    "date_add": "yyyy-mm-dd",
    "title": 225*" ",
    "author": 225*" ",
    "year": "yyyy",
}

def init_console():
    try:
        Operasi.hello()
        with open(DB_NAME, 'r') as file:
            print("Database is available, init done!")
    except:
        print('Database is not found!, Please make a new database!')
        Operasi.create_first_data()
        # with open(DB_NAME, 'w', encoding='utf-8') as file:
        #     author = input('Author : ')
        #     title = input('Title : ')
        #     year = input('Year : ')
        #     data_str = f"{author},{title},{year}"
        #     file.write(data_str)