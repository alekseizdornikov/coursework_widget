# from open_json import open_json
def sort_execuded(list_oper):
    '''
    Функция сортировки выполненных операций
    '''
    sort_list = []
    for ex in list_oper:
        if len(ex) == 0:
            continue
        if ex['state'] == 'EXECUTED':
            sort_list.append(ex)
        else:
            continue
    return sort_list


# print(sort_execuded(open_json()))

def sort_date(list_execuded):
    '''
    Функция сортировки массива по дате операции
    '''
    sort_list = sorted(list_execuded, key=lambda x: x['date'])
    return sort_list


# print(sort_date(sort_execuded(open_json())))


def last_operations(list_sorted):
    '''
    Функция вывода последних 5-ти операций
    '''
    last_five = list_sorted[-5:]
    last_five_rev = last_five[::-1]
    return last_five_rev

# print(last_operations(sort_date(sort_execuded(open_json()))))
