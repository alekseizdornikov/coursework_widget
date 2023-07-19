from open_json import open_json
from sort_func import sort_execuded, sort_date, last_operations

list_last_operations = last_operations(sort_date(sort_execuded(open_json())))
for key in list_last_operations:
    # Условие для открытия вкладов
    if len(key) == 6:
        date = key["date"] # Корректируем вывод даты
        date = date[:10]
        new_date = date.split("-")
        amount = key["operationAmount"] # Сумма перевода
        currency = amount["currency"] # Наименование валюты
        blok_code = key["to"] # Создаем шифр счёта "to"
        blok_code = blok_code.split(" ")
        new_blok_code = list(blok_code[1])
        new_blok_code = new_blok_code[-4:]
        new_blok_code = "".join(new_blok_code)
        print(f'{new_date[2]}.{new_date[1]}.{new_date[0]} {key["description"]}\n'
              f'{blok_code[0]} **** **** **** **** {new_blok_code}\n'
              f'{amount["amount"]} {currency["name"]}\n')
    # Условие для переводов
    else:
        date = key["date"]
        date = date[:10]
        new_date = date.split("-")
        amount = key["operationAmount"]
        currency = amount["currency"]
        blok_code = key["to"]
        blok_code = blok_code.split(" ")
        new_blok_code = list(blok_code[1])
        new_blok_code = new_blok_code[-4:]
        new_blok_code = "".join(new_blok_code)
        blok_code_2 = key["from"] # Создаем шифр счёта "from"
        blok_code_2 = blok_code_2.split(" ")
        new_blok_code_2 = list(blok_code_2[-1])
        new_blok_code_2 = new_blok_code_2[-4:]
        new_blok_code_2 = "".join(new_blok_code_2)

        print(f'{new_date[2]}.{new_date[1]}.{new_date[0]} {key["description"]}\n'
              f'{" ".join(blok_code_2[:-1])} **** **** **** {new_blok_code_2} -> {blok_code[0]} **** **** **** **** {new_blok_code}\n'
              f'{amount["amount"]} {currency["name"]}\n')
