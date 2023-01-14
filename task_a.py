import re
from typing import List
from unittest.mock import patch


def check_url(string: str) -> bool:
    '''Возвращает True, если переданная строка
    соответствует ссылке на проект в github. Иначе - False.'''
    return (isinstance(string, str)
            and re.fullmatch(r'http(s)?://github.com/.+/.+(\.git)?(/)?',
                             string))


def git_url_parse(links: List[str]) -> None:
    '''Принимает список ссылок на проекты в github,
    печатает в консоль названия этих проектов.'''
    for link in links:
        if not check_url(link):
            print(f'"{link}" не соответствует формату ссылки на проект гитхаб')
            continue
        name = link.split('/')[-1]
        print(name.split('.')[0]) if name.endswith('.git') else print(name)


@patch('builtins.print')
def test(mock_print):
    '''Тестирование функции-парсера ссылок на github.'''
    git_url_parse(['https://github.com/miguelgrinberg/Flask-SocketIO'])
    mock_print.assert_called_with('Flask-SocketIO')
    git_url_parse(['https://github.com/another_user/another_project.git'])
    mock_print.assert_called_with('another_project')
    git_url_parse(['random string'])
    mock_print.assert_called_with(('"random string" не соответствует '
                                   'формату ссылки на проект гитхаб'))
    git_url_parse([[1, 2]])
    mock_print.assert_called_with(('"[1, 2]" не соответствует формату '
                                   'ссылки на проект гитхаб'))


if __name__ == '__main__':
    test()
