# Web-приложение для определения заполненных форм.

## Установка и запуск

 Для MacOs и Linux вместо python использовать python3

## **1. Клонировать репозиторий:**
```
git clone https://github.com/ViktorovGO/task_for_interview.git
```

## **2. Перейти в папку проекта:**
```
cd /task_for_interview/
```

## **3. Cоздать и активировать виртуальное окружение:**
```
python -m virtualenv venv
```

Для Windows:
```
venv\Scripts\activate.bat
```

Для MacOs/Linux:
```
source venv/bin/activate
```

## **4. Установить зависимости из файла requirements.txt:**
- Обновить пакетный менеджер pip
```
python -m pip install --upgrade pip
```

- Установить зависимости
```
pip install -r requirements.txt
```

## **5. Запустить веб сервер**
~~~
cd /backend/
~~~
~~~
python manage.py runserver
~~~

## **6. Запустить тестовый скрипт**
### 6.1 Открыть ещё одну консоль в корневой папке проекта
### 6.2 Активировать виртуальное окружение
### 6.3 Запустить скрипт
~~~
python for_test.py
~~~
