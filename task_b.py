from unittest.mock import patch


def form_dict(first_list: list, second_list: list) -> None:
    '''Принимает два списка и печатает словарь
    (ключ из первого списка, значение из второго), упорядоченный по ключам.'''
    if len(first_list) == len(second_list):
        print('Длина первого списка не должна быть равна длине второго.')
        return
    return print(dict(sorted({key: value for key, value in
                 zip(first_list, second_list)}.items(), key=lambda x: x[0])))


@patch('builtins.print')
def test(mock_print):
    '''Тестирование функции преобразования двух списков в словарь.'''
    form_dict([3, 2, 1], ['1', '2', '3', '4'])
    mock_print.assert_called_with({1: '3', 2: '2', 3: '1'})
    form_dict([1, 1, 1], ['1', '1', '1'])
    mock_print.assert_called_with('Длина первого списка не должна быть равна '
                                  'длине второго.')
    form_dict([100], [])
    mock_print.assert_called_with({})


if __name__ == '__main__':
    test()
