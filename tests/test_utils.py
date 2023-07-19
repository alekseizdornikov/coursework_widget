from utils import sort_func


def test_sort_execuded():
    assert sort_func.sort_execuded([{'state': 'EXECUTED'}]) == [{'state': 'EXECUTED'}]
    assert sort_func.sort_execuded([{'state': 'EXECUTED'}, {'state': 'erling'}]) == [{'state': 'EXECUTED'}]
    assert sort_func.sort_execuded([{'state': 'erling'}]) == []


def test_sort_date():
    assert sort_func.sort_date([{'date': '2011-01-07'}, {'date': '2011-01-01'}]) == [{'date': '2011-01-01'},
                                                                                     {'date': '2011-01-07'}]
    assert sort_func.sort_date([]) == []

def test_last_operations():
    assert sort_func.last_operations([1, 2, 3, 4, 5, 6]) == [6, 5, 4, 3, 2]
