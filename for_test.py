import requests
import json


def start_test():
    url = 'http://127.0.0.1:8000/get_form/'
    s = requests.Session()
    to_test = [

            {
                'my_date': '12.12.2001',
                'my_phone': '89196575875',
                'my_mail': 'fl4shr21@yandex.ru',
                'my_text': 'Some text',
            },
            {
                'date': '12.12.2001', # Изменили название поля
                'my_phone': '89196575875',
                'my_mail': 'fl4shr21@yandex.ru',
                'my_text': 'Some text',
            },
            {
                'date': '12.12.2001',  # Изменили название поля
                'my_phone': '89196575875',
                'my_mail': 'fl4shr21@yandex.ru',
                '_text': 'Some text', # Изменили название поля
            },
            {
                'my_date': '12.12.2001',  # Изменили название поля
                'my_phone': '89196575875',
                'my_mail': 'fl4shr21@yandex.ru',
                '_text': 'Some text',
            },

            {
                'email':'test@gmail.com', 
            },
            {
                'email': 'test@@@gmail.com',
            },

    ]
    print('-'*200)
    for obj in to_test:
        response = s.post(url, data=obj)
        print(f'Запрос\n{obj}')
        print(f'Ответ\n{json.dumps(response.json(), indent=4)}')
        print('-'*200)


if __name__ == '__main__':
    start_test()
