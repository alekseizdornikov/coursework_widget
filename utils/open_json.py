import json


def open_json():
    '''
    Функция энкодирования файла operations.json
    '''
    with open('operations.json', encoding='utf-8') as file:
        list_operations = json.load(file)
        return list_operations

#print(open_json())