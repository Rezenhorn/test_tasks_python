import re
import time
from collections import Counter


def time_of_function(method):
    '''Декоратор, измеряющий время выполнения функции/метода.'''
    def wrapped(*args, **kwargs):
        start_time = time.perf_counter()
        result = method(*args, **kwargs)
        total_time = time.perf_counter() - start_time
        print(f'Время выполнения метода {method.__name__}: {total_time:.5f} с')
        return result
    return wrapped


def time_all_methods(cls):
    '''Декоратор класса, выводящий в консоль время выполнения методов.'''
    class NewCls:
        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)

        def __getattribute__(self, attribute):
            '''Возвращает атрибут класса декоратора сразу же,
            а атрибут исходного класса проверяет, является ли
            он методом. Если да - оборачивает его в декоратор
            time_of_function.
            '''
            try:
                x = super().__getattribute__(attribute)
            except AttributeError:
                pass
            else:
                return x
            attr = self._obj.__getattribute__(attribute)
            if isinstance(attr, type(self.__init__)):
                return time_of_function(attr)
            return attr
    return NewCls


@time_all_methods
class Text:
    def __init__(self, content: str) -> None:
        self.content = content
        self.word_list = re.findall(r"(\w[\w']*\w|\w)", self.content)

    def max_length_word(self) -> None:
        '''Печатает самое длинное слово в тексте.'''
        print('Самое длинное слово:', max(self.word_list, key=len))

    def most_frequent_word(self) -> None:
        '''Печатает самое встречающееся слово.'''
        print('Cамое частое слово:', min(Counter(self.word_list).items(),
              key=lambda x: (-x[1], x[0]))[0])

    def special_symbol_count(self) -> None:
        '''Печатает количество спецсимволов в тексте.'''
        print('Количество спецсимволов =',
              len(re.findall(r'[^\w\s]', self.content)))

    def print_palindromes(self) -> None:
        '''Печатает палиндромы из текста через запятую.'''
        print('Палиндромы:', ', '.join(set([word for word in self.word_list if
                                       word == word[::-1] and len(word) > 1])))


if __name__ == '__main__':
    test_text = Text('Привет, это тестовый текст. Тут мы проверяем работу '
                     'класса и его методов. Для теста нам потребуется '
                     'палиндром: это будет tenet. И еще очень длинное слово: '
                     'превысокомногорассмотрительствующий. Да, это реальное '
                     'слово!')

    test_text.max_length_word()
    test_text.most_frequent_word()
    test_text.special_symbol_count()
    test_text.print_palindromes()
