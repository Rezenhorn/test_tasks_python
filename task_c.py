from typing import List, Union
from unittest.mock import patch


def process_list(lst: List[Union[str, int]]) -> None:
    '''Функция принимает список элементов (состоящий из строк и цифр),
    возвращает новый список, с условием - если элемент списка был строкой,
    начало строки добавляет "abc_", в конец строки - "_cba".
    Если элемент был int - возводит в квадрат.'''
    print(list(map(lambda x: f'abc_{x}_cba' if isinstance(x, str)
                   else x**2, lst)))


@patch('builtins.print')
def test(mock_print):
    '''Тестирование функции преобразования двух списков в словарь.'''
    process_list([3, 2, '1'])
    mock_print.assert_called_with([9, 4, 'abc_1_cba'])
    process_list([])
    mock_print.assert_called_with([])


if __name__ == '__main__':
    test()
