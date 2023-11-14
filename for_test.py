import requests
import json


def start_test():
    url = 'http://127.0.0.1:8000/get_form/'
    s = requests.Session()
    to_test = [

            {
                'date': '12.12.2001',
                'phone': '89196575875',
                'email': 'fl4shr21@yandex.ru',
                'text': 'Some text',
            },
            {
                'date': '12-12-2001', # Поменяли формат даты на недопустимый
                'phone': '89196575875',
                'email': 'fl4shr21@yandex.ru',
                'text': 'Some text',
            },
            {
                'date': '2001-10-25',
                'phone': '89196575875',
                'email': 'fl4shr21@yandex.ru',
                'text': 'Some text',
            },
            {
                'date': '2001-10-25',
                'phone': '89196575875',
                'email': 'fl4shr21yandex.23ru', # Поменяли формат email на недопустимый
                'text': 'Some text',
            },
            {
                'date': '2001-10-25',
                'phone': '89196575875',
                'email': 'fl4shr21@yandex.ru', 
            },
            {
                'date': '2001-10-25',
                'phone': '891965758752323', # Поменяли формат телефона на недопустимый
                'email': 'fl4shr21@yandex.ru', 
            },
            {
                'date': '2001-10-25',
                'phone': '891965758752323', # Поменяли формат телефона на недопустимый
                'email': 'fl4shr21@yandex.ru', 
            },
            {
                'text':'Some text',
            },
            {
                'email':'Some text', # Поменяли формат email на недопустимый
            },
            {
                'email':'test@gmail.com', 
            },
    ]
    print('-'*200)
    for obj in to_test:
        response = s.post(url, data=obj)
        print(f'Запрос{obj}')
        print(json.dumps(response.json(), indent=4))
        print('-'*200)


if __name__ == '__main__':
    start_test()
