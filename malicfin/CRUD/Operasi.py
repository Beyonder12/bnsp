from . import Database
import random
import string

def hello():
    print('hello')

def create_first_data():
    data = Database.TEMPLATE.copy()
    data['pk'] = ''.join(random.choice(string.ascii_letters) for i in range(6))

    print(data["pk"])

    author: input('Author : ')
    title: input('Title : ')
    year: input('Year : ')

   



